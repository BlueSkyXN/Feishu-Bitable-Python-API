# LIST_VIEWS.py 文档

LIST_VIEWS.py 是一个用于列出数据表视图的工具。它提供了一个函数 `LIST_VIEWS()`，可以通过指定的参数或配置文件来获取数据表的视图列表。

参考官方API文档 [列出视图](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-view/list)

## 目录

- [介绍](#介绍)
- [使用指南](#使用指南)
- [函数介绍](#函数介绍)
- [示例](#示例)
- [注意事项](#注意事项)

## 介绍

LIST_VIEWS.py 是一个用于访问飞书多维表格 API 的工具。它使用飞书的 API 来列出指定数据表的所有视图。通过提供必要的认证信息和参数，用户可以轻松地获取数据表视图列表。

## 使用指南

### 导入方式

可以导入 LIST_VIEWS.py 脚本，并调用 `LIST_VIEWS()` 函数来获取数据表视图列表。以下是函数的定义和参数说明：

```python
def LIST_VIEWS(app_token=None, user_access_token=None, page_size=None, page_token=None, table_id=None, config_file=None):
    # 函数体...

# 使用示例
response_body = LIST_VIEWS(app_token, user_access_token, page_size, page_token, table_id, config_file)
```

- `app_token`：飞书应用的唯一标识符 (app token)。如果未提供，将从配置文件中获取默认值。
- `user_access_token`：用户访问令牌 (user access token)。如果未提供，将从配置文件中获取默认值。
- `page_size`：分页大小，指定每页返回的数据表视图数量。如果未提供，将从配置文件中获取默认值。
- `page_token`：分页标记，用于获取下一页数据表视图列表。如果未提供，将从配置文件中获取默认值。
- `table_id`：数据表的 ID，用于指定要获取视图列表的数据表。如果未提供，将从配置文件中获取默认值。
- `config_file`：配置文件路径，指定配置文件的位置。默认为 "feishu-config.ini"。

### 命令行方式

通过命令行参数直接运行 LIST_VIEWS.py 脚本可以获取数据表视图列表。以下是命令行参数的说明：

```bash
$ python LIST_VIEWS.py --app_token <app_token> --user_access_token <user_access_token> --page_size <page_size> --page_token <page_token> --table_id <table_id> --config_file <config_file_path>
```

- `--app_token`：飞书应用的唯一标识符 (app token)。
- `--user_access_token`：用户访问令牌 (user access token)。
- `--page_size`：分页大小，指定每页返回的数据表视图数量。
- `--page_token`：分页标记，用于获取下一页数据表视图列表。
- `--table_id`：数据表的 ID，用于指定要获取视图列表的数据表。
- `--config_file`：配置文件路径，指定配置文件的位置。默认为 "feishu-config.ini"。

## 函数介绍

### LIST_VIEWS 函数

此函数用于获取数据表的所有视图。函数的参数包括：

- `app_token`：飞书应用的唯一标识符 (app token)。默认为 None。
- `user_access_token`：用户访问令牌 (user access token)。默认为 None。
- `page_size`：分页大小，指定每页返回的数据表视图数量。默认为 None。
- `page_token`：分页标记，用于获取下一页数据表视图列表。默认为 None。
- `table_id`：数据表的 ID，用于指定要获取视图列表的数据表。默认为 None。
- `config_file`：配置文件路径，指定配置文件的位置。默认为 "feishu-config.ini"。

### LIST_VIEWS_CMD 函数

此函数用于解析命令行参数并调用 LIST_VIEWS 函数。函数无参数。

## 示例

以下是使用 LIST_VIEWS.py 脚本的示例：

```bash
$ python LIST_VIEWS.py --app_token <app_token> --user_access_token <user_access_token> --page_size <page_size> --page_token <page_token> --table_id <table_id> --config_file <config_file_path>
```

上述命令会使用指定的参数来获取数据表视图列表，并将结果以JSON格式输出。

```python
from LIST_VIEWS import LIST_VIEWS

app_token = "<app_token>"
user_access_token = "<user_access_token>"
page_size = <page_size>
page_token = "<page_token>"
table_id = "<table_id>"
config_file = "<config_file_path>"

response_body = LIST_VIEWS(app_token, user_access_token, page_size, page_token, table_id, config_file)
print(json.dumps(response_body, indent=4))
```

## 注意事项

- 在使用 LIST_VIEWS.py 时，需要确保已经正确安装了 Python 环境，并且已经安装了 requests、configparser、json 和 argparse 库。
- 在使用 LIST_VIEWS.py 时，需要确保提供的认证信息和参数是正确的，并具有访问数据表视图的权限。
- 在使用 LIST_VIEWS.py 时，需要确保配置文件的格式和路径是正确的。