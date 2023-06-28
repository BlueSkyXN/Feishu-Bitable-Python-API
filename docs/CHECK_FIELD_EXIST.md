# CHECK_FIELD_EXIST.py 使用文档

该程序 `CHECK_FIELD_EXIST.py` 是使用 Python 语言编写的，用于检查飞书表格中的字段是否存在，并在不存在时创建新字段。

## 目录

- [设计思路](#设计思路)
- [函数签名](#函数签名)
- [输入参数](#输入参数)
- [函数模式示例](#函数模式示例)
- [命令行模式示例](#命令行模式示例)

## 设计思路

整个程序的设计思路如下：

1. 从配置文件或函数参数中获取相关配置，如应用的访问令牌、表格 ID、视图 ID 等。
2. 使用 `LIST_FIELDS` 函数获取飞书表格中的字段列表。
3. 从 CSV 文件中读取字段列表。
4. 对比字段列表，检查每个需要检查的字段是否在飞书字段列表中。
5. 如果字段不存在于飞书字段列表中，则调用 `CREATE_FIELD` 函数创建新的字段。
6. 在创建字段后，打印成功信息。

## 函数签名

```python
def CHECK_FIELD_EXIST(app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, csv_file=None, config_file=None):
```

## 输入参数

- `app_token` (str, optional): 飞书应用的访问令牌。如果未提供，将从配置文件中获取。
- `table_id` (str, optional): 飞书表格的唯一标识符。如果未提供，将从配置文件中获取。
- `view_id` (str, optional): 飞书视图的唯一标识符。如果未提供，将从配置文件中获取。
- `page_token` (str, optional): 分页查询的页标识符。如果未提供，将从配置文件中获取。
- `page_size` (int, optional): 分页查询的页大小。如果未提供，将从配置文件中获取，默认为 100。
- `csv_file` (str, optional): CSV 文件的路径。如果未提供，将从配置文件中获取。
- `config_file` (str, optional): 配置文件的路径。如果未提供，默认为 `feishu-config.ini`。

## 函数模式示例

您可以按照以下方式使用 `CHECK_FIELD_EXIST` 函数：

```python
from CHECK_FIELD_EXIST import CHECK_FIELD_EXIST

app_token = "YOUR_APP_TOKEN"
table_id = "YOUR_TABLE_ID"
view_id = "YOUR_VIEW_ID"
page_token = "YOUR_PAGE_TOKEN"
page_size = 100
csv_file = "input.csv"
config_file = "feishu-config.ini"

CHECK_FIELD_EXIST(
    app_token=app_token,
    table_id=table_id,
    view_id=view_id,
    page_token=page_token,
    page_size=page_size,
    csv_file=csv_file,
    config_file=config_file
)
```

请根据实际情况提供正确的参数值。如果某个参数未提供，程序将尝试从配置文件中获取相应的值。如果在配置文件中也未找到对应的值，则程序将使用默认值。

注意：为了使用 `CHECK_FIELD_EXIST

` 函数，您需要确保 `LIST_FIELDS` 和 `CREATE_FIELD` 函数已经正确定义并可用。

## 命令行模式示例

您也可以使用命令行模式运行 `CHECK_FIELD_EXIST.py` 程序。在命令行中执行以下命令：

```bash
python CHECK_FIELD_EXIST.py --app_token YOUR_APP_TOKEN --table_id YOUR_TABLE_ID --view_id YOUR_VIEW_ID --page_token YOUR_PAGE_TOKEN --page_size 100 --csv_file input.csv --config_file feishu-config.ini
```

请根据实际情况提供正确的参数值。如果某个参数未提供，程序将尝试从配置文件中获取相应的值。如果在配置文件中也未找到对应的值，则程序将使用默认值。

注意：在命令行模式下，您需要确保相关的依赖项已经安装，并且程序文件和配置文件位于当前工作目录中。