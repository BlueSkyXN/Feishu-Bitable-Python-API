from FeishuBitableAPI import FeishuBitableAPI

# 创建 FeishuBitableAPI 类的实例
api = FeishuBitableAPI()

# 调用类的方法进行测试
app_token = api.GET_APPTOKEN_FROM_URL("https://ruijie.feishu.cn/base/VwGhbo65BaYLaOsSz1nciWc5ncb?table=tblzDsYuQkXfoy9e&view=vewAgGXuqf")


# 打印测试结果或进行其他操作
print("App Token:", app_token)

# 其他结果的打印或操作...
