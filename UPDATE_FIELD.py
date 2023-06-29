import requests
import configparser
import json
import argparse

def UPDATE_FIELD(app_token=None, table_id=None, field_id=None, field_name=None, field_type=None, config_file=None):
    if config_file is None:
        config_file = 'feishu-config.ini'

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    # 如果参数为空，则使用配置文件中的默认值
    if not app_token:
        app_token = config.get('TOKEN', 'app_token')
    if not table_id:
        table_id = config.get('ID', 'table_id')
    if not field_id:
        field_id = config.get('ID', 'field_id')
    if not field_name:
        field_name = config.get('LIST_FIELDS', 'field_name')
    if not field_type:
        field_type = config.getint('LIST_FIELDS', 'field_type', fallback=1)

    user_access_token = config.get('TOKEN', 'user_access_token')

    # 构造请求URL和头部
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields/{field_id}"
    headers = {
        'Authorization': f'Bearer {user_access_token}',
        'Content-Type': 'application/json; charset=utf-8'
    }

    # 构造请求体
    body = {
        'field_name': field_name,
        'type': field_type
    }

    # 发起请求，并返回响应体的json形式
    response = requests.put(url, headers=headers, data=json.dumps(body))
    return response.json()

def UPDATE_FIELD_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--app_token', help='app token')
    parser.add_argument('--table_id', help='table id')
    parser.add_argument('--field_id', help='field id')
    parser.add_argument('--field_name', help='field name')
    parser.add_argument('--field_type', type=int, help='field type')
    parser.add_argument('--config_file', default='feishu-config.ini', help='config file path')
    args = parser.parse_args()
    
    # 调用封装的函数，使用命令行参数或默认值
    response_body = UPDATE_FIELD(args.app_token, args.table_id, args.field_id, args.field_name, args.field_type, args.config_file)
    print(json.dumps(response_body, indent=4))

if __name__ == "__main__":
    UPDATE_FIELD_CMD()  # 调用封装的CMD函数
