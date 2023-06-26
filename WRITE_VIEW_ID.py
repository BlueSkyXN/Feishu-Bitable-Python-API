import argparse
import configparser
from GET_VIEW_ID import GET_VIEW_ID

# 检索视图并写入配置文件
# 这个函数用于将从GET_VIEW_ID获取的view_id写入到配置文件
def WRITE_VIEW_ID(view_name, app_token=None, user_access_token=None, page_size=None, page_token=None, config_file=None):
    if config_file is None or not config_file.strip():  # 如果未提供配置文件路径，则使用默认的配置文件 'feishu-config.ini'
        config_file = 'feishu-config.ini'

    config = configparser.ConfigParser()  # 创建一个ConfigParser对象
    config.read(config_file, encoding='utf-8')  # 读取名为'feishu-config.ini'的配置文件

    view_id = GET_VIEW_ID(view_name, app_token, user_access_token, page_size, page_token, config_file)  # 调用GET_VIEW_ID函数获取视图的ID

    # 如果提取的值不存在，将其置为空字符串
    if not view_id:
        view_id = ''

    # 检查配置文件是否存在名为'ID'的section，如果不存在则添加
    if 'ID' not in config:
        config.add_section('ID')
    # 在'ID' section下添加view_id
    config['ID']['view_id'] = view_id

    # 尝试将新的配置写入到名为'feishu-config.ini'的文件中
    try:
        with open(config_file, 'w', encoding='utf-8') as configfile:
            config.write(configfile)
    except Exception:  # 如果在尝试过程中出现错误，返回None
        return None

    return view_id  # 如果一切正常，返回提取的值

# 这个函数用于解析命令行参数并调用WRITE_VIEW_ID函数
def WRITE_VIEW_ID_CMD():
    # 创建一个argparse对象，用于解析命令行参数
    parser = argparse.ArgumentParser()
    # 添加一个命名为'-n'或'--name'的参数，该参数是可选的，作用是提供一个视图的名称
    parser.add_argument('-n', '--name', default=None, help='视图的名称')
    # 添加一个命名为'-i'或'--view'的参数，该参数是可选的，作用是提供一个视图的名称
    parser.add_argument('-i', '--view', default=None, help='视图的名称')
    parser.add_argument('--app_token', help='应用的 token')
    parser.add_argument('--user_access_token', help='用户的 access token')
    parser.add_argument('--page_size', type=int, help='每页的大小')
    parser.add_argument('--page_token', help='分页标记')
    parser.add_argument('--config_file', default="feishu-config.ini", help='配置文件路径')
    args = parser.parse_args()

    view_name = args.view if args.view is not None else args.name  # 检查'-n/--name'和'-i/--view'参数，优先使用'-i/--view'

    if view_name is None:  # 如果没有提供视图名称，则打印错误信息并退出
        print("错误：未提供视图名称，请使用'-n/--name'或'-i/--view'参数提供视图名称。")
        return

    result = WRITE_VIEW_ID(view_name, args.app_token, args.user_access_token, args.page_size, args.page_token, args.config_file)

    if result is None:  # 如果返回None，打印错误信息
        print("发生错误，请检查您的输入视图名称并再试一次。")
    else:  # 如果返回的不是None，打印提取的值和成功信息
        print(f"view_id: {result}")
        print(f"成功写入配置文件 '{args.config_file}'")

# 主函数
if __name__ == "__main__":
    # 调用解析命令行参数的函数
    WRITE_VIEW_ID_CMD()