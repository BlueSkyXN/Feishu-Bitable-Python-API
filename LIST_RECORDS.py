import requests
import configparser
import json
import argparse

# 列出记录
def LIST_RECORDS(app_token=None, table_id=None, page_token=None, page_size=None, config_file=None):
    if config_file is None:
        config_file = 'feishu-config.ini'

    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    if not app_token:
        app_token = config.get('TOKEN', 'app_token')
    if not table_id:
        table_id = config.get('ID', 'table_id')
    if not page_token:
        page_token = config.get('LIST_RECORDS', 'page_token', fallback=None)
    if not page_size:
        page_size = config.get('LIST_RECORDS', 'page_size', fallback=100)

    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records"
    headers = {
        'Authorization': 'Bearer ' + config.get('TOKEN', 'user_access_token'),
        'Content-Type': 'application/json; charset=utf-8',
    }

    params = {'page_size': page_size}
    if page_token:
        params['page_token'] = page_token

    response = requests.get(url, headers=headers, params=params)
    return response.json()


# 列出记录命令行调用函数
def LIST_RECORDS_CMD():
    parser = argparse.ArgumentParser()
    parser.add_argument('--app_token', help='app token')
    parser.add_argument('--table_id', help='table ID')
    parser.add_argument('--page_token', help='page token')
    parser.add_argument('--page_size', type=int, help='page size')
    parser.add_argument('--config_file', default='feishu-config.ini', help='config file path')
    args = parser.parse_args()

    response_body = LIST_RECORDS(args.app_token, args.table_id, args.page_token, args.page_size, args.config_file)
    print(json.dumps(response_body, indent=4))


if __name__ == "__main__":
    LIST_RECORDS_CMD()
