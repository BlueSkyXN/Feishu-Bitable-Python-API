import requests
import json
import configparser
from datetime import datetime
import os
import argparse

def CREATE_TABLE(app_token=None, table_name=None, default_view_name=None, fields=None, config_file=None, fields_file=None):
    if config_file is None:
        config_file = 'feishu-config.ini'

    if fields_file is None:
        fields_file = 'feishu-field.ini'

    if default_view_name is None:
        default_view_name = '默认的表格视图'

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    user_access_token = config.get('TOKEN', 'user_access_token')
    
    # 仅在未提供输入参数时从配置文件中读取
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

def CREATE_TABLE_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()

    # 添加参数，此参数用来指定应用的访问令牌
    parser.add_argument('--app_token', help='应用的访问令牌')

    # 添加参数，此参数用来指定表格的名称
    parser.add_argument('--table_name', help='表格的名称')

    # 添加参数，此参数用来指定默认的表格视图名称
    parser.add_argument('--default_view_name', help='默认的表格视图名称')

    # 添加参数，此参数用来指定字段配置文件的路径
    parser.add_argument('--fields_file', help='字段配置文件的路径')

    args = parser.parse_args()

    # 调用 CREATE_TABLE 函数，创建数据表
    response = CREATE_TABLE(
        app_token=args.app_token,
        table_name=args.table_name,
        default_view_name=args.default_view_name,
        fields_file=args.fields_file
    )

    # 打印响应结果
    print(response)


# 主函数
if __name__ == "__main__":
    CREATE_TABLE_CMD()
