import requests
import configparser
from datetime import datetime

# 读取配置文件
config = configparser.ConfigParser()
config.read('feishu-config.ini', encoding='utf-8')

# 提取tokens和app_token
user_access_token = config.get('TOKEN', 'user_access_token')
app_token = config.get('TOKEN', 'app_token')

# 设置请求URL
url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables"

# 设置请求头
headers = {
    "Authorization": f"Bearer {user_access_token}",
    "Content-Type": "application/json; charset=utf-8"
}

# 定义基础表名和视图名
base_table_name = "新建数据表"
base_view_name = "表格"

# 初始化字段列表
fields = [
    {
        "field_name": "KEY",
        "type": 1
    },
    {
        "field_name": "多行文本",
        "type": 1
    }
]

# 初始化请求数据
data = {
    "table": {
        "name": base_table_name,
        "default_view_name": base_view_name,
        "fields": fields
    }
}

# 发送请求
response = requests.post(url, headers=headers, json=data)
response_json = response.json()

# 检查是否表名重复
if response_json.get('code') in [1254013, 1254001]:
    # 获取当前日期
    current_date = datetime.now().strftime('%m%d')
    # 更新表名
    new_table_name = f"{base_table_name} {current_date}"
    print(f"New table name: {new_table_name}")  # 打印新的表名以便进行故障排除
    data["table"]["name"] = new_table_name
    # 重新发送请求
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

# 打印响应
print(response_json)
