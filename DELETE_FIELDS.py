import requests
import configparser
import argparse

def DELETE_FIELD(app_token=None, table_id=None, field_id=None, config_file=None):
    if config_file is None:
        config_file = 'feishu-config.ini'
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    # 从配置文件获取参数
    access_token = config.get('TOKEN', 'user_access_token')

    # 如果没有提供app_token或table_id，则从配置文件中读取
    if not app_token:
        app_token = config.get('TOKEN', 'app_token')
    if not table_id:
        table_id = config.get('ID', 'table_id')
    if not field_id:
        field_id = config.get('ID', 'field_id')

    # 构建URL
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields/{field_id}"

    # 设置请求头
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # 发送DELETE请求
    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        print(f"字段 {field_id} 已被成功删除")
    else:
        print(f"在删除字段 {field_id} 时发生错误，状态码: {response.status_code}")
        print(f"响应内容: {response.text}")


def DELETE_FIELD_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()

    # 添加参数，此参数用来指定要删除的字段ID
    parser.add_argument('-f', '--field', required=True, help='字段ID')
    parser.add_argument('-t', '--table', required=True, help='表格ID')
    parser.add_argument('-c', '--config', default='feishu-config.ini', help='配置文件路径')

    args = parser.parse_args()

    # 调用DELETE_FIELD函数，删除指定ID的字段
    DELETE_FIELD(args.field, args.table, config_file=args.config)

if __name__ == "__main__":
    DELETE_FIELD_CMD()
