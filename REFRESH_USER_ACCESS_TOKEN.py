import argparse
import configparser
import requests
import json
import codecs

def REFRESH_USER_ACCESS_TOKEN(token=None, refresh=None):
    config = configparser.ConfigParser()
    with codecs.open('feishu-config.ini', 'r', encoding='utf-8') as f:
        config.read_file(f)

    if not config.has_section('TOKEN'):
        config.add_section('TOKEN')
        
    if 'app_token' not in config['TOKEN']:
        config.set('TOKEN', 'app_token', '')
        
    if 'user_access_token' not in config['TOKEN']:
        config.set('TOKEN', 'user_access_token', '')

    with codecs.open('feishu-config.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)

    token = config.get('TOKEN', 'app_token') if token is None else token
    refresh = config.get('TOKEN', 'user_access_token') if refresh is None else refresh

    url = "https://open.feishu.cn/open-apis/authen/v1/refresh_access_token"
    headers = {"Content-Type": "application/json"}

    payload = {
        "app_access_token": token,
        "grant_type": "refresh_token",
        "refresh_token": refresh
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()
    if data["code"] != 0:
        print(f"Error: {data['msg']}")
        return None

    config.set('TOKEN', 'user_access_token', data['data']['user_access_token'])
    with codecs.open('feishu-config.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)

    return data['data']['user_access_token']

def REFRESH_USER_ACCESS_TOKEN_CMD():
    parser = argparse.ArgumentParser(description='Refresh user access token.')
    parser.add_argument('-t', '--token', type=str, help='The token.')
    parser.add_argument('-r', '--refresh', type=str, help='The refresh token.')
    args = parser.parse_args()

    user_access_token = REFRESH_USER_ACCESS_TOKEN(args.token, args.refresh)
    print(f'User Access Token: {user_access_token}')

if __name__ == '__main__':
    REFRESH_USER_ACCESS_TOKEN_CMD()
