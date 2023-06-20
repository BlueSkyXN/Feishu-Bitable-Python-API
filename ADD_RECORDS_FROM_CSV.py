import requests
import configparser
import json
import BUILD_FIELD
from CHECK_FIELD_EXIST import CHECK_FIELD_EXIST

def ADD_RECORDS_FROM_CSV():
        # 读取配置文件
    config = configparser.ConfigParser()
    config.read('feishu-config.ini', encoding='utf-8')

    # 提取tokens和app_token
    user_access_token = config.get('TOKEN', 'user_access_token')
    app_token = config.get('TOKEN', 'app_token')
    table_id = config.get('ID', 'table_id')
    csv_file_path = config.get('FILE_PATH', 'csv_file_path')

    # 设置请求头
    headers = {
        "Authorization": f"Bearer {user_access_token}",
        "Content-Type": "application/json; charset=utf-8"
    }

    # 调用从BUILD_FIELD.py导入的函数来构建请求体
    record_dict = BUILD_FIELD.BUILD_FIELD(csv_file_path, 'feishu-field.ini')
    all_records = record_dict.get('records', [])

    # 检查记录数量，如果超过450则开始分片处理
    batch_size = 450  # 每次发送的记录数量
    for i in range(0, len(all_records), batch_size):
        batch_records = all_records[i:i+batch_size]  # 获取当前批次的记录
        record_dict['records'] = batch_records

        # 构建请求URL
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_create"
        print(f"URL set to: {url}")

        # 发送请求并接收响应
        response = requests.post(url, headers=headers, json=record_dict)
        print("Request sent. Response received.")

        # 检查响应状态
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get('code') == 0:
                print(f"Successfully created table records. Response status code: {response.status_code}, Response code: {response_json.get('code')}")
            else:
                print(f"Error in creating table records. Response status code: {response.status_code}, Response code: {response_json.get('code')}")
                # 如果响应中包含 "FieldNameNotFound" 错误，尝试修复并重试
                if response_json.get("code") == 1254045:
                    print("检测到FieldNameNotFound错误，尝试创建不存在的字段...")
                    CHECK_FIELD_EXIST()

                    print("重试添加记录...")
                    response = requests.post(url, headers=headers, json=record_dict)
                    response_json = response.json()
                    
                    if response.status_code != 200 or response_json.get('code') != 0:
                        print(f"重试失败，无法添加记录。错误信息: {response.json()}")
                        response.raise_for_status()
                else:
                    response.raise_for_status()
        else:
            print(f"Error in creating table records. Response status code: {response.status_code}")
            response.raise_for_status()

    # 我假设你只希望保存最后一批次的请求体和响应体
    ENABLE_ADD_RECORDS = False
    
    if ENABLE_ADD_RECORDS:
        # 更新field配置文件
        field_config = configparser.ConfigParser()
        field_config.read('feishu-field.ini', encoding='utf-8')
        if "ADD_RECORDS_FROM_CSV" not in field_config.sections():
            field_config.add_section("ADD_RECORDS_FROM_CSV")
        field_config.set("ADD_RECORDS_FROM_CSV", "request_body", json.dumps({"records": batch_records}))
        field_config.set("ADD_RECORDS_FROM_CSV", "response_body", response.text)
        with open('feishu-field.ini', 'w', encoding='utf-8') as field_configfile:
            field_config.write(field_configfile)
            print("Request body and response body saved to feishu-field.ini.")

if __name__ == "__main__":
    ADD_RECORDS_FROM_CSV()
