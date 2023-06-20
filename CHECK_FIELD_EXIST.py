import configparser
import pandas as pd
import argparse
from LIST_FIELDS import LIST_FIELDS
from CREATE_FIELD import CREATE_FIELD

def CHECK_FIELD_EXIST():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('feishu-config.ini', encoding='utf-8')

    # 获取飞书中的字段列表
    response = LIST_FIELDS()
    feishu_fields = [item['field_name'] for item in response['data']['items']]

    # 从 CSV 文件中读取字段列表
    csv_file_path = config.get('FILE_PATH', 'csv_file_path')
    df = pd.read_csv(csv_file_path)
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
    args = parser.parse_args()

    # 调用封装的函数，使用命令行参数或默认值
    CHECK_FIELD_EXIST()
