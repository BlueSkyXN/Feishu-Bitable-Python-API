import requests
import configparser
import json
from datetime import datetime
import os

def get_config(file, section, key):
    config = configparser.ConfigParser()
    config.read(file)
    return config.get(section, key)

def get_fields(file):
    if not os.path.exists(file):
        return [
            {
                "field_name": "KEY",
                "type": 1
            },
            {
                "field_name": "多行文本",
                "type": 1
            }
        ]
    config = configparser.ConfigParser()
    config.read(file)
    fields = []
    for section in config.sections():
        field = {}
        for key, val in config.items(section):
            field[key] = val
        fields.append(field)
    return fields

def write_fields(file, fields):
    config = configparser.ConfigParser()
    for i, field in enumerate(fields):
        config.add_section(f'Field{i}')
        for key, val in field.items():
            config.set(f'Field{i}', key, val)
    with open(file, 'w') as configfile:
        config.write(configfile)

def get_default_table_name():
    return '新建数据表 ' + datetime.now().strftime('%m%d')

def create_table(user_access_token, app_token, table_name=None, default_view_name='默认的表格视图', fields=None):
    if table_name is None:
        table_name = get_default_table_name()
    if fields is None:
        fields = get_fields('feishu-field.ini')
    headers = {
        'Authorization': f'Bearer {user_access_token}',
        'Content-Type': 'application/json; charset=utf-8'
    }
    data = {
        'table': {
            'name': table_name,
            'default_view_name': default_view_name,
            'fields': fields
        }
    }
    response = requests.post(f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables', headers=headers, data=json.dumps(data))
    return response.json()

# 使用示例
user_access_token = get_config('feishu-config.ini', 'TOKEN', 'user_access_token')
app_token = get_config('feishu-config.ini', 'TOKEN', 'app_token')
fields = [{'field_name': '多行文本', 'type': '1'}]
write_fields('feishu-field.ini', fields)
response = create_table(user_access_token, app_token)
print(response)
