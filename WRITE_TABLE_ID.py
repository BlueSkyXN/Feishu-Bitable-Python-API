import argparse
import configparser
from GET_TABLE_ID import GET_TABLE_ID

# 这个函数用于将从GET_TABLE_ID获取的table_id写入到配置文件
def WRITE_TABLE_ID(name):
    config = configparser.ConfigParser()  # 创建一个ConfigParser对象
    config.read('feishu-config.ini')  # 读取名为'feishu-config.ini'的配置文件

    # 尝试从name获取table_id
    try:
        table_id = GET_TABLE_ID(name)
        # 如果提取的值不存在，将其置为空字符串
        if not table_id:
            table_id = ''
    except Exception:  # 如果在尝试过程中出现错误，返回None
        return None

    # 检查配置文件是否存在名为'ID'的section，如果不存在则添加
    if 'ID' not in config:
        config.add_section('ID')
    # 在'ID' section下添加table_id
    config['ID']['table_id'] = table_id

    # 尝试将新的配置写入到名为'feishu-config.ini'的文件中
    try:
        with open('feishu-config.ini', 'w') as configfile:
            config.write(configfile)
    except Exception:  # 如果在尝试过程中出现错误，返回None
        return None

    return table_id  # 如果一切正常，返回提取的值


# 这个函数用于解析命令行参数并调用WRITE_TABLE_ID函数
def WRITE_TABLE_ID_CMD():
    # 创建一个argparse对象，用于解析命令行参数
    parser = argparse.ArgumentParser()
    # 添加一个命名为'-n'或'--name'的参数，该参数是必需的，作用是提供一个数据表的名称
    parser.add_argument('-n', '--name', required=True, help='数据表的名称')
    # 解析命令行参数
    args = parser.parse_args()
    # 调用WRITE_TABLE_ID函数，将从数据表名称获取的table_id写入到配置文件中
    result = WRITE_TABLE_ID(args.name)

    # 检查WRITE_TABLE_ID函数的返回结果
    if result is None:  # 如果返回None，打印错误信息
        print("发生错误，请检查您的输入数据表名称并再试一次。")
    else:  # 如果返回的不是None，打印提取的值和成功信息
        print(f"table_id: {result}")
        print("成功写入 'feishu-config.ini' 文件")


# 主函数
if __name__ == "__main__":
    # 调用解析命令行参数的函数
    WRITE_TABLE_ID_CMD()
