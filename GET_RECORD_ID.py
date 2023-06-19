import argparse
import configparser
from LIST_RECORDS import LIST_RECORDS

# 从给定的响应中获取具有特定字段值的记录的ID
def GET_RECORD_ID(response, field_name, value):
    # 在返回的所有记录信息中，寻找字段值匹配的记录
    for item in response["data"]["items"]:
        if item["fields"].get(field_name) == value:
            return item["record_id"]

    return "NONE"  # 如果没有找到字段值匹配的记录，返回"NONE"

# 此函数用于解析命令行参数并调用GET_RECORD_ID函数
def GET_RECORD_ID_CMD():
    parser = argparse.ArgumentParser()  # 创建一个命令行参数解析对象
    # 添加一个名为'-v'或'--value'的参数，此参数用来指定要查询的字段值
    parser.add_argument('-v', '--value', default=None, help='字段值')
    # 添加一个名为'-i'或'--input'的参数，此参数也用来指定要查询的字段值
    parser.add_argument('-i', '--input', default=None, help='字段值')
    args = parser.parse_args()  # 解析命令行参数

    # 检查'-v/--value'和'-i/--input'参数，优先使用'-v/--value'
    field_value = args.value if args.value is not None else args.input

    if field_value is None:  # 如果没有提供字段值，则打印错误信息并退出
        print("错误：未提供字段值，请使用'-v/--value'或'-i/--input'参数提供字段值。")
        return

    # 读取配置文件获取字段名
    config = configparser.ConfigParser()
    config.read('feishu-config.ini')
    field_name = config.get('LIST_RECORDS', 'key', fallback=None)

    # 调用LIST_RECORDS函数获取所有记录的信息
    response = LIST_RECORDS()

    # 调用GET_RECORD_ID函数获取记录的ID
    record_id = GET_RECORD_ID(response, field_name, field_value)
    print(record_id)  # 打印记录的ID


# 主函数
if __name__ == "__main__":
    GET_RECORD_ID_CMD()  # 调用GET_RECORD_ID_CMD函数
