import argparse
import configparser
from GET_INFO_FROM_URL import GET_APPTOKEN_FROM_URL, GET_TABLEID_FROM_URL, GET_VIEWID_FROM_URL

def WRITE_INFO_FROM_URL(url):
    config = configparser.ConfigParser()
    config.read('feishu-config.ini', encoding='utf-8')

    try:
        app_token = GET_APPTOKEN_FROM_URL(url)
        table_id = GET_TABLEID_FROM_URL(url)
        view_id = GET_VIEWID_FROM_URL(url)

        if not app_token:
            app_token = ''
        if not table_id:
            table_id = ''
        if not view_id:
            view_id = ''
    except Exception:
        return None

    if 'TOKEN' not in config:
        config.add_section('TOKEN')
    config['TOKEN']['app_token'] = app_token

    if 'ID' not in config:
        config.add_section('ID')
    config['ID']['table_id'] = table_id
    config['ID']['view_id'] = view_id

    try:
        with open('feishu-config.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)
    except Exception:
        return None

    return app_token, table_id, view_id


def WRITE_INFO_FROM_URL_CMD():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', default=None, help='用于提取令牌的URL')
    parser.add_argument('-i', '--input', default=None, help='用于提取令牌的URL')
    args = parser.parse_args()

    url = args.url if args.url is not None else args.input

    if url is None:
        print("错误：未提供URL，请使用'-u/--url'或'-i/--input'参数提供URL。")
        return

    result = WRITE_INFO_FROM_URL(url)

    if result is None:
        print("发生错误，请检查您的输入URL并再试一次。")
    else:
        app_token, table_id, view_id = result
        print(f"app_token: {app_token}")
        print(f"table_id: {table_id}")
        print(f"view_id: {view_id}")
        print("成功写入 'feishu-config.ini' 文件")


if __name__ == "__main__":
    WRITE_INFO_FROM_URL_CMD()
