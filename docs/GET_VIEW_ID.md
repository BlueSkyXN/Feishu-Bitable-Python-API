# GET_VIEW_ID.py 文档

GET_VIEW_ID.py 是一个用于检索视图 ID 的工具。它提供了一个函数 `GET_VIEW_ID()`，可以通过给定的视图名称获取视图的 ID。

## 目录

- [介绍](#介绍)
- [使用指南](#使用指南)
- [函数介绍](#函数介绍)
- [示例](#示例)
- [注意事项](#注意事项)

## 介绍

GET_VIEW_ID.py 是一个用于访问飞书多维表格 API 的工具。它使用飞书的 API 来检索指定视图名称的视图 ID。通过提供必要的认证信息和参数，用户可以轻松地获取视图 ID。

## 使用指南

### 导入方式

可以导入 GET_VIEW_ID.py 脚本，并调用 `GET_VIEW_ID()` 函数来获取视图 ID。以下是函数的定义和参数说明：

```python
def GET_VIEW_ID(view_name="默认视图", app_token=None, user_access_token=None, page_size=None, page_token=None, config_file=None):
    # 函数体...

# 使用示例
view_id = GET_VIEW_ID(view_name, app_token, user_access_token, page_size, page_token, config_file)
```

- `view_name`：要查询的视图名称。默认为 "默认视图"。
- `app_token`：飞书应用的唯一标识符 (app token)。如果未提供，将从配置文件中获取默认值。
- `user_access_token`：用户访问令牌 (user access token)。如果未提供，将从配置文件中获取默认值。
- `page_size`：分页大小，指定每页返回的数据表视图数量。如果未提供，将从配置文件中获取默认值。
- `page_token`：分页标记，用于获取下一页数据表视图列表。如果未提供，将从配置文件中获取默认值。
- `config_file`：配置文件路径，指定配置文件的位置。如果未提供，将使用默认的配置文件路径。

### 命令行方式

通过命令行参数直接运行 GET_VIEW_ID.py 脚本可以获取视图 ID。以下是命令行参数的说明：

```bash
$ python GET_VIEW_ID.py --name <view_name> --app_token <app_token> --user_access_token <user_access_token> --page_size <page_size> --page_token <page_token> --config_file <config_file_path>
```

- `--name`：要查询的视图名称。
- `--app_token`：飞书应用的唯一标识符 (app token)。
- `--user_access_token`：用户访问令牌 (user access token)。
- `--page_size`：分页大小，指定每页返回的数据表视图数量。
- `--page_token`：分页标记，用于获取下一页数据表视图列表。
- `--config_file`：配置文件路径，指定配置文件的位置。

## 函数介绍

### GET_VIEW_ID 函数

此函数

用于通过给定的名称获取视图的 ID。函数的参数包括：

- `view_name`：要查询的视图名称。默认为 "默认视图"。
- `app_token`：飞书应用的唯一标识符 (app token)。默认为 None。
- `user_access_token`：用户访问令牌 (user access token)。默认为 None。
- `page_size`：分页大小，指定每页返回的数据表视图数量。默认为 None。
- `page_token`：分页标记，用于获取下一页数据表视图列表。默认为 None。
- `config_file`：配置文件路径，指定配置文件的位置。默认为 "feishu-config.ini"。

### GET_VIEW_ID_CMD 函数

此函数用于解析命令行参数并调用 GET_VIEW_ID 函数。函数无参数。

## 示例

以下是使用 GET_VIEW_ID.py 脚本的示例：

```bash
$ python GET_VIEW_ID.py --name <view_name> --app_token <app_token> --user_access_token <user_access_token> --page_size <page_size> --page_token <page_token> --config_file <config_file_path>
```

上述命令会使用指定的参数来获取视图 ID，并将结果输出。

```python
from GET_VIEW_ID import GET_VIEW_ID

view_name = "<view_name>"
app_token = "<app_token>"
user_access_token = "<user_access_token>"
page_size = <page_size>
page_token = "<page_token>"
config_file = "<config_file_path>"

view_id = GET_VIEW_ID(view_name, app_token, user_access_token, page_size, page_token, config_file)
print(view_id)
```

### 输出

脚本的输出是一个ID

## 注意事项

- 在使用 GET_VIEW_ID.py 时，需要确保已经正确安装了 Python 环境，并且已经安装了 argparse、configparser 和 LIST_VIEWS 模块。
- 在使用 GET_VIEW_ID.py 时，需要确保提供的认证信息和参数是正确的，并具有访问视图的权限。
- 在使用 GET_VIEW_ID.py 时，需要确保配置文件的格式和路径是正确的。
