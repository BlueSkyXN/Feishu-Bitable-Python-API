import requests
import json
import configparser
import argparse

def REFRESH_USER_ACCESS_TOKEN(token, refresh_token):
    url = 'https://open.feishu.cn/open-apis/authen/v1/refresh_access_token'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json; charset=utf-8'
    }
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get('code') == 0:
            user_access_token = response_data.get('data').get('access_token')
            return user_access_token
        else:
            return None
    else:
        return None

def REFRESH_USER_ACCESS_TOKEN_CMD():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", required=True, help="App Access Token")
    parser.add_argument("-r", "--refresh", required=True, help="Refresh Token")
    args = parser.parse_args()
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    if not config.has_option('TOKEN', 'user_access_token'):
        config.set('TOKEN', 'user_access_token', '')
        with open('config.ini', 'w') as f:
            config.write(f)

    if not config.has_option('TOKEN', 'refresh_token'):
        config.set('TOKEN', 'refresh_token', config.get('TOKEN', 'user_access_token'))
        with open('config.ini', 'w') as f:
            config.write(f)

    user_access_token = REFRESH_USER_ACCESS_TOKEN(args.token, args.refresh)
    if user_access_token:
        config.set('TOKEN', 'user_access_token', user_access_token)
        with open('config.ini', 'w') as f:
            config.write(f)
    else:
        REFRESH_USER_ACCESS_TOKEN(args.token, config.get('TOKEN', 'user_access_token'))

if __name__ == "__main__":
    REFRESH_USER_ACCESS_TOKEN_CMD()
