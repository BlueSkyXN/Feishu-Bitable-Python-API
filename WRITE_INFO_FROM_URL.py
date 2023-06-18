import argparse
import configparser
from GET_INFO_FROM_URL import GET_APPTOKEN_FROM_URL, GET_TABLEID_FROM_URL, GET_VIEWID_FROM_URL

# 这个函数用于将从URL中提取的信息写入到配置文件
def WRITE_INFO_FROM_URL(url):
    config = configparser.ConfigParser()  # 创建一个ConfigParser对象
    config.read('feishu-config.ini')  # 读取名为'feishu-config.ini'的配置文件

    # 尝试从URL中提取app_token, table_id, view_id
    try:
        app_token = GET_APPTOKEN_FROM_URL(url)
        table_id = GET_TABLEID_FROM_URL(url)
        view_id = GET_VIEWID_FROM_URL(url)

        # 如果任何一个提取的值不存在，将其置为空字符串
        if not app_token:
            app_token = ''
        if not table_id:
            table_id = ''
        if not view_id:
            view_id = ''
    except Exception:  # 如果在尝试过程中出现错误，返回None
        return None

    # 检查配置文件是否存在名为'TOKEN'的section，如果不存在则添加
    if 'TOKEN' not in config:
        config.add_section('TOKEN')
    # 在'TOKEN' section下添加app_token
    config['TOKEN']['app_token'] = app_token

    # 检查配置文件是否存在名为'ID'的section，如果不存在则添加
    if 'ID' not in config:
        config.add_section('ID')
    # 在'ID' section下添加table_id和view_id
    config['ID']['table_id'] = table_id
    config['ID']['view_id'] = view_id

    # 尝试将新的配置写入到名为'feishu-config.ini'的文件中
    try:
        with open('feishu-config.ini', 'w') as configfile:
            config.write(configfile)
    except Exception:  # 如果在尝试过程中出现错误，返回None
        return None

    return app_token, table_id, view_id  # 如果一切正常，返回提取的值


# 这个函数用于解析命令行参数并调用WRITE_INFO_FROM_URL函数
def WRITE_INFO_FROM_URL_CMD():
    # 创建一个argparse对象，用于解析命令行参数
    parser = argparse.ArgumentParser()
    # 添加一个命名为'-u'或'--url'的参数，该参数是必需的，作用是提供一个URL以供提取token
    parser.add_argument('-u', '--url', required=True, help='用于提取令牌的URL')
    # 解析命令行参数
    args = parser.parse_args()
    # 调用WRITE_INFO_FROM_URL函数，将从URL中提取的token写入到配置文件中
    result = WRITE_INFO_FROM_URL(args.url)

    # 检查WRITE_INFO_FROM_URL函数的返回结果
    if result is None:  # 如果返回None，打印错误信息
        print("发生错误，请检查您的输入URL并再试一次。")
    else:  # 如果返回的不是None，打印提取的值和成功信息
        app_token, table_id, view_id = result
        print(f"app_token: {app_token}")
        print(f"table_id: {table_id}")
        print(f"view_id: {view_id}")
        print("成功写入 'feishu-config.ini' 文件")


# 主函数
if __name__ == "__main__":
    # 调用解析命令行参数的函数
    WRITE_INFO_FROM_URL_CMD()
