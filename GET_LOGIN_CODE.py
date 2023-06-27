from urllib.parse import urlparse, parse_qs
import configparser
import argparse

def GET_LOGIN_CODE(redirect_uri=None, app_id=None, config_file=None):
    config = configparser.ConfigParser()

    # 如果配置文件路径为空，则使用默认路径
    if not config_file:
        config_file = 'feishu-config.ini'

    config.read(config_file, encoding='utf-8')

    # 获取重定向URL
    if not redirect_uri:
        redirect_uri = config.get('LOGIN_CODE', 'redirect_uri', fallback='http://127.0.0.1/')

    # 获取app_id
    if not app_id:
        app_id = config.get('LOGIN_CODE', 'app_id', fallback='cli_a40141935331100e')

    login_url = f"https://open.feishu.cn/open-apis/authen/v1/index?redirect_uri={redirect_uri}&app_id={app_id}&state=some_random_string"
    print(f"请访问以下 URL 进行登录：\n{login_url}")
    new_url = input("请输入登录后得到的新的 URL：")
    parsed_url = urlparse(new_url)
    parsed_query = parse_qs(parsed_url.query)
    code = parsed_query.get("code")
    if code:
        return code[0]
    else:
        return None

def GET_LOGIN_CODE_CMD():
    parser = argparse.ArgumentParser(description='Get login code.')
    parser.add_argument('-r', '--redirect_uri', help='Redirect URL')
    parser.add_argument('-a', '--app_id', help='App ID')
    parser.add_argument('-c', '--config_file', help='Config file path')
    args = parser.parse_args()

    redirect_uri = args.redirect_uri
    app_id = args.app_id
    config_file = args.config_file

    code = GET_LOGIN_CODE(redirect_uri, app_id, config_file)
    if code:
        print(f"获取到的 code 是：{code}")
    else:
        print("没有在 URL 中找到 code。")

# 主函数
if __name__ == "__main__":
    GET_LOGIN_CODE_CMD()
