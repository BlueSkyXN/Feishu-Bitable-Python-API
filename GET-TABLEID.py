import argparse
from LIST_DATATABLES import LIST_DATATABLES

# 此函数用于通过给定的名称获取表的ID
def GET_TABLE_ID(name="数据表"):
    response = LIST_DATATABLES()  # 调用LIST_DATATABLES函数获取所有数据表的信息

    # 在返回的所有数据表信息中，寻找名称匹配的数据表
    for item in response["data"]["items"]:
        if item["name"] == name:  # 如果找到了名称匹配的数据表，返回其ID
            return item["table_id"]

    return "NONE"  # 如果没有找到名称匹配的数据表，返回"NONE"

# 此函数用于解析命令行参数并调用GET_TABLE_ID函数
def GET_TABLE_ID_CMD():
    parser = argparse.ArgumentParser()  # 创建一个命令行参数解析对象
    # 添加一个名为'-i'或'--input'的参数，此参数默认值为"数据表"，用来指定要查询的数据表的名称
    parser.add_argument('-i', '--input', default="数据表", help='数据表的名字')
    args = parser.parse_args()  # 解析命令行参数
    table_id = GET_TABLE_ID(args.input)  # 调用GET_TABLE_ID函数获取表的ID
    print(table_id)  # 打印表的ID

# 主函数
if __name__ == "__main__":
    GET_TABLE_ID_CMD()  # 调用GET_TABLE_ID_CMD函数
