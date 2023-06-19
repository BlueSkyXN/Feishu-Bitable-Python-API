import requests
import configparser
import json
import argparse

# 列出字段
def LIST_FIELDS(app_token=None, table_id=None, view_id=None, text_field_as_array=None, page_token=None, page_size=None):
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('feishu-config.ini')

    # 如果参数为空，则使用配置文件中的默认值
    if not app_token:
        app_token = config.get('TOKEN', 'app_token')
    if not table_id:
        table_id = config.get('ID', 'table_id')
    if not view_id:
        view_id = config.get('ID', 'view_id', fallback=None)
    if not text_field_as_array:
        text_field_as_array = config.get('LIST_FIELDS', 'text_field_as_array', fallback=None)
    if not page_token:
        page_token = config.get('LIST_FIELDS', 'page_token', fallback=None)
    if not page_size:
        page_size = config.get('LIST_FIELDS', 'page_size', fallback=100)

    # 构造请求URL和头部
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields"
    headers = {
        'Authorization': 'Bearer ' + config.get('TOKEN', 'user_access_token'),
        'Content-Type': 'application/json; charset=utf-8',
    }

    # 添加请求参数
    params = {'page_size': page_size}
    if view_id:
        params['view_id'] = view_id
    if text_field_as_array:
        params['text_field_as_array'] = text_field_as_array
    if page_token:
        params['page_token'] = page_token

    # 发起请求，并返回响应体的json形式
    response = requests.get(url, headers=headers, params=params)
    return response.json()


if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--app_token', help='app token')
    parser.add_argument('--table_id', help='table ID')
    parser.add_argument('--view_id', help='view ID')
    parser.add_argument('--text_field_as_array', help='text field as array')
    parser.add_argument('--page_token', help='page token')
    parser.add_argument('--page_size', type=int, help='page size')
    args = parser.parse_args()

    # 调用封装的函数，使用命令行参数或默认值
    response_body = LIST_FIELDS(args.app_token, args.table_id, args.view_id, args.text_field_as_array, args.page_token, args.page_size)
    print(json.dumps(response_body, indent=4))
