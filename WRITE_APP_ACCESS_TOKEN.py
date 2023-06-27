import configparser
from GET_APP_ACCESS_TOKEN import GET_APP_ACCESS_TOKEN
import argparse

def WRITE_APP_ACCESS_TOKEN(app_id=None, app_secret=None, config_file=None):
    config = configparser.ConfigParser()  # 创建一个ConfigParser对象
    if config_file:
        config.read(config_file, encoding='utf-8')  # 读取指定的配置文件
    else:
        config.read('feishu-config.ini', encoding='utf-8')  # 默认读取名为'feishu-config.ini'的配置文件

    # 尝试从app_id和app_secret获取app_access_token
    try:
        app_access_token = GET_APP_ACCESS_TOKEN(app_id, app_secret, config_file)
        # 如果提取的值不存在，将其置为空字符串
        if not app_access_token:
            app_access_token = ''
    except Exception:  # 如果在尝试过程中出现错误，返回None
        return None

    # 检查配置文件是否存在名为'TOKEN'的section，如果不存在则添加
    if 'TOKEN' not in config:
        config.add_section('TOKEN')
    # 在'TOKEN' section下添加app_access_token
    config['TOKEN']['app_access_token'] = app_access_token

    # 尝试将新的配置写入到配置文件中
    try:
        if config_file:
            with open(config_file, 'w', encoding='utf-8') as configfile:
                config.write(configfile)
        else:
            with open('feishu-config.ini', 'w', encoding='utf-8') as configfile:
                config.write(configfile)
    except Exception:  # 如果在尝试过程中出现错误，返回None
        return None

    return app_access_token  # 如果一切正常，返回提取的值

# 主函数
if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--id', help='app ID')
    parser.add_argument('-s', '--secret', help='app secret')
    parser.add_argument('--config_file', help='config file path')
    args = parser.parse_args()

    # 调用WRITE_APP_ACCESS_TOKEN函数，将从app_id和app_secret获取的app_access_token写入到配置文件中
    result = WRITE_APP_ACCESS_TOKEN(args.id, args.secret, args.config_file)

    # 检查WRITE_APP_ACCESS_TOKEN函数的返回结果
    if result is None:  # 如果返回None，打印错误信息
        print("发生错误，请检查您的输入并再试一次。")
    else:  # 如果返回的不是None，打印提取的值和成功信息
        print(f"app_access_token: {result}")
        print("成功写入配置文件")
