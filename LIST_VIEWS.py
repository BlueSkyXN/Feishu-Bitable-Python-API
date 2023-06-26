import requests
import configparser
import json
import argparse


# 列出视图
# 此函数用于获取数据表的所有视图，接收五个可选参数
def LIST_VIEWS(app_token=None, user_access_token=None, page_size=None, page_token=None, table_id=None, config_file=None):
    if config_file is None:
        config_file = "feishu-config.ini"

    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    if not app_token:
        app_token = config.get('TOKEN', 'app_token')  # 从配置文件读取 app_token，用于认证请求
    if not user_access_token:
        user_access_token = config.get('TOKEN', 'user_access_token')  # 从配置文件读取 user_access_token，用于认证请求
    if not page_size:
        page_size = config.get('LIST_VIEWS', 'page_size', fallback=100)  # 从配置文件读取 page_size，默认为 100
    if not page_token:
        page_token = config.get('LIST_VIEWS', 'page_token', fallback=None)  # 从配置文件读取 page_token，默认为 None
    if not table_id:
        table_id = config.get('ID', 'table_id')  # 从配置文件读取 table_id，用于构建请求 URL

    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/views"  # 构建请求 URL
    headers = {
        'Authorization': f'Bearer {user_access_token}',  # 设置请求头中的 Authorization，值为 Bearer access_token
        'Content-Type': 'application/json; charset=utf-8'
    }

    params = {'page_size': page_size}  # 设置请求参数中的 page_size，控制每页的视图数量
    if page_token:
        params['page_token'] = page_token  # 如果存在 page_token，将其添加到请求参数中，用于分页获取视图列表

    response = requests.get(url, headers=headers, params=params)  # 发起 GET 请求获取视图列表
    return response.json()  # 返回响应体的 JSON 数据


# 列出视图命令行调用函数
def LIST_VIEWS_CMD():
    parser = argparse.ArgumentParser()  # 创建命令行参数解析器
    parser.add_argument('--app_token', help='应用的 token')  # 添加命令行参数 app_token，用于传递应用的 token
    parser.add_argument('--user_access_token', help='用户的 access token')  # 添加命令行参数 user_access_token，用于传递用户的 access token
    parser.add_argument('--page_size', type=int, help='每页的大小')  # 添加命令行参数 page_size，用于传递每页的大小
    parser.add_argument('--page_token', help='分页标记')  # 添加命令行参数 page_token，用于传递分页标记
    parser.add_argument('--table_id', help='数据表的 ID')  # 添加命令行参数 table_id，用于传递数据表的 ID
    parser.add_argument('--config_file', default="feishu-config.ini", help='配置文件路径')  # 添加命令行参数 config_file，用于传递配置文件的路径，默认为 feishu-config.ini
    args = parser.parse_args()  # 解析命令行参数

    response_body = LIST_VIEWS(args.app_token, args.user_access_token, args.page_size, args.page_token, args.table_id, args.config_file)  # 调用 LIST_VIEWS 函数获取视图列表
    print(json.dumps(response_body, indent=4))  # 打印响应体的 JSON 数据


if __name__ == "__main__":
    LIST_VIEWS_CMD()
