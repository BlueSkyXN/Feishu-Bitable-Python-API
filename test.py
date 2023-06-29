from FeishuBitableAPI import FeishuBitableAPI

# 创建 FeishuBitableAPI 类的实例
api = FeishuBitableAPI()

# 调用类的方法进行测试
app_token = api.GET_APP_ACCESS_TOKEN(app_id="your_app_id", app_secret="your_app_secret", config_file="your_config_file.ini")
table_info = api.GET_FIELD_INFO(field_name="your_field_name", app_token="your_app_token", table_id="your_table_id")
# 其他方法的调用...

# 打印测试结果或进行其他操作
print("App Token:", app_token)
print("Table Info:", table_info)
# 其他结果的打印或操作...
