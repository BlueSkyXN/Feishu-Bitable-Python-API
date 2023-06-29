import configparser
import argparse
from LIST_TABLES import LIST_TABLES

# 检索字段
# 此函数用于通过给定的名称获取表的ID
def GET_TABLE_ID(name="数据表", app_token=None, user_access_token=None, page_size=None, page_token=None, config_file=None):
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
    if not record_id:
        record_id = config.get('ID', 'record_id')

    response = LIST_TABLES(app_token, user_access_token, page_size, page_token, config_file)

    # 在返回的所有数据表信息中，寻找名称匹配的数据表
    for item in response["data"]["items"]:
        if item["name"] == name:  # 如果找到了名称匹配的数据表，返回其ID
            return item["table_id"]

    return "NONE"  # 如果没有找到名称匹配的数据表，返回"NONE"

# 此函数用于解析命令行参数并调用 GET_TABLE_ID 函数
def GET_TABLE_ID_CMD():
    parser = argparse.ArgumentParser()  # 创建一个命令行参数解析对象
    group = parser.add_mutually_exclusive_group()  # 创建互斥组

    # 添加一个名为 '-i' 或 '--input' 的参数，此参数默认值为 "数据表"，用来指定要查询的数据表的名称
    group.add_argument('-i', '--input', default="数据表", help='数据表的名字')
    # 添加一个名为 '-n' 或 '--name' 的参数，用来指定要查询的数据表的名称
    group.add_argument('-n', '--name', default="数据表", help='数据表的名字')
    parser.add_argument('--app_token', help='app token')
    parser.add_argument('--user_access_token', help='user access token')
    parser.add_argument('--page_size', type=int, help='page size')
    parser.add_argument('--page_token', help='page token')
    parser.add_argument('--config_file', default="feishu-config.ini", help='config file path')
    args = parser.parse_args()  # 解析命令行参数

    table_name = args.name if args.name else args.input  # 判断优先使用 --name 或 -n 参数

    table_id = GET_TABLE_ID(table_name, args.app_token, args.user_access_token, args.page_size, args.page_token, args.config_file)  # 调用 GET_TABLE_ID 函数获取表的 ID
    print(table_id)  # 打印表的 ID

# 主函数
if __name__ == "__main__":
    GET_TABLE_ID_CMD()  # 调用 GET_TABLE_ID_CMD 函数
