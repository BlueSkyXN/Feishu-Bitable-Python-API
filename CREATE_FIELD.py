import requests
import json
import configparser
import argparse

def CREATE_FIELD(field_name, field_type=None, app_token=None, table_id=None, config_file=None):
    
    if config_file is None:
        config_file = 'feishu-config.ini'

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    # 仅在未提供输入参数时从配置文件中读取
    if app_token is None:
        app_token = config.get('TOKEN', 'app_token')
    if table_id is None:
        table_id = config.get('ID', 'table_id')

    # 从配置文件获取参数
    user_access_token = config.get('TOKEN', 'user_access_token')

    # 设置字段类型的默认值为1
    if field_type is None:
        field_type = 1

    # API endpoint
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields"

    # 请求头
    headers = {
        "Authorization": f"Bearer {user_access_token}",
        "Content-Type": "application/json; charset=utf-8"
    }

    # 创建字段
    payload = {
        "field_name": field_name,
        "type": field_type
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f"Creating field {field_name}...")
    print(response.json())

def CREATE_FIELD_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()

    # 添加参数，此参数用来指定要创建的字段名
    parser.add_argument('-f', '--field', required=True, help='字段名')

    # 添加参数，此参数用来指定字段类型，默认为1
    parser.add_argument('--field_type', type=int, default=1, help='字段类型')

    # 添加参数，此参数用来指定多维表格的唯一标识符 app_token
    parser.add_argument('--app_token', help='多维表格的唯一标识符 app_token')

    # 添加参数，此参数用来指定多维表格数据表的唯一标识符 table_id
    parser.add_argument('--table_id', help='多维表格数据表的唯一标识符 table_id')

    # 添加参数，此参数用来指定配置文件路径，默认为'feishu-config.ini'
    parser.add_argument('--config_file', default='feishu-config.ini', help='配置文件路径')

    args = parser.parse_args()

    # 调用CREATE_FIELD函数，创建新字段
    CREATE_FIELD(args.field, args.field_type, args.app_token, args.table_id, args.config_file)

# 主函数
if __name__ == "__main__":
    CREATE_FIELD_CMD()
