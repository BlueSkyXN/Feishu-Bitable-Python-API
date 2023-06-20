import requests
import configparser
import argparse
from DELETE_FIELDS import DELETE_FIELD
from GET_FIELD_INFO import GET_FIELD_ID

# 默认要删除的字段列表
DEFAULT_FIELDS_TO_DELETE = ["单选", "多选", "群组", "日期", "附件", "人员"]

def DELETE_FIELDS_DEFAULT():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('feishu-config.ini', encoding='utf-8')

    # 从命令行获取表格ID，或者使用配置文件中的默认值
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--table', default=config.get('ID', 'table_id'), help='table ID')
    args = parser.parse_args()
    table_id = args.table

    # 删除默认字段
    for field_name in DEFAULT_FIELDS_TO_DELETE:
        field_id = GET_FIELD_ID(field_name)
        if field_id != "NONE":
            DELETE_FIELD(field_id, table_id)

if __name__ == "__main__":
    DELETE_FIELDS_DEFAULT()
