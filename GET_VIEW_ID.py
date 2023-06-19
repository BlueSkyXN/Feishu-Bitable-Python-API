import argparse
from LIST_VIEWS import LIST_VIEWS

# 检索视图
# 此函数用于通过给定的名称获取视图的ID
def GET_VIEW_ID(view_name="默认视图"):
    response = LIST_VIEWS()  # 调用LIST_VIEWS函数获取所有视图的信息

    # 在返回的所有视图信息中，寻找名称匹配的视图
    for item in response["data"]["items"]:
        if item["view_name"] == view_name:  # 如果找到了名称匹配的视图，返回其ID
            return item["view_id"]

    return "NONE"  # 如果没有找到名称匹配的视图，返回"NONE"

# 此函数用于解析命令行参数并调用GET_VIEW_ID函数
def GET_VIEW_ID_CMD():
    parser = argparse.ArgumentParser()  # 创建一个命令行参数解析对象
    # 添加一个名为'-n'或'--name'的参数，此参数用来指定要查询的视图的名称
    parser.add_argument('-n', '--name', default=None, help='视图的名字')
    # 添加一个名为'-i'或'--input'的参数，此参数也用来指定要查询的视图的名称
    parser.add_argument('-i', '--input', default=None, help='视图的名字')
    args = parser.parse_args()  # 解析命令行参数

    # 检查'-n/--name'和'-i/--input'参数，优先使用'-n/--name'
    view_name = args.name if args.name is not None else args.input

    if view_name is None:  # 如果没有提供视图名称，则打印错误信息并退出
        print("错误：未提供视图名称，请使用'-n/--name'或'-i/--input'参数提供视图名称。")
        return

    view_id = GET_VIEW_ID(view_name)  # 调用GET_VIEW_ID函数获取视图的ID
    print(view_id)  # 打印视图的ID


# 主函数
if __name__ == "__main__":
    GET_VIEW_ID_CMD()  # 调用GET_VIEW_ID_CMD函数
