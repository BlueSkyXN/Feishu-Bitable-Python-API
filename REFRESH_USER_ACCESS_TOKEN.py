import requests
import configparser
import argparse
import json

def REFRESH_USER_ACCESS_TOKEN(token=None, refresh_token=None):
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('feishu-config.ini', encoding='utf-8')

    # 从配置文件获取参数
    if token is None:
        token = config.get('TOKEN', 'app_access_token')
    if refresh_token is None:
        refresh_token = token

    # 构建请求URL和请求头
    url = "https://open.feishu.cn/open-apis/authen/v1/refresh_access_token"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json; charset=utf-8',
    }

    # 构建请求体
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }

    # 发起请求
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response_json = response.json()
    
    if response.status_code == 200 and response_json.get('code') == 0:
        # 更新配置文件
        if 'access_token' in response_json.get('data', {}):
            config.set('TOKEN', 'user_access_token', response_json['data']['access_token'])
            config.set('TOKEN', 'refresh_token', response_json['data']['refresh_token'])
            with open('feishu-config.ini', 'w') as configfile:
                config.write(configfile)
    else:
        # 使用user_access_token再尝试一次
        if config.has_option('TOKEN', 'user_access_token'):
            REFRESH_USER_ACCESS_TOKEN(token, config.get('TOKEN', 'user_access_token'))

    return config.get('TOKEN', 'user_access_token')


def REFRESH_USER_ACCESS_TOKEN_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', help='app access token')
    parser.add_argument('-r', '--refresh', help='refresh token')
    args = parser.parse_args()

    # 调用REFRESH_USER_ACCESS_TOKEN函数，获取新的user_access_token
    user_access_token = REFRESH_USER_ACCESS_TOKEN(args.token, args.refresh)
    
    # 打印结果
    print(f'user_access_token: {user_access_token}')


# 主函数
if __name__ == "__main__":
    REFRESH_USER_ACCESS_TOKEN_CMD()
