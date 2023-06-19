import argparse
import configparser
from GET_RECORD_ID import GET_RECORD_ID_CMD

# 此函数用于将从GET_RECORD_ID_CMD获取的record_id写入到配置文件
def WRITE_RECORD_ID(value):
    config = configparser.ConfigParser()  # 创建一个ConfigParser对象
    config.read('feishu-config.ini', encoding='utf-8')  # 读取名为'feishu-config.ini'的配置文件

    # 尝试从value获取record_id
    try:
        record_id = GET_RECORD_ID_CMD(value)
        # 如果提取的值不存在，将其置为空字符串
        if not record_id:
            record_id = ''
    except Exception:  # 如果在尝试过程中出现错误，返回None
        return None

    # 检查配置文件是否存在名为'ID'的section，如果不存在则添加
    if 'ID' not in config:
        config.add_section('ID')
    # 在'ID' section下添加record_id
    config['ID']['record_id'] = record_id

    # 尝试将新的配置写入到名为'feishu-config.ini'的文件中
    try:
        with open('feishu-config.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)
    except Exception:  # 如果在尝试过程中出现错误，返回None
        return None

    return record_id  # 如果一切正常，返回提取的值


# 此函数用于解析命令行参数并调用WRITE_RECORD_ID函数
def WRITE_RECORD_ID_CMD():
    # 创建一个argparse对象，用于解析命令行参数
    parser = argparse.ArgumentParser()
    # 添加一个命名为'-v'或'--value'的参数，该参数是可选的，作用是提供一个字段值
    parser.add_argument('-v', '--value', default=None, help='字段值')
    # 添加一个命名为'-i'或'--input'的参数，该参数是可选的，作用是提供一个字段值
    parser.add_argument('-i', '--input', default=None, help='字段值')
    # 解析命令行参数
    args = parser.parse_args()

    # 检查'-v/--value'和'-i/--input'参数，优先使用'-v/--value'
    field_value = args.value if args.value is not None else args.input

    if field_value is None:  # 如果没有提供字段值，则打印错误信息并退出
        print("错误：未提供字段值，请使用'-v/--value'或'-i/--input'参数提供字段值。")
        return

    # 调用WRITE_RECORD_ID函数，将从字段值获取的record_id写入到配置文件中
    result = WRITE_RECORD_ID(field_value)

    # 检查WRITE_RECORD_ID函数的返回结果
    if result is None:  # 如果返回None，打印错误信息
        print("发生错误，请检查您的输入字段值并再试一次。")
    else:  # 如果返回的不是None，打印提取的值和成功信息
        print(f"record_id: {result}")
        print("成功写入 'feishu-config.ini' 文件")



# 主函数
if __name__ == "__main__":
    # 调用解析命令行参数的函数
    WRITE_RECORD_ID_CMD()
