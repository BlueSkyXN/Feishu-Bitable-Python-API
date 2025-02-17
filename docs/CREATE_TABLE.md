# CREATE_TABLE.py 使用文档

该程序 `CREATE_TABLE.py` 是使用 Python 语言编写的，用于在多维表格中创建新的数据表。它通过调用 Feishu API 实现数据表的创建，并可以自定义表格名称、默认视图名称和字段配置。

参考官方API文档 [新增一个数据表](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table/create)

## 目录

- [设计思路](#设计思路)
- [输入参数](#输入参数)
  - [CMD 模式](#cmd-模式)
  - [函数模式](#函数模式)
- [输出结果](#输出结果)
- [使用示例](#使用示例)
  - [直接调用](#直接调用)
  - [命令行使用](#命令行使用)
  - [请求体示例](#请求体示例)
  - [响应体示例](#响应体示例)

## 设计思路

整个程序的设计思路如下：

1. 读取配置文件 `feishu-config.ini` 或指定的配置文件，获取访问令牌。
2. 访问令牌既可以是用户身份的访问令牌（user_access_token）,也可以是应用身份的访问令牌（tenant_access_token）。
3. 如果访问令牌未提供输入参数，则从配置文件中获取相应的值。优先使用应用身份的访问令牌(confing文件内的app_access_token)。
4. 对于文件夹 token，可通过以下两种方式获取文件夹的 token：文件夹的 URL：https://sample.feishu.cn/drive/folder/fldbcO1UuPz8VwnpPx5a92abcef；调用开放平台接口获取：
5. 如果未提供表格名称，则默认生成一个带有当前日期时间戳的名称。
6. 构建 API 请求的 URL 和请求头。
7. 创建新的数据表，将表格名称、文件夹token作为请求体的参数。
8. 发送请求并返回创建数据表的结果。

## 输入参数

### CMD 模式

该程序支持的输入参数如下：

- `--access_token`：访问令牌
- `--table_name`：表格的名称
- `--folder_token`：目标文件夹token

### 函数模式

- `access_token`：访问令牌
- `table_name`：表格的名称，默认为带有当前日期时间戳的名称
- `folder_token`：目标文件夹token
- `config_file`：配置文件路径，默认为 "feishu-config.ini"

## 使用示例

您可以按照以下方式来使用 `CREATE_TABLE.py`:

### 直接调用

```python
from CREATE_TABLE import CREATE_TABLE

access_token = "YOUR_ACCESS_TOKEN"  # 应用的访问令牌
table_name = "新建数据表"  # 表格的名称
folder_token = "YourFolderToken" # 目标文件夹token

CREATE_TABLE(access_token, table_name, folder_token)
```

### 命令行使用

在命令行中运行以下命令来创建新的数据表：

```
python CREATE_TABLE.py --access_token YOUR_ACCESS_TOKEN --table_name "新建数据表" --folder_token "YourFolderToken" --fields_file /path/to/fields.ini
```

请注意，在运行程序之前，确保您已替换示例代码中的 `YOUR_ACCESS_TOKEN`、`folder_token`等为实际的访问令牌、表格的名称和字段配置文件的路径。

### 请求体示例
```json
{
    "title":"sales sheet",
    "folder_token":"fldbcO1UuPz8VwnpPx5a92abcef"
}

### 响应体示例
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "spreadsheet": {
            "title": "Sales sheet",
            "folder_token": "fldbcO1UuPz8VwnpPx5a92abcef",
            "url": "https://example.feishu.cn/sheets/Iow7sNNEphp3WbtnbCscPqabcef",
            "spreadsheet_token": "Iow7sNNEphp3WbtnbCscPqabcef"
        }
    }
}
```