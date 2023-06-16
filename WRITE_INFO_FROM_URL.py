import argparse
import configparser
from GET_INFO_FROM_URL import GET_APPTOKEN_FROM_URL, GET_TABLEID_FROM_URL, GET_VIEWID_FROM_URL

# 这个函数用于将从URL中提取的token写入到配置文件
def WRITE_INFO_FROM_URL(url):
    config = configparser.ConfigParser()  # 创建一个ConfigParser对象
    config.read('feishu-config.ini')  # 读取名为'feishu-config.ini'的配置文件

    # 从URL中提取app_token, table_id, view_id
    app_token = GET_APPTOKEN_FROM_URL(url)
    table_id = GET_TABLEID_FROM_URL(url)
    view_id = GET_VIEWID_FROM_URL(url)

    # 检查是否存在名为'TOKEN'的section，如果不存在则添加
    if 'TOKEN' not in config:
        config.add_section('TOKEN')
    # 在'TOKEN' section下添加app_token
    config['TOKEN']['app_token'] = app_token

    # 检查是否存在名为'ID'的section，如果不存在则添加
    if 'ID' not in config:
        config.add_section('ID')
    # 在'ID' section下添加table_id和view_id
    config['ID']['table_id'] = table_id
    config['ID']['view_id'] = view_id

    # 将新的配置写入到名为'feishu-config.ini'的文件中
    with open('feishu-config.ini', 'w') as configfile:
        config.write(configfile)

def WRITE_INFO_FROM_URL_CMD():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=True, help='用于提取令牌的URL')
    args = parser.parse_args()
    WRITE_INFO_FROM_URL(args.url)

if __name__ == "__main__":
    WRITE_INFO_FROM_URL_CMD()
