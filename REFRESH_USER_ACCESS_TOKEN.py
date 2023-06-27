import requests
import configparser
import json
import os
import argparse

def REFRESH_USER_ACCESS_TOKEN(app_access_token=None, refresh_token=None, config_file=None):
    if config_file is None:
        config_file = 'feishu-config.ini'

    # 确保配置文件存在
    if not os.path.exists(config_file):
        with open(config_file, 'w') as f:
            pass

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    # 确保 TOKEN 部分存在
    if not config.has_section('TOKEN'):
        config.add_section('TOKEN')

    # 从配置文件或者参数获取令牌
    app_access_token = app_access_token if app_access_token is not None else config.get('TOKEN', 'app_access_token', fallback=None)
    refresh_token = refresh_token if refresh_token is not None else config.get('TOKEN', 'refresh_token', fallback=None)

    # 如果任一令牌不存在，需要用户先获取它
    if not app_access_token or not refresh_token:
        raise ValueError("Both app_access_token and refresh_token are required. Please get them first.")

    # 构建请求URL和请求头
    url = "https://open.feishu.cn/open-apis/authen/v1/refresh_access_token"
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': f'Bearer {app_access_token}'
    }

    # 构建请求体
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "app_access_token": app_access_token
    }

    # 发起请求
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response_json = response.json()

    # 检查响应状态码
    if response.status_code != 200:
        print(f"HTTP Error: {response_json}")
        return None

    # 检查响应体中的 code
    if response_json.get('code') != 0:
        print(f"Response Error: {response_json}")
        return None

    # 更新配置文件
    if 'data' in response_json and 'access_token' in response_json['data']:
        config.set('TOKEN', 'user_access_token', response_json['data']['access_token'])
        config.set('TOKEN', 'refresh_token', response_json['data']['refresh_token'])
        with open(config_file, 'w', encoding='utf-8') as configfile:
            config.write(configfile)

    return response_json.get('data', {}).get('access_token')

def REFRESH_USER_ACCESS_TOKEN_CMD():
    parser = argparse.ArgumentParser(description='Refresh user access token.')
    parser.add_argument('-a', '--app_token', type=str, help='The app access token.')
    parser.add_argument('-r', '--refresh', type=str, help='The refresh token.')
    parser.add_argument('--config_file', default='feishu-config.ini', help='config file path')
    args = parser.parse_args()

    user_access_token = REFRESH_USER_ACCESS_TOKEN(args.app_token, args.refresh, args.config_file)
    print(f'User Access Token: {user_access_token}')

if __name__ == "__main__":
    REFRESH_USER_ACCESS_TOKEN_CMD()
