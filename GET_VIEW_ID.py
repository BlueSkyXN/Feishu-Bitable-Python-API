import argparse
from LIST_VIEWS import LIST_VIEWS

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
    # 添加一个名为'-n'或'--name'的参数，此参数默认值为"默认视图"，用来指定要查询的视图的名称
    parser.add_argument('-n', '--name', default="表格", help='视图的名字')
    args = parser.parse_args()  # 解析命令行参数
    view_id = GET_VIEW_ID(args.name)  # 调用GET_VIEW_ID函数获取视图的ID
    print(view_id)  # 打印视图的ID

# 主函数
if __name__ == "__main__":
    GET_VIEW_ID_CMD()  # 调用GET_VIEW_ID_CMD函数
