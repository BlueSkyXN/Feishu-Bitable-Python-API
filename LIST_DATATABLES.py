import configparser
import requests
import json

def read_config_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    user_access_token = config.get('TOKEN', 'user_access_token')
    app_token = config.get('TOKEN', 'app_token')
    return user_access_token, app_token

def list_tables(user_access_token, app_token):
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables?page_size=20"
    headers = {
      'Authorization': f'Bearer {user_access_token}'
    }
    response = requests.request("GET", url, headers=headers)
    return response.text

if __name__ == "__main__":
    user_access_token, app_token = read_config_file('feishu-config.ini')
    response_text = list_tables(user_access_token, app_token)

    print(response_text)  # Print the original response

    response_data = json.loads(response_text)

    # Print table name and ID for each table
    for table in response_data['data']['items']:
        print(f"Table Name: {table['name']}, Table ID: {table['table_id']}")
