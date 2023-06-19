import argparse
import sys
from urllib.parse import urlparse, parse_qs

# 这个函数用于从URL中提取出参数
def EXTRACT_PARAMETERS(url):
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

    # 返回提取出的app_token, table_id, view_id
    return app_token, table_id, view_id

# 从URL中提取app_token
def GET_APPTOKEN_FROM_URL(url):
    app_token, _, _ = EXTRACT_PARAMETERS(url)
    return app_token

# 从URL中提取table_id
def GET_TABLEID_FROM_URL(url):
    _, table_id, _ = EXTRACT_PARAMETERS(url)
    return table_id

# 从URL中提取view_id
def GET_VIEWID_FROM_URL(url):
    _, _, view_id = EXTRACT_PARAMETERS(url)
    return view_id

# 主函数
if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    # 添加一个名为url的参数，该参数为可选，其作用是提供用于提取参数的URL
    parser.add_argument('-u', '--url', default=None, help='用于提取参数的URL')
    # 添加一个名为input的参数，该参数也为可选，其作用是提供用于提取参数的URL
    parser.add_argument('-i', '--input', default=None, help='用于提取参数的URL')
    # 解析命令行参数
    args = parser.parse_args()

    # 检查'-u/--url'和'-i/--input'参数，优先使用'-u/--url'
    url = args.url if args.url is not None else args.input

    if url is None:  # 如果没有提供URL，打印错误信息并退出
        print("错误：未提供URL，请使用'-u/--url'或'-i/--input'参数提供URL。")
        sys.exit()

    # 从URL中提取app_token, table_id, view_id
    app_token, table_id, view_id = EXTRACT_PARAMETERS(url)

    # 打印提取出的app_token, table_id, view_id
    print(f"app_token: {app_token}")
    print(f"table_id: {table_id}")
    print(f"view_id: {view_id}")