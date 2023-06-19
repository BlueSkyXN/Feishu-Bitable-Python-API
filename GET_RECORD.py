import requests
import configparser
import json
import argparse

def GET_RECORD(app_token=None, table_id=None, record_id=None, user_access_token=None):
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('feishu-config.ini')

    # 如果参数为空，则使用配置文件中的默认值
    if not app_token:
        app_token = config.get('TOKEN', 'app_token')
    if not table_id:
        table_id = config.get('ID', 'table_id')
    if not record_id:
        record_id = config.get('ID', 'record_id')
    if not user_access_token:
        user_access_token = config.get('TOKEN', 'user_access_token')

    # 构造请求URL和头部
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}"
    headers = {
        'Authorization': f'Bearer {user_access_token}',
        'Content-Type': 'application/json; charset=utf-8'
    }

    # 发起请求，并返回响应体的json形式
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--app_token', help='app token')
    parser.add_argument('--table_id', help='table id')
    parser.add_argument('--record_id', help='record id')
    parser.add_argument('--user_access_token', help='user access token')
    args = parser.parse_args()

    # 调用封装的函数，使用命令行参数或默认值
    response_body = GET_RECORD(args.app_token, args.table_id, args.record_id, args.user_access_token)
    print(json.dumps(response_body, indent=4))
