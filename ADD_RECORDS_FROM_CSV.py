import requests
import configparser
import json
from BUILD_FIELD import BUILD_FIELD
from CHECK_FIELD_EXIST import CHECK_FIELD_EXIST

def ADD_RECORDS_FROM_CSV(app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, csv_file=None, config_file=None, field_file=None):
    if config_file is None:
        config_file = 'feishu-config.ini'
    if field_file is None:
        field_file = 'feishu-field.ini'

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    if csv_file is None:
        csv_file = 'input.csv'

    # 提取tokens和app_token
    user_access_token = config.get('TOKEN', 'user_access_token')

    # 仅在未提供输入参数时从配置文件中读取
    if app_token is None:
        app_token = config.get('TOKEN', 'app_token')
    if table_id is None:
        table_id = config.get('ID', 'table_id')
    if not csv_file:
        csv_file = config.get('FILE_PATH', 'csv_file_path', fallback='input.csv')
    if view_id is None:
        view_id = config.get('ID', 'view_id')
    if not page_token:
        page_token = config.get('ADD_RECORDS', 'page_token', fallback=None)
    if not page_size:
        page_size = config.get('ADD_RECORDS', 'page_size', fallback=100)


    # 设置请求头
    headers = {
        "Authorization": f"Bearer {user_access_token}",
        "Content-Type": "application/json; charset=utf-8"
    }

    # 调用从BUILD_FIELD.py导入的函数来构建请求体
    record_dict = BUILD_FIELD(csv_file, field_file)

    all_records = record_dict.get('records', [])

    # 检查记录数量，如果超过450则开始分片处理
    batch_size = 450  # 每次发送的记录数量
    for i in range(0, len(all_records), batch_size):
        batch_records = all_records[i:i+batch_size]  # 获取当前批次的记录
        # 对于每个批次，都应该重构请求体
        batch_request_body = {'records': batch_records}

        # 构建请求URL
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_create"
        print(f"URL set to: {url}")

        # 发送请求并接收响应
        response = requests.post(url, headers=headers, json=batch_request_body)
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

                    CHECK_FIELD_EXIST(app_token=app_token, table_id=table_id, view_id=view_id, page_token=page_token, page_size=page_size, csv_file=csv_file, config_file=config_file)

                    print("重试添加记录...")
                    response = requests.post(url, headers=headers, json=batch_request_body)
                    response_json = response.json()
                    
                    if response.status_code != 200 or response_json.get('code') != 0:
                        print(f"重试失败，无法添加记录。错误信息: {response.json()}")
                        response.raise_for_status()
                else:
                    response.raise_for_status()
        else:
            print(f"Error in creating table records. Response status code: {response.status_code}")
            response.raise_for_status()

    ENABLE_ADD_RECORDS = False
    
    if ENABLE_ADD_RECORDS:
        if field_file is None:
           field_file = 'feishu-field.ini'
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
