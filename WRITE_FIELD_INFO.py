import configparser
import argparse
from GET_FIELD_INFO import GET_FIELD_INFO

# 将字段信息写入配置文件
def WRITE_FIELD_INFO(field_name=None, field_id=None, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
    if config_file is None:
        config_file = "feishu-config.ini"

    config = configparser.ConfigParser()
    config.read(config_file, encoding="utf-8")

    # 调用GET_FIELD_INFO函数获取字段信息
    field_info = GET_FIELD_INFO(field_name, field_id, app_token, table_id, view_id, page_token, page_size, config_file)

    # 检查配置文件是否存在名为'FIELD_INFO'的section，如果不存在则添加
    if "FIELD_INFO" not in config:
        config.add_section("FIELD_INFO")

    # 在'FIELD_INFO' section下添加field_info
    config.set("FIELD_INFO", "field_info", json.dumps(field_info))

    # 尝试将新的配置写入到配置文件中
    try:
        with open(config_file, "w", encoding="utf-8") as configfile:
            config.write(configfile)
    except Exception as e:
        print(f"写入配置文件错误: {str(e)}")
        return

    print(f"成功写入field_info: {field_info} 到 '{config_file}' 文件")


def WRITE_FIELD_INFO_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", default=None, help="字段名称")
    parser.add_argument("-i", "--id", default=None, help="字段ID")
    parser.add_argument("--app_token", help="app token")
    parser.add_argument("--table_id", help="table ID")
    parser.add_argument("--view_id", help="view ID")
    parser.add_argument("--page_token", help="page token")
    parser.add_argument("--page_size", type=int, help="page size")
    parser.add_argument("--config_file", default="feishu-config.ini", help="配置文件路径")
    args = parser.parse_args()

    # 调用WRITE_FIELD_INFO函数，将字段信息写入配置文件
    WRITE_FIELD_INFO(
        field_name=args.name,
        field_id=args.id,
        app_token=args.app_token,
        table_id=args.table_id,
        view_id=args.view_id,
        page_token=args.page_token,
        page_size=args.page_size,
        config_file=args.config_file
    )


if __name__ == "__main__":
    WRITE_FIELD_INFO_CMD()
