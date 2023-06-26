import argparse
import sys
import json
from urllib.parse import urlparse, parse_qs

def GET_INFO_FROM_URL(url):
    # 解析URL
    parsed_url = urlparse(url)
    # 提取URL的参数部分
    params = parse_qs(parsed_url.query)

    # 从URL的路径中获取app_token，路径的最后一部分即为app_token
    app_token = parsed_url.path.split('/')[-1]
    # 从参数中获取table_id，如果没有table参数则返回None
    table_id = params.get('table', [None])[0]
    # 从参数中获取view_id，如果没有view参数则返回None
    view_id = params.get('view', [None])[0]

    # 构建包含提取的信息的字典
    info = {"app_token": app_token, "table_id": table_id, "view_id": view_id}

    # 返回提取出的信息字典
    return info

def GET_INFO_FROM_URL_JSON(url):
    info = GET_INFO_FROM_URL(url)
    return json.dumps(info)

def GET_APPTOKEN_FROM_URL(url):
    info = GET_INFO_FROM_URL(url)
    return info["app_token"]

def GET_TABLEID_FROM_URL(url):
    info = GET_INFO_FROM_URL(url)
    return info["table_id"]

def GET_VIEWID_FROM_URL(url):
    info = GET_INFO_FROM_URL(url)
    return info["view_id"]

if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', default=None, help='用于提取参数的URL')
    parser.add_argument('-i', '--input', default=None, help='用于提取参数的URL')
    args = parser.parse_args()

    url = args.url if args.url is not None else args.input

    if url is None:
        print("错误：未提供URL，请使用'-u/--url'或'-i/--input'参数提供URL。")
        sys.exit()

    # 调用GET_INFO_FROM_URL函数获取提取的信息
    info = GET_INFO_FROM_URL(url)

    # 将字典转换为JSON格式字符串
    json_info = json.dumps(info)

    # 打印JSON格式字符串
    print(json_info)

    # 调用其他函数提取特定值并打印
    app_token = GET_APPTOKEN_FROM_URL(url)
    table_id = GET_TABLEID_FROM_URL(url)
    view_id = GET_VIEWID_FROM_URL(url)
    print(f"app_token: {app_token}")
    print(f"table_id: {table_id}")
    print(f"view_id: {view_id}")
