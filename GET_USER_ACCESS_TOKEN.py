import requests
import configparser
import argparse
import json
import os

def GET_USER_ACCESS_TOKEN(login_code):
    # 配置文件路径
    config_path='feishu-config.ini'

    # 确保配置文件存在
    if not os.path.exists(config_path):
        with open(config_path, 'w') as f:
            pass

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')

    # 确保 TOKEN 部分存在
    if not config.has_section('TOKEN'):
        config.add_section('TOKEN')

    # 从配置文件获取参数
    app_access_token = config.get('TOKEN', 'app_access_token', fallback=None)

    # 如果app_access_token不存在，需要用户先获取它
    if not app_access_token:
        raise ValueError("app_access_token not found in the configuration file. Please get it first.")

    # 构建请求URL和请求头
    url = "https://open.feishu.cn/open-apis/authen/v1/access_token"
    headers = {
        'Authorization': f'Bearer {app_access_token}',
        'Content-Type': 'application/json; charset=utf-8',
    }

    # 构建请求体
    payload = {
        "grant_type": "authorization_code",
        "code": login_code
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
        with open(config_path, 'w', encoding='utf-8') as configfile:
            config.write(configfile)

    return response_json.get('data', {}).get('access_token')


def GET_USER_ACCESS_TOKEN_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--login_code', help='登录预授权码')
    args = parser.parse_args()

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('feishu-config.ini', encoding='utf-8')

    # 获取登录码，优先从命令行参数获取，没有则从配置文件获取
    login_code = args.login_code if args.login_code else config.get('TOKEN', 'login_code', fallback=None)

    if not login_code:
        raise ValueError("login_code is required either in command line argument or in the configuration file.")

    # 调用 GET_USER_ACCESS_TOKEN 函数，获取 user_access_token
    user_access_token = GET_USER_ACCESS_TOKEN(login_code)
    
    # 打印结果
    print(f'user_access_token: {user_access_token}')


# 主函数
if __name__ == "__main__":
    GET_USER_ACCESS_TOKEN_CMD()
