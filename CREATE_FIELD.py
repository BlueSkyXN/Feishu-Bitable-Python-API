import requests
import json
import configparser
import argparse

# 函数用于创建字段
def CREATE_FIELD(field_name, field_type=1):
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('feishu-config.ini', encoding='utf-8')

    # 从配置文件获取参数
    app_token = config.get('TOKEN', 'app_token')
    table_id = config.get('ID', 'table_id')
    access_token = config.get('TOKEN', 'user_access_token')

    # API endpoint
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields"

    # 请求头
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=utf-8"
    }

    # 创建字段
    payload = {
        "field_name": field_name,
        "type": field_type,
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f"Creating field {field_name}...")
    print(response.json())


# 函数用于从命令行获取参数并创建字段
def CREATE_FIELD_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()

    # 添加第一个参数，此参数用来指定要创建的字段名
    parser.add_argument('-f', '--field', required=True, help='字段名')

    # 添加第二个参数，此参数用来指定要创建的字段类型，默认为1（多行文本）
    parser.add_argument('-t', '--type', type=int, default=1, help='字段类型')

    args = parser.parse_args()

    # 调用CREATE_FIELD函数，创建新字段
    CREATE_FIELD(args.field, args.type)


# 主函数
if __name__ == "__main__":
    CREATE_FIELD_CMD()
