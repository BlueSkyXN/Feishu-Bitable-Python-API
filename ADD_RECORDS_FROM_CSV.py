import requests
import configparser
import json
import BUILD_FIELD

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
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_create"
    print(f"URL set to: {url}")

    # 发送请求并接收响应
    response = requests.post(url, headers=headers, json=request_body)
    print("Request sent. Response received.")

    # 检查响应状态
    if response.status_code == 200:
        print(f"Successfully created table records. Response status code: {response.status_code}")
    else:
        print(f"Error in creating table records. Response status code: {response.status_code}")
        response.raise_for_status()

    # 更新field配置文件
    field_config = configparser.ConfigParser()
    field_config.read('feishu-field.ini', encoding='utf-8')
    if "REQUEST_RESPONSE" not in field_config.sections():
        field_config.add_section("REQUEST_RESPONSE")
    field_config.set("REQUEST_RESPONSE", "request_body", json.dumps(request_body))
    field_config.set("REQUEST_RESPONSE", "response_body", response.text)
    with open('feishu-field.ini', 'w', encoding='utf-8') as field_configfile:
        field_config.write(field_configfile)
        print("Request body and response body saved to feishu-field.ini.")

if __name__ == "__main__":
    main()
