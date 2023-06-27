# CREATE_FIELD.py 使用文档

该程序 `CREATE_FIELD.py` 是使用 Python 语言编写的，用于在多维表格中创建新字段。它通过调用 Feishu API 实现字段的创建。

参考官方API文档 [新增字段](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-field/create)

## 目录

- [设计思路](#设计思路)
- [输入参数](#输入参数)
  - [CMD 模式](#cmd-模式)
- [使用示例](#使用示例)
  - [直接调用](#直接调用)
  - [命令行使用](#命令行使用)

## 设计思路

整个程序的设计思路如下：

1. 读取配置文件 `feishu-config.ini` 或指定的配置文件，获取应用的令牌（app_token）、数据表的唯一标识符（table_id）和用户访问令牌（user_access_token）。
2. 如果未提供输入参数，则从配置文件中获取相应的值。
3. 构建 API 请求的 URL 和请求头。
4. 创建新字段，将字段名称和字段类型作为请求体的参数。
5. 发送请求并打印创建字段的结果。

## 输入参数

### CMD 模式

该程序支持的输入参数如下：

- `-f/--field`：字段名，必需参数
- `--field_type`：字段类型，默认为1
- `--app_token`：多维表格的唯一标识符 app_token
- `--table_id`：多维表格数据表的唯一标识符 table_id
- `--config_file`：配置文件路径，默认为 `feishu-config.ini`

## 使用示例

您可以按照以下方式来使用 `CREATE_FIELD.py`：

### 直接调用

```python
from CREATE_FIELD import CREATE_FIELD

field_name = "字段名"
field_type = 1  # 字段类型，默认为1
app_token = "YOUR_APP_TOKEN"  # 多维表格的唯一标识符 app_token
table_id = "YOUR_TABLE_ID"  # 多维表格数据表的唯一标识符 table_id
config_file = "feishu-config.ini"  # 配置文件路径

CREATE_FIELD(field_name, field_type, app_token, table_id, config_file)
```

### 命令行使用

在命令行中运行以下命令来创建新字段：

```
python CREATE_FIELD.py -f FIELD_NAME --field_type FIELD_TYPE --app_token YOUR_APP_TOKEN --table_id YOUR_TABLE_ID --config_file /path/to/config.ini
```

请注意，在运行程序之前，确保您已替换示例代码中的 `FIELD_NAME`、`FIELD_TYPE`、`YOUR_APP_TOKEN` 和 `YOUR_TABLE_ID` 为实际的字段名、字段类型、多维表格的唯一标识符 app_token 和数据表的唯一标识符 table_id。

