import csv
import configparser
import requests
import json

# 读取配置文件
config = configparser.ConfigParser()
config.read('feishu-config.ini', encoding='utf-8')

# 提取tokens和app_token
user_access_token = config.get('TOKEN', 'user_access_token')
app_token = config.get('TOKEN', 'app_token')

# 提取CSV文件路径
csv_file_path = config.get('FILE_PATH', 'csv_file_path')

def read_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def csv_to_records(csv_data):
    headers = csv_data[0]
    records = []
    for row in csv_data[1:]:
        record = {headers[i]: value for i, value in enumerate(row)}
        records.append({"fields": record})
    return records

def post_records(app_token, table_id, records):
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_create"

    headers = {
        "Authorization": f"Bearer {user_access_token}",
        "Content-Type": "application/json; charset=utf-8"
    }

    data = {"records": records}
    response = requests.post(url, headers=headers, json=data)

    return response.json()

def create_table_records(csv_file_path, app_token, table_id):
    csv_data = read_csv(csv_file_path)
    records = csv_to_records(csv_data)
    response = post_records(app_token, table_id, records)
    return response
