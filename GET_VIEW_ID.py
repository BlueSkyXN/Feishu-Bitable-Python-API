import argparse
import configparser
from LIST_VIEWS import LIST_VIEWS

# 检索视图
# 此函数用于通过给定的名称获取视图的ID
def GET_VIEW_ID(view_name="默认视图", app_token=None, user_access_token=None, page_size=None, page_token=None, config_file=None):
    if config_file is None or not config_file.strip():  # 如果未提供配置文件路径，则使用默认的配置文件 'feishu-config.ini'
        config_file = 'feishu-config.ini'

    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    if not app_token:
        app_token = config.get('TOKEN', 'app_token')
    if not user_access_token:
        user_access_token = config.get('TOKEN', 'user_access_token')
    if not page_size:
        page_size = config.get('LIST_VIEWS', 'page_size', fallback=100)
    if not page_token:
        page_token = config.get('LIST_VIEWS', 'page_token', fallback=None)

    response = LIST_VIEWS(app_token, user_access_token, page_size, page_token, config_file)  # 调用LIST_VIEWS函数获取所有视图的信息

    # 在返回的所有视图信息中，寻找名称匹配的视图
    for item in response["data"]["items"]:
        if item["view_name"] == view_name:  # 如果找到了名称匹配的视图，返回其ID
            return item["view_id"]

    return "NONE"  # 如果没有找到名称匹配的视图，返回"NONE"

# 此函数用于解析命令行参数并调用GET_VIEW_ID函数
def GET_VIEW_ID_CMD():
    parser = argparse.ArgumentParser()  # 创建一个命令行参数解析对象
    parser.add_argument('-n', '--name', default=None, help='视图的名字')  # 添加一个名为'-n'或'--name'的参数，用于指定要查询的视图的名称
    parser.add_argument('-i', '--input', default=None, help='视图的名字')  # 添加一个名为'-i'或'--input'的参数，用于指定要查询的视图的名称
    parser.add_argument('--app_token', help='应用的 token')  # 添加一个名为'--app_token'的参数，用于传递应用的 token
    parser.add_argument('--user_access_token', help='用户的 access token')  # 添加一个名为'--user_access_token'的参数，用于传递用户的 access token
    parser.add_argument('--page_size', type=int, help='每页的大小')  # 添加一个名为'--page_size'的参数，用于传递每页的大小
    parser.add_argument('--page_token', help='分页标记')  # 添加一个名为'--page_token'的参数，用于传递分页标记
    parser.add_argument('--config_file', help='配置文件路径')  # 添加一个名为'--config_file'的参数，用于传递配置文件的路径
    args = parser.parse_args()  # 解析命令行参数

    view_name = args.name if args.name is not None else args.input  # 检查'-n/--name'和'-i/--input'参数，优先使用'-n/--name'

    if view_name is None:  # 如果没有提供视图名称，则打印错误信息并退出
        print("错误：未提供视图名称，请使用'-n/--name'或'-i/--input'参数提供视图名称。")
        return

    view_id = GET_VIEW_ID(view_name, args.app_token, args.user_access_token, args.page_size, args.page_token, args.config_file)  # 调用GET_VIEW_ID函数获取视图的ID
    print(view_id)  # 打印视图的ID


# 主函数
if __name__ == "__main__":
    GET_VIEW_ID_CMD()  # 调用GET_VIEW_ID_CMD函数
