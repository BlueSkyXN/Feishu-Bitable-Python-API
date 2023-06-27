import urllib.parse
import configparser
import argparse

def WRITE_LOGIN_CODE(redirect_uri=None, app_id=None, config_file=None):

    # 如果配置文件路径为空，则使用默认路径
    if not config_file:
        config_file = 'feishu-config.ini'
        
    # 创建一个 configparser 对象，用于读取和写入配置文件
    config = configparser.ConfigParser()


    config.read(config_file, encoding='utf-8')

    # 如果重定向URL未提供，则尝试从配置文件中获取，默认为 'http://127.0.0.1/'
    if redirect_uri is None:
        if config.has_option('LOGIN_CODE', 'redirect_uri'):
            redirect_uri = config.get('LOGIN_CODE', 'redirect_uri')
        else:
            redirect_uri = 'http://127.0.0.1/'

    # 如果app_id未提供，则尝试从配置文件中获取，默认为 'cli_a40141935331100e'
    if app_id is None:
        if config.has_option('LOGIN_CODE', 'app_id'):
            app_id = config.get('LOGIN_CODE', 'app_id')
        else:
            app_id = 'cli_a40141935331100e'

    # 提示用户访问登录 URL，并从中获取 code
    print("请访问以下 URL 进行登录：")
    
    login_url = f"https://open.feishu.cn/open-apis/authen/v1/index?redirect_uri={redirect_uri}&app_id={app_id}&state=some_random_string"
    
    print(login_url)

    redirected_url = input("请输入登录后得到的新的 URL：")
    parsed_url = urllib.parse.urlparse(redirected_url)
    parsed_query = urllib.parse.parse_qs(parsed_url.query)

    # 从 URL 的查询参数中获取 code
    login_code = parsed_query.get('code', [None])[0]
    if login_code is None:
        print("在输入的 URL 中没有找到 'code' 参数。")
        return

    print(f"获取到的 login_code 是：{login_code}")

    # 检查配置文件是否存在名为 'TOKEN' 的 section，如果不存在则添加
    if 'TOKEN' not in config:
        config.add_section('TOKEN')

    # 在 'TOKEN' section 下添加 login_code
    config['TOKEN']['login_code'] = login_code

    # 尝试将新的配置写入到配置文件中
    try:
        with open(config_file, 'w', encoding='utf-8') as configfile:
            config.write(configfile)
    except Exception as e:
        print(f"写入配置文件时出现错误：{e}")
        return

    print(f"登录预授权码已成功写入 '{config_file}' 文件。")

def WRITE_LOGIN_CODE_CMD():
    parser = argparse.ArgumentParser(description='Write login code to config file.')
    parser.add_argument('-r', '--redirect_uri', default=None, help='Redirect URL')
    parser.add_argument('-a', '--app_id', default=None, help='App ID')
    parser.add_argument('-c', '--config_file', default='feishu-config.ini', help='Config file path')
    args = parser.parse_args()

    redirect_uri = args.redirect_uri
    app_id = args.app_id
    config_file = args.config_file

    WRITE_LOGIN_CODE(redirect_uri, app_id, config_file)

# 主函数
if __name__ == "__main__":
    WRITE_LOGIN_CODE_CMD()
