import requests
import json
import configparser
from datetime import datetime
import os
import argparse

def CREATE_TABLE(access_token=None, table_name=None, config_file=None, folder_token=None):
    if config_file is None:
        config_file = 'feishu-config.ini'

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    user_access_token = config.get('TOKEN', 'user_access_token')
    
    # 仅在未提供输入参数时从配置文件中读取. Access Token优先从App Access Token读取.
    if access_token is None:
       access_token = config.get('TOKEN', 'app_access_token') or config.get('TOKEN', 'user_access_token')

    # 设置默认表格名称
    if table_name is None:
        table_name = '新建数据表 ' + datetime.now().strftime('%m%d')

    # 设置表格上传目标文件夹:
    if folder_token is None:
        folder_token = config.get('TABLE_CONFIG', 'default_folder')

    headers = {
        'Authorization': f'Bearer {user_access_token}',
        'Content-Type': 'application/json; charset=utf-8'
    }
       
    data = {
        'title': table_name,
    }; 
    if folder_token != None: 
        data.update({'folder_token': folder_token})
 
    response = requests.post(f'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets', headers=headers, data=json.dumps(data))
    return response.json()

def CREATE_TABLE_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()

    # 添加参数，此参数用来指定应用的访问令牌
    parser.add_argument('--access_token', help='表格的访问令牌')

    # 添加参数，此参数用来指定表格的名称
    parser.add_argument('--table_name', help='表格的名称')
    
    # 添加参数，此参数用来指定目标文件夹token
    parser.add_argument('--folder_token', help='目标文件夹token')

    args = parser.parse_args()

    # 调用 CREATE_TABLE 函数，创建数据表
    response = CREATE_TABLE(
        access_token=args.access_token,
        table_name=args.table_name,
        folder_token=args.folder_token
    )

    # 打印响应结果
    print(response)


# 主函数
if __name__ == "__main__":
    CREATE_TABLE_CMD()
