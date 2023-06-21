from urllib.parse import urlparse, parse_qs

# 显示登录 URL
login_url = "https://open.feishu.cn/open-apis/authen/v1/index?redirect_uri=http://127.0.0.1/&app_id=cli_a40141935331100e&state=some_random_string"
print(f"请访问以下 URL 进行登录：\n{login_url}")

# 提示用户输入新的 URL
new_url = input("请输入登录后得到的新的 URL：")

# 解析新的 URL
parsed_url = urlparse(new_url)
parsed_query = parse_qs(parsed_url.query)

# 提取出 code
code = parsed_query.get("code")
if code:
    print(f"获取到的 code 是：{code[0]}")
else:
    print("没有在 URL 中找到 code。")
