# WRITE_FIELD_INFO.py 文档

`WRITE_FIELD_INFO.py` 是一个用于将字段信息写入配置文件的工具。它提供了一个名为 `WRITE_FIELD_INFO()` 的函数，可以通过给定的字段名称或字段 ID 查询字段信息，并将字段信息写入配置文件。

## 设计思路

主要有以下几个函数构成：

1. `WRITE_FIELD_INFO(field_name=None, field_id=None,...)`: 根据字段名称或字段 ID 查询字段信息，并将字段信息写入配置文件。
2. `WRITE_FIELD_INFO_CMD()`: 命令行调用函数，用于将字段信息写入配置文件。

函数中的参数主要有：

- `field_name`：要查询的字段名称。
- `field_id`：要查询的字段 ID。
- `app_token`：应用的唯一标识符 (app token)。
- `table_id`：表格的唯一标识符 (table ID)。
- `view_id`：视图的唯一标识符 (view ID)。
- `page_token`：分页标记，用于获取下一页的字段列表。
- `page_size`：页面大小，指定每页返回的字段数量。
- `config_file`：配置文件路径，指定配置文件的位置。

## 使用示例

以下是使用 `WRITE_FIELD_INFO.py` 的示例：

```bash
python WRITE_FIELD_INFO.py --name 字段名称
```

或

```bash
python WRITE_FIELD_INFO.py --id 字段ID
```

```python
from WRITE_FIELD_INFO import WRITE_FIELD_INFO

field_name = "字段名称"
field_id = "字段ID"
app_token = "应用token"
table_id = "表格ID"
view_id = "视图ID"
page_token = "分页标记"
page_size = "页面大小"
config_file = "配置文件路径"

WRITE_FIELD_INFO(field_name, field_id, app_token, table_id, view_id, page_token, page_size, config_file)
```

请注意，`app_token`、`table_id` 和 `view_id` 是必需的参数。如果未设置这些参数，脚本将无法运行。

## 输入输出

### 输入

`WRITE_FIELD_INFO.py` 脚本接受以下参数作为输入：

- `field_name`：要查询的字段名称。
- `field_id`：要查询的字段 ID。
- `app_token`：飞书应用的唯一标识符 (app token)。
- `table_id`：表格的唯一标识符 (table ID)。
- `view_id`：视图的唯一标识符 (view ID)。
- `page_token`：分页标记，用于获取下一页的字段列表。
- `page_size`：页面大小，指定每页返回的字段数量。
- `config_file`：配置文件路径，指定配置文件的位置。

### 输出

该工具将字段信息写入配置文件。

## 示例

以下是使用 `WRITE_FIELD_INFO.py` 脚本的示例：

```bash
python WRITE_FIELD_INFO.py --name 字段名称
```

或

```bash
python WRITE_FIELD_INFO.py --

id 字段ID
```

请注意，以上示例是通过命令行方式运行脚本来将字段信息写入配置文件。

```python
from WRITE_FIELD_INFO import WRITE_FIELD_INFO

field_name = "字段名称"
field_id = "字段ID"
app_token = "应用token"
table_id = "表格ID"
view_id = "视图ID"
page_token = "分页标记"
page_size = "页面大小"
config_file = "配置文件路径"

WRITE_FIELD_INFO(field_name, field_id, app_token, table_id, view_id, page_token, page_size, config_file)
```

请注意，以上示例是通过导入方式调用函数来将字段信息写入配置文件。