import configparser
import argparse
from DELETE_FIELDS import DELETE_FIELD
from DELETE_RECORD import DELETE_RECORD
from GET_FIELD_INFO import GET_FIELD_ID
from LIST_RECORDS import LIST_RECORDS

# 默认要删除的字段列表
DEFAULT_FIELDS_TO_DELETE = ["单选", "多选", "群组", "日期", "附件", "人员"]

def DELETE_EMPTY_RECORDS(app_token, table_id):
    page_token = None
    while True:
        # 列出记录
        records_response = LIST_RECORDS(app_token, table_id, page_token, 100)
        records = records_response.get('data', {}).get('items', [])

        # 删除空的记录
        for record in records:
            if not record.get('fields'):
                record_id = record.get('id')
                DELETE_RECORD(app_token, table_id, record_id)
                
        # 如果有下一页，继续处理
        page_token = records_response.get('data', {}).get('page_token')
        if not page_token:
            break

def DELETE_FIELDS_DEFAULT():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('feishu-config.ini', encoding='utf-8')

    # 从命令行获取表格ID，或者使用配置文件中的默认值
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--table', default=config.get('ID', 'table_id'), help='table ID')
    args = parser.parse_args()
    table_id = args.table

    # 获取app_token
    app_token = config.get('TOKEN', 'app_token')

    # 删除默认字段
    for field_name in DEFAULT_FIELDS_TO_DELETE:
        field_id = GET_FIELD_ID(field_name)
        if field_id != "NONE":
            DELETE_FIELD(app_token, table_id, field_id)

    # 删除空的记录
    DELETE_EMPTY_RECORDS(app_token, table_id)

if __name__ == "__main__":
    DELETE_FIELDS_DEFAULT()
