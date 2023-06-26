import argparse
import configparser
from LIST_RECORDS import LIST_RECORDS

# 从给定的响应中获取具有特定字段值的记录的ID
def GET_RECORD_ID(field_value, field_name=None, config_file=None):
    if config_file is None:
        config_file = 'feishu-config.ini'

    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    if field_name is None:
        field_name = config.get('LIST_RECORDS', 'key', fallback=None)

    response = LIST_RECORDS(config_file=config_file)

    for item in response["data"]["items"]:
        if item["fields"].get(field_name) == field_value:
            return item["record_id"]

    return "NONE"


# 解析命令行参数并调用GET_RECORD_ID函数
def GET_RECORD_ID_CMD():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--field', default=None, help='字段名')
    parser.add_argument('--field_name', default=None, help='字段名')
    parser.add_argument('-n', '--name', default=None, help='字段名')
    parser.add_argument('-k', '--key', default=None, help='字段名')
    parser.add_argument('-v', '--value', required=True, help='字段值')
    parser.add_argument('--config_file', default='feishu-config.ini', help='配置文件路径')
    args = parser.parse_args()

    field_name = args.field if args.field is not None else args.field_name if args.field_name is not None else args.name if args.name is not None else args.key

    record_id = GET_RECORD_ID(args.value, field_name, args.config_file)
    print(record_id)


if __name__ == "__main__":
    GET_RECORD_ID_CMD()
