import configparser
from GET_RECORD_ID import GET_RECORD_ID

# 此函数用于将从GET_RECORD_ID获取的record_id写入到配置文件
def WRITE_RECORD_ID(field_name, value):
    config = configparser.ConfigParser()  # 创建一个ConfigParser对象
    config.read('feishu-config.ini', encoding='utf-8')  # 读取名为'feishu-config.ini'的配置文件

    # 调用GET_RECORD_ID函数获取记录的ID
    record_id = GET_RECORD_ID(value, field_name)

    # 检查配置文件是否存在名为'ID'的section，如果不存在则添加
    if 'ID' not in config:
        config.add_section('ID')
    # 在'ID' section下添加record_id
    config['ID']['record_id'] = record_id

    # 尝试将新的配置写入到名为'feishu-config.ini'的文件中
    try:
        with open('feishu-config.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)
    except Exception as e:  # 如果在尝试过程中出现错误，打印错误信息并退出
        print(f"写入配置文件错误: {str(e)}")
        return

    print(f"成功写入record_id: {record_id} 到 'feishu-config.ini' 文件")

def WRITE_RECORD_ID_CMD():
    import argparse
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    # 添加第一个参数，此参数用来指定要查询的字段名，有多种命令行输入方式
    parser.add_argument('-f', '--field', default=None, help='字段名')
    parser.add_argument('--field_name', default=None, help='字段名')
    parser.add_argument('-n', '--name', default=None, help='字段名')
    parser.add_argument('-k', '--key', default=None, help='字段名')
    # 添加第二个参数，此参数用来指定要查询的字段值
    parser.add_argument('-v', '--value', required=True, help='字段值')
    args = parser.parse_args()

    # 按照优先级顺序检查字段名参数的值，优先级顺序是 '-f/--field' > '--field_name' > '-n/--name' > '-k/--key'
    field_name = args.field if args.field is not None else args.field_name if args.field_name is not None else args.name if args.name is not None else args.key

    if field_name is None:  # 如果没有提供字段名，则打印错误信息并退出
        print("错误：未提供字段名，请使用'-f/--field'或'--field_name'或'-n/--name'或'-k/--key'参数提供字段名。")
        return

    # 调用WRITE_RECORD_ID函数，将从字段名和字段值获取的record_id写入到配置文件中
    WRITE_RECORD_ID(field_name, args.value)


# 主函数
if __name__ == "__main__":
    WRITE_RECORD_ID_CMD()
