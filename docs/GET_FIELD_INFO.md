# GET_FIELD_INFO.py 文档

`GET_FIELD_INFO.py` 是一个用于通过字段名称或字段ID查询字段相关信息的工具。它提供了一个名为 `GET_FIELD_INFO()` 的函数，可以获取字段的名称、字段ID、字段类型等信息。该工具还支持通过配置文件自定义参数，提供了更灵活的使用方式

## 目录

- [使用指南](#使用指南)
- [设计思路](#设计思路)
- [输入输出](#输入输出)
- [示例](#示例)

## 使用指南

### 命令行方式

通过命令行参数直接运行 `GET_FIELD_INFO.py` 脚本可以获取字段信息。以下是命令行参数的说明：

```bash
python GET_FIELD_INFO.py --name <字段名称> --id <字段ID> --app_token <应用token> --table_id <表格ID> --view_id <视图ID> --page_token <分页标记> --page_size <页面大小> --config_file <配置文件路径>
```

- `--name`：指定要查询的字段名称。
- `--id`：指定要查询的字段ID。
- `--app_token`：设置应用的token进行身份验证。
- `--table_id`：设置要查询的表格ID。
- `--view_id`：设置要查询的视图ID。
- `--page_token`：设置分页标记，用于获取下一页的字段列表。
- `--page_size`：设置页面大小，指定每页返回的字段数量。
- `--config_file`：配置文件路径，指定配置文件的位置。默认为 "feishu-config.ini"。

### 导入模块方式

您也可以将 `GET_FIELD_INFO.py` 脚本导入为模块，并使用 `GET_FIELD_INFO()` 函数来获取字段信息。以下是函数定义和参数说明：

```python
def GET_FIELD_INFO(field_name=None, field_id=None, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
    # 函数体...

# 使用示例
field_info = GET_FIELD_INFO(field_name, field_id, app_token, table_id, view_id, page_token, page_size, config_file)
print(field_info)
```

- `field_name`：字段名称。
- `field_id`：字段ID。
- `app_token`：应用的token。如果未提供，将从配置文件中获取默认值。
- `table_id`：表格ID。如果未提供，将从配置文件中获取默认值。
- `view_id`：视图ID。如果未提供，将从配置文件中获取默认值。
- `page_token`：分页标记。如果未提供，将从配置文件中获取默认值。
- `page_size`：页面大小。如果未提供，将从配置文件中获取默认值。
- `config_file`：配置文件路径。默认为 "feishu-config.ini"。

## 设计思路

`GET_FIELD_INFO.py` 的设计思路

是通过飞书多维表格 API 来查询字段信息。它使用 HTTP GET 请求访问 API，并根据提供的字段名称或字段ID来定制请求。以下是设计思路的概述：

1. 读取配置文件：首先，脚本会读取配置文件（默认为 "feishu-config.ini"）以获取默认的 app_token、table_id、view_id、page_token 和 page_size 值。

2. 解析命令行参数：如果使用命令行方式运行脚本，它会解析命令行参数并覆盖配置文件中的默认值。

3. 构造请求：根据提供的参数，脚本会构造包含认证信息和查询参数的请求 URL 和请求头。

4. 发起请求：使用 Python 的 requests 库发送 HTTP GET 请求，并获取响应体。

5. 解析响应：将响应体解析为 JSON 格式，并返回字段信息。

## 输入输出

### 输入

`GET_FIELD_INFO.py` 脚本接受以下参数作为输入：

- `field_name`：要查询的字段名称。
- `field_id`：要查询的字段ID。
- `app_token`：飞书应用的唯一标识符 (app token)。如果未提供，将从配置文件中获取默认值。
- `table_id`：表格的唯一标识符 (table ID)。如果未提供，将从配置文件中获取默认值。
- `view_id`：视图的唯一标识符 (view ID)。如果未提供，将从配置文件中获取默认值。
- `page_token`：分页标记，用于获取下一页的字段列表。如果未提供，将从配置文件中获取默认值。
- `page_size`：页面大小，指定每页返回的字段数量。如果未提供，将从配置文件中获取默认值。
- `config_file`：配置文件路径，指定配置文件的位置。

### 输出

`GET_FIELD_INFO.py` 脚本的输出是一个包含字段信息的字典。字段信息包括字段名称、字段ID、字段类型等（具体取决于飞书 API 返回的字段信息）。

以下是示例输出：

```python
{
    "field_id": "field123",
    "field_name": "字段名称",
    "field_type": "字段类型",
    ...
}
```

## 示例

以下是使用 `GET_FIELD_INFO.py` 脚本的示例：

```bash
python GET_FIELD_INFO.py --name 字段名称
```

或

```bash
python GET_FIELD_INFO.py --id 字段ID
```

```python
from GET_FIELD_INFO import GET_FIELD_INFO

field_name = "字段名称"
field_id = "字段ID"
app_token = "应用token"
table_id = "表格ID"
view_id = "视图ID"
page_token = "分页标记"
page_size = "页面大小"
config_file = "配置文件路径"

field_info = GET_FIELD_INFO(field_name, field_id, app_token, table_id, view_id, page_token, page_size, config_file)
print(field_info)
```

请注意，`app_token`、`table_id` 和 `view_id` 是必需的参数。如果未设置

这些参数，脚本将无法运行。