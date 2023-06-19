import argparse
import configparser
from LIST_RECORDS import LIST_RECORDS

# 从给定的响应中获取具有特定字段值的记录的ID
def GET_RECORD_ID(field_value, field_name=None):
    config_file='feishu-config.ini'  # 配置文件名
    # 读取配置文件获取字段名
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    # 如果没有提供字段名，从配置文件获取默认字段名
    if field_name is None:
        field_name = config.get('LIST_RECORDS', 'key', fallback=None)

    # 调用LIST_RECORDS函数获取所有记录的信息
    response = LIST_RECORDS()

    # 在返回的所有记录信息中，寻找字段值匹配的记录
    for item in response["data"]["items"]:
        if item["fields"].get(field_name) == field_value:
            return item["record_id"]

    return "NONE"  # 如果没有找到字段值匹配的记录，返回"NONE"



# 此函数用于解析命令行参数并调用GET_RECORD_ID函数
def GET_RECORD_ID_CMD_DEST():
    parser = argparse.ArgumentParser()  # 创建一个命令行参数解析对象

    # 添加对字段名的支持，注意字段名是可选的，有多个别名
    # 优先级：'-f' > '--field' > '--field_name' > '-n' > '--name' > '-k' > '--key'
    parser.add_argument('-f', dest='field_name', default=None, help='字段名')
    parser.add_argument('--field', dest='field_name', default=None, help='字段名')
    parser.add_argument('--field_name', dest='field_name', default=None, help='字段名')
    parser.add_argument('-n', dest='field_name', default=None, help='字段名')
    parser.add_argument('--name', dest='field_name', default=None, help='字段名')
    parser.add_argument('-k', dest='field_name', default=None, help='字段名')
    parser.add_argument('--key', dest='field_name', default=None, help='字段名')

    # 添加对字段值的支持，支持-v或--value参数输入
    parser.add_argument('-v', '--value', required=True, help='字段值')

    args = parser.parse_args()  # 解析命令行参数

    # 调用GET_RECORD_ID函数获取记录的ID
    record_id = GET_RECORD_ID(args.value, args.field_name)
    print(record_id)  # 打印记录的ID

def GET_RECORD_ID_CMD():
    parser = argparse.ArgumentParser()  # 创建一个命令行参数解析对象

    # 添加对字段名的支持，每个别名作为一个单独的参数
    parser.add_argument('-f', '--field', default=None, help='字段名')
    parser.add_argument('--field_name', default=None, help='字段名')
    parser.add_argument('-n', '--name', default=None, help='字段名')
    parser.add_argument('-k', '--key', default=None, help='字段名')

    # 添加对字段值的支持，支持-v或--value参数输入
    parser.add_argument('-v', '--value', required=True, help='字段值')

    args = parser.parse_args()  # 解析命令行参数

    # 按照优先级顺序检查字段名参数的值，优先级顺序是 '-f/--field' > '--field_name' > '-n/--name' > '-k/--key'
    field_name = args.field if args.field is not None else args.field_name if args.field_name is not None else args.name if args.name is not None else args.key

    # 调用GET_RECORD_ID函数获取记录的ID
    record_id = GET_RECORD_ID(args.value, field_name)
    print(record_id)  # 打印记录的ID


# 主函数
if __name__ == "__main__":
    GET_RECORD_ID_CMD()  # 调用GET_RECORD_ID_CMD函数
