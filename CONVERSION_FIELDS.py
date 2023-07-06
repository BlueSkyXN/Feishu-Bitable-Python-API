import requests
import configparser
import json
import argparse
from LIST_FIELDS import LIST_FIELDS
from UPDATE_FIELD import UPDATE_FIELD
def human_to_machine(app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):

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
    if not field_id:
        field_id = config.get('ID', 'field_id')
    if not field_name:
        field_name = config.get('LIST_FIELDS', 'field_name')

    # 获取当前的字段
    current_fields = LIST_FIELDS(app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None)

    # 遍历当前的字段
    for field in current_fields['data']['items']:
        # 检查当前字段是否在映射中
        if field['field_name'] in fields_map:
            # 如果在，则更新字段名
            UPDATE_FIELD(app_token, table_id, field['field_id'], fields_map[field['field_name']])


def machine_to_human(app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
    
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
    if not field_id:
        field_id = config.get('ID', 'field_id')
    if not field_name:
        field_name = config.get('LIST_FIELDS', 'field_name')

    # 获取当前的字段
    current_fields = LIST_FIELDS(app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None)

    # 反转字典映射
    reversed_fields_map = {v: k for k, v in fields_map.items()}

    # 遍历当前的字段
    for field in current_fields['data']['items']:
        # 检查当前字段是否在反转映射中
        if field['field_name'] in reversed_fields_map:
            # 如果在，则更新字段名
            UPDATE_FIELD(app_token, table_id, field['field_id'], reversed_fields_map[field['field_name']])
