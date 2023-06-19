import configparser
import argparse
from GET_FIELD_INFO import GET_FIELD_INFO

# 此函数用于将从GET_FIELD_INFO获取的字段信息写入到配置文件
def WRITE_FIELD_INFO(field_name=None, field_id=None):
    config = configparser.ConfigParser()  # 创建一个ConfigParser对象
    config.read('feishu-config.ini', encoding='utf-8')  # 读取名为'feishu-config.ini'的配置文件

    # 调用GET_FIELD_INFO函数获取字段的信息
    field_info = GET_FIELD_INFO(field_name, field_id)

    # 检查配置文件是否存在名为'FIELD_INFO'的section，如果不存在则添加
    if 'FIELD_INFO' not in config:
        config.add_section('FIELD_INFO')
    # 在'FIELD_INFO' section下添加field_info
    config['FIELD_INFO']['field_info'] = field_info

    # 尝试将新的配置写入到名为'feishu-config.ini'的文件中
    try:
        with open('feishu-config.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)
    except Exception as e:  # 如果在尝试过程中出现错误，打印错误信息并退出
        print(f"写入配置文件错误: {str(e)}")
        return

    print(f"成功写入field_info: {field_info} 到 'feishu-config.ini' 文件")

def WRITE_FIELD_INFO_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    # 添加第一个参数，此参数用来指定要查询的字段名
    parser.add_argument('-n', '--name', default=None, help='字段名')
    # 添加第二个参数，此参数用来指定要查询的字段ID
    parser.add_argument('-i', '--id', default=None, help='字段ID')
    args = parser.parse_args()

    # 调用WRITE_FIELD_INFO函数，将从字段名和字段ID获取的field_info写入到配置文件中
    WRITE_FIELD_INFO(args.name, args.id)

# 主函数
if __name__ == "__main__":
    WRITE_FIELD_INFO_CMD()
