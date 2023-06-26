import requests
import configparser
import json
import argparse

def LIST_TABLES(app_token=None, user_access_token=None, page_size=None, page_token=None, config_file=None):
    # 如果未指定配置文件，则使用默认的配置文件名
    if config_file is None:
        config_file = "feishu-config.ini"

    # 创建配置解析器对象
    config = configparser.ConfigParser()
    # 读取配置文件
    config.read(config_file, encoding='utf-8')

    # 如果未提供 app_token，则从配置文件中获取
    if not app_token:
        app_token = config.get('TOKEN', 'app_token')
    # 如果未提供 user_access_token，则从配置文件中获取
    if not user_access_token:
        user_access_token = config.get('TOKEN', 'user_access_token')
    # 如果未提供 page_token，则从配置文件中获取，如果配置文件中没有设置则默认为 None
    if not page_token:
        page_token = config.get('LIST_TABLES', 'page_token', fallback=None)
    # 如果未提供 page_size，则从配置文件中获取，如果配置文件中没有设置则默认为 100
    if not page_size:
        page_size = config.get('LIST_TABLES', 'page_size', fallback=100)

    # 构建请求的 URL
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables"
    # 设置请求的头部信息
    headers = {
        'Authorization': f'Bearer {user_access_token}',
        'Content-Type': 'application/json; charset=utf-8'
    }

    # 构建请求的参数
    params = {'page_size': page_size}
    if page_token:
        params['page_token'] = page_token

    # 发送 GET 请求
    response = requests.get(url, headers=headers, params=params)
    # 返回响应的 JSON 数据
    return response.json()

def LIST_TABLES_CMD():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser()
    # 添加命令行参数
    parser.add_argument('--app_token', help='app token')
    parser.add_argument('--user_access_token', help='user access token')
    parser.add_argument('--page_size', type=int, help='page size')
    parser.add_argument('--page_token', help='page token')
    parser.add_argument('--config_file', default="feishu-config.ini", help='config file path')
    # 解析命令行参数
    args = parser.parse_args()

    # 调用 LIST_TABLES 函数获取表格列表的响应数据
    response_body = LIST_TABLES(args.app_token, args.user_access_token, args.page_size, args.page_token, args.config_file)
    # 将响应数据以缩进格式打印输出
    print(json.dumps(response_body, indent=4))

if __name__ == "__main__":
    # 执行 LIST_TABLES_CMD 函数
    LIST_TABLES_CMD()
