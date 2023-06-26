# LIST_TABLES.py 文档

LIST_TABLES.py 是一个用于列出多维表格中所有数据表的工具。它提供了一个封装的函数 `LIST_TABLES()`，可以通过指定的参数或配置文件来获取数据表列表。

参考官方API文档 [列出数据表](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table/list#9dab04c2)


## 目录

- [介绍](#介绍)
- [使用指南](#使用指南)
- [设计思路](#设计思路)
- [输入输出](#输入输出)
- [示例](#示例)

## 介绍

LIST_TABLES.py 是一个用于访问飞书多维表格 API 的工具。它使用飞书的 API 来列出指定应用的所有数据表。通过提供必要的认证信息和参数，用户可以轻松地获取数据表列表。

该工具提供了两种使用方式：通过命令行参数直接运行脚本，或通过导入脚本并调用函数来获取数据表列表。

## 使用指南

### 命令行方式

通过命令行参数直接运行 LIST_TABLES.py 脚本可以获取数据表列表。以下是命令行参数的说明：

```bash
$ python LIST_TABLES.py --app_token <app_token> --user_access_token <user_access_token> --page_size <page_size> --page_token <page_token> --config_file <config_file_path>
```

- `--app_token`：飞书应用的唯一标识符 (app token)。
- `--user_access_token`：用户访问令牌 (user access token)。
- `--page_size`：分页大小，指定每页返回的数据表数量。
- `--page_token`：分页标记，用于获取下一页数据表列表。
- `--config_file`：配置文件路径，指定配置文件的位置。默认为 "feishu-config.ini"。

### 导入方式

可以导入 LIST_TABLES.py 脚本，并调用 `LIST_TABLES()` 函数来获取数据表列表。以下是函数的定义和参数说明：

```python
def LIST_TABLES(app_token=None, user_access_token=None, page_size=None, page_token=None, config_file=None):
    # 函数体...

# 使用示例
response_body = LIST_TABLES(app_token, user_access_token, page_size, page_token, config_file)
```

- `app_token`：飞书应用的唯一标识符 (app token)。如果未提供，将从配置文件中获取默认值。
- `user_access_token`：用户访问令牌 (user access token)。如果未提供，将从配置文件中获取默认值。
- `page_size`：分页大小，指定每页返回的数据表数量。如果未提供，将从配置文件中获取默认值。
- `page_token`：分页标记，用于获取下一页数据表列表。如果未提供，将从配置文件中获取默认值。
- `config_file`：配置文件路径，指定配置文件的位置。默认

为 "feishu-config.ini"。

## 设计思路

LIST_TABLES.py 的设计思路是通过飞书多维表格 API 来获取数据表列表。它使用 HTTP GET 请求访问 API，并通过认证信息和参数来定制请求。以下是设计思路的概述：

1. 读取配置文件：首先，脚本会读取配置文件（默认为 "feishu-config.ini"）以获取默认的 app_token、user_access_token、page_token 和 page_size 值。

2. 解析命令行参数：如果使用命令行方式运行脚本，它会解析命令行参数并覆盖配置文件中的默认值。

3. 构造请求：根据提供的参数，脚本会构造包含认证信息和查询参数的请求 URL 和请求头。

4. 发起请求：使用 Python 的 requests 库发送 HTTP GET 请求，并获取响应体。

5. 解析响应：将响应体解析为 JSON 格式，并返回数据表列表。

## 输入输出

### 输入

LIST_TABLES.py 脚本接受以下参数作为输入：

- `app_token`：飞书应用的唯一标识符 (app token)。
- `user_access_token`：用户访问令牌 (user access token)。
- `page_size`：分页大小，指定每页返回的数据表数量。
- `page_token`：分页标记，用于获取下一页数据表列表。
- `config_file`：配置文件路径，指定配置文件的位置。

如果这些参数未提供，则脚本将尝试从配置文件中获取默认值。

### 输出

LIST_TABLES.py 脚本的输出是一个 JSON 格式的数据表列表。它包含了每个数据表的详细信息，如数据表的名称、ID、创建时间等。（具体取决于飞书API）

以下是示例输出：

```json
{
    "tables": [
        {
            "table_id": "tbl123456789",
            "name": "Table 1",
            "created_at": "2023-06-01T12:00:00Z",
            "updated_at": "2023-06-02T10:00:00Z"
        },
        {
            "table_id": "tbl987654321",
            "name": "Table 2",
            "created_at": "2023-06-03T14:00:00Z",
            "updated_at": "2023-06-04T11:30:00Z"
        }
    ],
    "page_token": "tblsRc9GRRXKqhvW"
}
```

输出是一个包含数据表列表和分页标记的 JSON 对象。

## 示例

以下是使用 LIST_TABLES.py 脚本的示例：

```bash
$ python LIST_TABLES.py --app_token appbcbWCzen6D8dezhoCH2RpMAh --user_access_token u-7f1bcd13fc57d46bac21793a18e560 --page_size 10 --page_token tblsRc9GRRXKqhvW --config_file feishu-config.ini
```

上述命令会使用指定的参数来获取数据表列表，并将结果打印为 JSON 格式的输出。

```python
from LIST_TABLES import LIST_TABLES

app_token = "appbcbWCzen6D8dezhoCH2RpMAh"
user_access_token = "u-7f1bcd13fc57d46bac21793a18e560"
page_size = 10
page_token = "tblsRc9GRRXKqhvW"
config_file = "feishu-config.ini"

response_body = LIST_TABLES(app_token, user_access_token, page_size, page_token, config_file)
print(json.dumps(response_body, indent=4))
```

