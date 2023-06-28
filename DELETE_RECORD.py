import requests
import configparser
import argparse

def DELETE_RECORD(app_token=None, table_id=None, record_id=None, config_file=None):
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
    if not record_id:
        record_id = config.get('ID', 'record_id')

    # 提取token
    user_access_token = config.get('TOKEN', 'user_access_token')

    # 构建请求URL和请求头
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}"
    headers = {
        'Authorization': f'Bearer {user_access_token}',
        'Content-Type': 'application/json; charset=utf-8',
    }

    # 发起请求
    response = requests.delete(url, headers=headers)

    # 检查响应状态
    if response.status_code == 200:
        print(f'Successfully deleted record: {record_id}')
    else:
        print(f'Failed to delete record: {record_id}. Status code: {response.status_code}')

def DELETE_RECORD_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--app_token', default=None, help='app token')
    parser.add_argument('-t', '--table_id', default=None, help='table ID')
    parser.add_argument('-r', '--record_id', default=None, help='record ID')
    parser.add_argument('-c', '--config', default='feishu-config.ini', help='配置文件路径')
    args = parser.parse_args()

    # 调用DELETE_RECORD函数
    DELETE_RECORD(args.app_token, args.table_id, args.record_id, config_file=args.config)


if __name__ == "__main__":
    DELETE_RECORD_CMD()
