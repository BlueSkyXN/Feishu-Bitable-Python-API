import argparse
import configparser
from GET_TABLE_ID import GET_TABLE_ID

# 检索字段并写入配置文件
# 这个函数用于将从 GET_TABLE_ID 获取的 table_id 写入到配置文件
def WRITE_TABLE_ID(name, app_token=None, user_access_token=None, page_size=None, page_token=None, config_file=None):
    config = configparser.ConfigParser()  # 创建一个 ConfigParser 对象
    config.read(config_file, encoding='utf-8')  # 读取配置文件

    # 尝试从 name 获取 table_id
    try:
        table_id = GET_TABLE_ID(name, app_token, user_access_token, page_size, page_token, config_file)
        # 如果提取的值不存在，将其置为空字符串
        if not table_id:
            table_id = ''
    except Exception:
        return None  # 如果在尝试过程中出现错误，返回 None

    # 检查配置文件是否存在名为 'ID' 的 section，如果不存在则添加
    if 'ID' not in config:
        config.add_section('ID')
    # 在 'ID' section 下添加 table_id
    config['ID']['table_id'] = table_id

    # 尝试将新的配置写入到配置文件中
    try:
        with open(config_file, 'w', encoding='utf-8') as configfile:
            config.write(configfile)
    except Exception:
        return None  # 如果在尝试过程中出现错误，返回 None

    return table_id  # 如果一切正常，返回提取的值


# 这个函数用于解析命令行参数并调用 WRITE_TABLE_ID 函数
def WRITE_TABLE_ID_CMD():
    parser = argparse.ArgumentParser()  # 创建一个 argparse 对象，用于解析命令行参数
    # 添加一个命名为 '-n' 或 '--name' 的参数，该参数是可选的，作用是提供一个数据表的名称
    parser.add_argument('-n', '--name', default=None, help='数据表的名称')
    # 添加一个命名为 '-i' 或 '--input' 的参数，该参数是可选的，作用是提供一个数据表的名称
    parser.add_argument('-i', '--input', default=None, help='数据表的名称')
    parser.add_argument('--app_token', help='app token')
    parser.add_argument('--user_access_token', help='user access token')
    parser.add_argument('--page_size', type=int, help='page size')
    parser.add_argument('--page_token', help='page token')
    parser.add_argument('--config_file', default="feishu-config.ini", help='config file path')
    args = parser.parse_args()

    # 检查 '--name' 和 '-n' 参数，优先使用 '--name'
    table_name = args.name if args.name is not None else args.input

    if table_name is None:  # 如果没有提供数据表名称，则打印错误信息并退出
        print("错误：未提供数据表名称，请使用'-n/--name'或'-i/--input'参数提供数据表名称。")
        return

    # 调用 WRITE_TABLE_ID 函数，将从数据表名称获取的 table_id 写入到配置文件中
    result = WRITE_TABLE_ID(table_name, args.app_token, args.user_access_token, args.page_size, args.page_token, args.config_file)

    # 检查 WRITE_TABLE_ID 函数的返回结果
    if result is None:  # 如果返回 None，打印错误信息
        print("发生错误，请检查您的输入数据表名称并再试一次。")
    else:  # 如果返回的不是 None，打印提取的值和成功信息
        print(f"table_id: {result}")
        print("成功写入 'feishu-config.ini' 文件")


# 主函数
if __name__ == "__main__":
    # 调用解析命令行参数的函数
    WRITE_TABLE_ID_CMD()
