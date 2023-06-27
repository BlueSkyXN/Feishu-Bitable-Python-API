import requests
import configparser
import argparse
import json

def GET_APP_ACCESS_TOKEN(app_id=None, app_secret=None, config_file=None):
    # 读取配置文件
    config = configparser.ConfigParser()
    if config_file:
        config.read(config_file, encoding='utf-8')
    else:
        config.read('feishu-config.ini', encoding='utf-8')

    # 从配置文件获取参数
    if app_id is None:
        app_id = config.get('ID', 'app_id')
    if app_secret is None:
        app_secret = config.get('ID', 'app_secret')

    # 构建请求URL和请求头
    url = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal"
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
    }

    # 构建请求体
    payload = {
        "app_id": app_id,
        "app_secret": app_secret
    }

    # 发起请求
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response_json = response.json()
    
    # 更新配置文件
    # if 'app_access_token' in response_json:
    #     config.set('TOKEN', 'app_access_token', response_json['app_access_token'])
    #     if config_file:
    #         with open(config_file, 'w', encoding='utf-8') as configfile:
    #             config.write(configfile)
    #     else:
    #         with open('feishu-config.ini', 'w', encoding='utf-8') as configfile:
    #             config.write(configfile)

    return response_json.get('app_access_token')

def GET_APP_ACCESS_TOKEN_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--id', help='app ID')
    parser.add_argument('-s', '--secret', help='app secret')
    parser.add_argument('--config_file', help='config file path')
    args = parser.parse_args()

    # 调用GET_APP_ACCESS_TOKEN函数，获取app_access_token
    app_access_token = GET_APP_ACCESS_TOKEN(args.id, args.secret, args.config_file)
    
    # 打印结果
    print(f'app_access_token: {app_access_token}')

# 主函数
if __name__ == "__main__":
    GET_APP_ACCESS_TOKEN_CMD()
