import requests
import configparser
import json
import BUILD_FIELD

def build_request_url(app_token, table_id):
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_create"
    print(f"URL set to: {url}")
    return url

def send_request(url, headers, data):
    response = requests.post(url, headers=headers, json=data)
    print("Request sent. Response received.")
    return response

def check_response_status(response):
    if response.status_code == 200:
        print(f"Successfully created table records. Response status code: {response.status_code}")
    else:
        print(f"Error in creating table records. Response status code: {response.status_code}")
        response.raise_for_status()

def main():
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
    request_body = BUILD_FIELD.BUILD_FIELD(csv_file_path, 'feishu-field.ini')

    # 构建请求URL
    url = build_request_url(app_token, table_id)

    # 发送请求并接收响应
    response = send_request(url, headers, request_body)

    # 检查响应状态
    check_response_status(response)

if __name__ == "__main__":
    main()
