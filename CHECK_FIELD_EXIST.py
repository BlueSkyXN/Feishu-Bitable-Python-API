import configparser
import pandas as pd
import argparse
from LIST_FIELDS import LIST_FIELDS
from CREATE_FIELD import CREATE_FIELD

def CHECK_FIELD_EXIST(app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, csv_file=None, config_file=None):
    if config_file is None:
        config_file = 'feishu-config.ini'

    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    if not app_token:
        app_token = config.get('TOKEN', 'app_token')
    if not table_id:
        table_id = config.get('ID', 'table_id')
    if not view_id:
        view_id = config.get('ID', 'view_id')
    if not page_token:
        page_token = config.get('LIST_FIELDS', 'page_token', fallback=None)
    if not page_size:
        page_size = config.get('LIST_FIELDS', 'page_size', fallback=100)

    # 获取飞书中的字段列表
    response = LIST_FIELDS(app_token, table_id, view_id, page_token, page_size, config_file)
    feishu_fields = [item['field_name'] for item in response['data']['items']]

    # 从 CSV 文件中读取字段列表
    if csv_file is None:
        csv_file = config.get('FILE_PATH', 'csv_file_path')

    df = pd.read_csv(csv_file)
    fields_to_check = df.columns.tolist()

    # 检查每个需要检查的字段是否在飞书字段列表中，如果不在，就创建新的字段
    for field in fields_to_check:
        if field not in feishu_fields:
            CREATE_FIELD(field)
            print(f"字段 {field} 已成功创建")

if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--app_token', help='app token')
    parser.add_argument('--table_id', help='table ID')
    parser.add_argument('--view_id', help='view ID')
    parser.add_argument('--page_token', help='page token')
    parser.add_argument('--page_size', type=int, help='page size')
    parser.add_argument('--csv_file', help='CSV file path')
    parser.add_argument('--config_file', help='config file')
    args = parser.parse_args()

    # 调用封装的函数，使用命令行参数或默认值
    CHECK_FIELD_EXIST(
        app_token=args.app_token,
        table_id=args.table_id,
        view_id=args.view_id,
        page_token=args.page_token,
        page_size=args.page_size,
        csv_file=args.csv_file,
        config_file=args.config_file
    )

