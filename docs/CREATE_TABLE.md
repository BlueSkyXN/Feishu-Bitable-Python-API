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

1. 读取配置文件 `feishu-config.ini` 或指定的配置文件，获取用户访问令牌（user_access_token）和应用的访问令牌（app_token）。
2. 如果未提供输入参数，则从配置文件中获取相应的值。
3. 如果未提供表格名称，则默认生成一个带有当前日期时间戳的名称。
4. 如果未提供默认视图名称，则默认使用 "默认的表格视图"。
5. 如果未提供字段配置，则根据字段配置文件生成默认字段。
6. 构建 API 请求的 URL 和请求头。
7. 创建新的数据表，将表格名称、默认视图名称和字段配置作为请求体的参数。
8. 发送请求并返回创建数据表的结果。

非常抱歉，我遗漏了直接函数模式的输入参数说明。以下是修正后的文档：

## 输入参数

### CMD 模式

该程序支持的输入参数如下：

- `--app_token`：应用的访问令牌
- `--table_name`：表格的名称
- `--default_view_name`：默认的表格视图名称
- `--fields_file`：字段配置文件的路径

### 函数模式

- `app_token`：应用的访问令牌
- `table_name`：表格的名称，默认为带有当前日期时间戳的名称
- `default_view_name`：默认的表格视图名称，默认为 "默认的表格视图"
- `fields`：字段配置列表，默认根据字段配置文件生成默认字段
- `config_file`：配置文件路径，默认为 "feishu-config.ini"
- `fields_file`：字段配置文件路径，默认为 "feishu-field.ini"

## 使用示例

您可以按照以下方式来使用 `CREATE_TABLE.py`：

### 直接调用

```python
from CREATE_TABLE import CREATE_TABLE

app_token = "YOUR_APP_TOKEN"  # 应用的访问令牌
table_name = "新建数据表"  # 表格的名称
default_view_name = "默认的表格视图"  # 默认的表格视图名称
fields = [
    {
        "field_name": "KEY",
        "type": 1
    }
]  # 字段配置

CREATE_TABLE(app_token, table_name, default_view_name, fields)
```

### 命令行使用

在命令行中运行以下命令来创建新的数据表：

```
python CREATE_TABLE.py --app_token YOUR_APP_TOKEN --table_name "新建数据表" --default_view_name "默认的表格视图" --fields_file /path/to/fields.ini
```

请注意，在运行程序之前，确保您已替换示例代码中的 `YOUR_APP_TOKEN`、`新建数据表`、`默认的表格视图` 和 `/path/to/fields.ini` 为实际的应用的访问令牌、表格的名称、默认的表格视图名称和字段配置文件的路径。

### 请求体示例
```json
{
    "table":{
        "name":"数据表名称",
        "default_view_name":"默认的表格视图",
        "fields":[
            {
                "field_name":"多行文本",
                "type":1
            }
        ]
    }
}

```

### 响应体示例
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "table_id": "tblDBTWm6Es84d8c",
        "default_view_id": "vewUuKOz2R",
        "field_id_list": [
            "fldhr2hBEA"
        ]
    }
}
```