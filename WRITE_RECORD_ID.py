import configparser
import argparse
from GET_RECORD_ID import GET_RECORD_ID

# 此函数用于将从GET_RECORD_ID获取的record_id写入到配置文件
def WRITE_RECORD_ID(value, field_name=None, config_file=None):
    if config_file is None:
        config_file = 'feishu-config.ini'

    config = configparser.ConfigParser()  # 创建一个ConfigParser对象
    config.read(config_file, encoding='utf-8')  # 读取名为'feishu-config.ini'的配置文件

    if field_name is None:
        field_name = config.get('LIST_RECORDS', 'key', fallback=None)

    # 调用GET_RECORD_ID函数获取记录的ID
    record_id = GET_RECORD_ID(value, field_name, config_file)

    # 检查配置文件是否存在名为'ID'的section，如果不存在则添加
    if 'ID' not in config:
        config.add_section('ID')
    # 在'ID' section下添加record_id
    config['ID']['record_id'] = record_id

    # 尝试将新的配置写入到名为'feishu-config.ini'的文件中
    try:
        with open(config_file, 'w', encoding='utf-8') as configfile:
            config.write(configfile)
    except Exception as e:  # 如果在尝试过程中出现错误，打印错误信息并退出
        print(f"写入配置文件错误: {str(e)}")
        return

    print(f"成功写入record_id: {record_id} 到配置文件 {config_file}")

def WRITE_RECORD_ID_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    # 添加第一个参数，此参数用来指定要查询的字段值
    parser.add_argument('-v', '--value', required=True, help='字段值')
    # 添加第二个参数，此参数用来指定要查询的字段名，有多种命令行输入方式
    parser.add_argument('-f', '--field', default=None, help='字段名')
    parser.add_argument('--field_name', default=None, help='字段名')
    parser.add_argument('-n', '--name', default=None, help='字段名')
    parser.add_argument('-k', '--key', default=None, help='字段名')
    parser.add_argument('--config_file', default='feishu-config.ini', help='配置文件路径')
    args = parser.parse_args()

    # 按照优先级顺序检查字段名参数的值，优先级顺序是 '-f/--field' > '--field_name' > '-n/--name' > '-k/--key'
    field_name = args.field if args.field is not None else args.field_name if args.field_name is not None else args.name if args.name is not None else args.key

    # 调用WRITE_RECORD_ID函数，将从字段值和字段名获取的record_id写入到配置文件中
    WRITE_RECORD_ID(args.value, field_name, args.config_file)


# 主函数
if __name__ == "__main__":
    WRITE_RECORD_ID_CMD()
