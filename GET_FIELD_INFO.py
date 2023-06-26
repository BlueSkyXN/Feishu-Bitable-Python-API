import argparse
import configparser
import json
import requests
from LIST_FIELDS import LIST_FIELDS


# 使用字段名称获取字段ID
def GET_FIELD_ID(field_name, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
    response = LIST_FIELDS(app_token, table_id, view_id, page_token, page_size, config_file)
    for item in response["data"]["items"]:
        if item["field_name"] == field_name:
            return item["field_id"]
    return "NONE"


# 使用字段ID获取字段名称
def GET_FIELD_NAME(field_id, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
    response = LIST_FIELDS(app_token, table_id, view_id, page_token, page_size, config_file)
    for item in response["data"]["items"]:
        if item["field_id"] == field_id:
            return item["field_name"]
    return "NONE"


# 获取字段信息
def GET_FIELD_INFO(field_name=None, field_id=None, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
    response = LIST_FIELDS(app_token, table_id, view_id, page_token, page_size, config_file)

    if field_name:
        for item in response["data"]["items"]:
            if item["field_name"] == field_name:
                return item

    elif field_id:
        for item in response["data"]["items"]:
            if item["field_id"] == field_id:
                return item

    return {}


# 命令行参数解析函数
def GET_FIELD_INFO_CMD():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default=None, help='字段名称')
    parser.add_argument('-i', '--id', default=None, help='字段ID')
    parser.add_argument('--app_token', help='app token')
    parser.add_argument('--table_id', help='table ID')
    parser.add_argument('--view_id', help='view ID')
    parser.add_argument('--page_token', help='page token')
    parser.add_argument('--page_size', type=int, help='page size')
    parser.add_argument('--config_file', default="feishu-config.ini", help='配置文件路径')
    args = parser.parse_args()

    field_info = GET_FIELD_INFO(
        field_name=args.name,
        field_id=args.id,
        app_token=args.app_token,
        table_id=args.table_id,
        view_id=args.view_id,
        page_token=args.page_token,
        page_size=args.page_size,
        config_file=args.config_file
    )

    print(json.dumps(field_info, indent=4))


if __name__ == "__main__":
    GET_FIELD_INFO_CMD()
