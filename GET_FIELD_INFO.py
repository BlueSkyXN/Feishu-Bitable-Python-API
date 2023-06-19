import argparse
import configparser
from LIST_FIELDS import LIST_FIELDS

# 使用字段名称获取字段ID
def GET_FIELD_ID(field_name):
    response = LIST_FIELDS()
    for item in response["data"]["items"]:
        if item["field_name"] == field_name:
            return item["field_id"]
    return "NONE"

# 使用字段ID获取字段名称
def GET_FIELD_NAME(field_id):
    response = LIST_FIELDS()
    for item in response["data"]["items"]:
        if item["field_id"] == field_id:
            return item["field_name"]
    return "NONE"

def GET_FIELD_INFO(field_name=None, field_id=None):
    response = LIST_FIELDS()  

    # 优先使用字段名查找
    if field_name:
        for item in response["data"]["items"]:
            if item["field_name"] == field_name:
                return item["field_id"]

    # 使用字段ID查找
    elif field_id:
        for item in response["data"]["items"]:
            if item["field_id"] == field_id:
                return item["field_name"]

    return "NONE"


# 命令行参数解析函数
def GET_FIELD_INFO_CMD():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default=None, help='字段名称')
    parser.add_argument('-i', '--id', default=None, help='字段ID')
    args = parser.parse_args()

    # 如果没有输入任何参数，使用配置文件中的默认值
    if not args.name and not args.id:
        config = configparser.ConfigParser()
        config.read('feishu-config.ini')
        args.name = config.get('LIST_FIELDS', 'field_name', fallback=None)
        args.id = config.get('ID', 'field_id', fallback=None)

    if args.name:
        result = GET_FIELD_ID(args.name)
        print(result)

        # 将找到的字段ID写入配置文件
        config = configparser.ConfigParser()
        config.read('feishu-config.ini')
        config.set('ID', 'field_id', result)
        with open('feishu-config.ini', 'w') as configfile:
            config.write(configfile)

    elif args.id:
        result = GET_FIELD_NAME(args.id)
        print(result)

if __name__ == "__main__":
    GET_FIELD_INFO_CMD()
