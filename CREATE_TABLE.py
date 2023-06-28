import requests
import json
import configparser
from datetime import datetime
import os

def CREATE_TABLE(user_access_token=None, app_token=None, table_name=None, default_view_name='默认的表格视图', fields=None, config_file='feishu-config.ini', fields_file='feishu-field.ini'):
    if config_file is None:
        config_file = 'feishu-config.ini'

    if fields_file is None:
        fields_file = 'feishu-field.ini'

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    # 仅在未提供输入参数时从配置文件中读取
    if user_access_token is None:
        user_access_token = config.get('TOKEN', 'user_access_token')
    if app_token is None:
        app_token = config.get('TOKEN', 'app_token')

    # 设置默认表格名称
    if table_name is None:
        table_name = '新建数据表 ' + datetime.now().strftime('%m%d')

    # 获取字段信息
    if fields is None:
        if not os.path.exists(fields_file):
            fields = [
                {
                    "field_name": "KEY",
                    "type": 1
                },
                {
                    "field_name": "多行文本",
                    "type": 1
                }
            ]
        else:
            fields = []
            fields_config = configparser.ConfigParser()
            fields_config.read(fields_file)
            for section in fields_config.sections():
                field = {}
                for key, val in fields_config.items(section):
                    field[key] = val
                fields.append(field)

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
