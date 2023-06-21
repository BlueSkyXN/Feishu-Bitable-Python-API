import urllib.parse
import configparser

def WRITE_LOGIN_CODE():
    # 提示用户访问登录 URL，并从中获取 code
    print("请访问以下 URL 进行登录：")
    print("https://open.feishu.cn/open-apis/authen/v1/index?redirect_uri=http://127.0.0.1/&app_id=cli_a40141935331100e&state=some_random_string")

    redirected_url = input("请输入登录后得到的新的 URL：")
    parsed_url = urllib.parse.urlparse(redirected_url)
    parsed_query = urllib.parse.parse_qs(parsed_url.query)

    # 从 URL 的查询参数中获取 code
    login_code = parsed_query.get('code', [None])[0]
    if login_code is None:
        print("在输入的 URL 中没有找到 'code' 参数。")
        return

    print(f"获取到的 login_code 是：{login_code}")

    # 创建一个 configparser 对象，用于读取和写入配置文件
    config = configparser.ConfigParser()
    config.read('feishu-config.ini', encoding='utf-8')

    # 检查配置文件是否存在名为 'TOKEN' 的 section，如果不存在则添加
    if 'TOKEN' not in config:
        config.add_section('TOKEN')

    # 在 'TOKEN' section 下添加 login_code
    config['TOKEN']['login_code'] = login_code

    # 尝试将新的配置写入到名为 'feishu-config.ini' 的文件中
    try:
        with open('feishu-config.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)
    except Exception as e:
        print(f"写入配置文件时出现错误：{e}")
        return

    print("登录预授权码已成功写入 'feishu-config.ini' 文件。")

if __name__ == "__main__":
    WRITE_LOGIN_CODE()
