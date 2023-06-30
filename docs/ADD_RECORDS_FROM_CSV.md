# ADD_RECORDS_FROM_CSV.py 使用指南

## 简介

ADD_RECORDS_FROM_CSV.py 是一个 Python 脚本，用于从 CSV 文件中读取数据，并将这些数据添加到飞书表格中。该脚本使用飞书开放平台的 API，通过批量创建记录的方式将数据添加到指定的表格中。

## 设计思路

该脚本的主要功能是通过读取 CSV 文件和配置文件，构建请求体，然后发送请求到飞书的 API，将 CSV 文件中的数据添加到飞书表格中。在发送请求之前，脚本会检查记录数量，如果记录数量超过450，则会进行分片处理，每次发送450条记录。

如果在添加记录的过程中出现 "FieldNameNotFound" 错误，脚本会尝试修复并重试。如果重试失败，脚本会抛出异常。

1. 读取配置文件：程序首先读取配置文件 `feishu-config.ini` 中的参数，包括用户访问令牌、应用令牌、数据表 ID 等。
2. 构建请求体：调用 `BUILD_FIELD` 函数来构建请求体，该函数从 CSV 文件中提取记录并根据字段配置文件构建相应的数据结构。
3. 分批处理：如果记录数量超过 450 条，程序将对记录进行分批处理，每次发送 450 条记录。
4. 发送请求：程序使用 `requests` 库向 Feishu API 发送请求，将记录添加到数据表中。
5. 处理响应：程序检查响应的状态和结果信息，并根据情况进行相应的处理，如处理字段不存在的错误。
6. 保存请求和响应信息：如果启用了保存功能，程序将请求体和响应体保存到字段配置文件中。


## 使用示例

以下是一个使用示例：

```python
from ADD_RECORDS_FROM_CSV import ADD_RECORDS_FROM_CSV

ADD_RECORDS_FROM_CSV(
    app_token='your_app_token',
    table_id='your_table_id',
    view_id='your_view_id',
    page_token='your_page_token',
    page_size=100,
    csv_file='your_csv_file_path',
    config_file='your_config_file_path',
    field_file='your_field_file_path'
)
```

在这个示例中，你需要将 `'your_app_token'`、`'your_table_id'`、`'your_view_id'`、`'your_page_token'`、`'your_csv_file_path'`、`'your_config_file_path'` 和 `'your_field_file_path'` 替换为你自己的值。

## 输入参数

ADD_RECORDS_FROM_CSV 函数接受以下参数：

- `app_token` (可选): Feishu 应用的 app_token，如果未提供，将从配置文件中读取。
- `table_id` (可选): 要添加记录的数据表的 ID，如果未提供，将从配置文件中读取。
- `view_id` (可选): 要添加记录的视图的 ID，如果未提供，将从配置文件中读取。
- `page_token` (可选): 分页处理时的页标记，用于继续上次的操作，如果未提供，将从配置文件中读取。
- `page_size` (可选): 每个批次发送的记录数量，如果未提供，将从配置文件中读取。
- `csv_file` (可选): 包含要添加记录的 CSV 文件的路径，如果未提供，将从配置文件中读取。
- `config_file` (可选): 配置文件的路径，默认为 `feishu-config.ini`。
- `field_file` (可选): 字段配置文件的路径，默认为 `feishu-field.ini`。

如果没有提供这些参数，函数会从默认的配置文件中读取。

## 输出

函数会打印出请求的 URL，发送请求后的响应状态，以及是否成功创建表格记录的信息。如果在创建记录的过程中出现错误，函数会打印出错误信息。

如果启用了 `ENABLE_ADD_RECORDS`，函数还会将请求体和响应体保存到字段配置文件中。


## 配置文件

在运行 `ADD_RECORDS_FROM_CSV.py` 之前，需要准备一个配置文件 `feishu-config.ini`，用于存储必要的参数信息。请确保配置文件与 `ADD_RECORDS_FROM_CSV.py` 在同一目录下，并按照以下格式进行配置。配置文件是一个 INI 格式的文件，包含以下几个部分：

- `TOKEN`：包含 `user_access_token` 和 `app_token`。
- `ID`：包含 `table_id` 和 `view_id`。
- `FILE_PATH`：包含 `csv_file_path`。
- `ADD_RECORDS`：包含 `page_token` 和 `page_size`。

以下是一个配置文件的示例：

```ini
[TOKEN]
user_access_token = your_user_access_token
app_token = your_app_token

[ID]
table_id = your_table_id
view_id = your_view_id

[FILE_PATH]
csv_file_path = your_csv_file_path

[ADD_RECORDS]
page_token = your_page_token
page_size = your_page_size
```

在这个示例中，你需要将 `'your_user_access_token'`、`'your_app_token'`、`'your_table_id'`、`'your_view_id'`、`'your_csv_file_path'`、`'your_page_token'` 和 `'your_page_size'` 替换为你自己的值。

### 字段配置文件

字段配置文件是一个 INI 格式的文件，用于保存请求体和响应体。如果启用了 `ENABLE_ADD_RECORDS`，函数会将请求体和响应体保存到这个文件中。

以下是一个字段配置文件的示例：

```ini
[ADD_RECORDS_FROM_CSV]
request_body = your_request_body
response_body = your_response_body
```

在这个示例中，你需要将 `'your_request_body'` 和 `'your_response_body'` 替换为你自己的值。

程序会使用字段配置文件 `feishu-field.ini` 来保存请求体和响应体。可以使用以下示例来创建配置文件：

```ini
[ADD_RECORDS_FROM_CSV]
request_body = {}
response_body = {}
```

在程序执行期间，请求体和响应体会被更新并保存到字段配置文件中。

## 注意事项

- 请确保你的 CSV 文件、配置文件和字段配置文件的路径正确，且文件格式正确。
- 请确保你的 app_token、table_id 和 view_id 正确，且你有权限访问对应的表格和视图。
- 请确保你的 page_token 和 page_size 正确，且不超过飞书 API 的限制。
- 如果你的记录数量超过450，函数会自动进行分片处理，每次发送450条记录。如果你的记录数量远远超过450，可能需要花费一些时间来添加所有的记录。
- 如果在添加记录的过程中出现 "FieldNameNotFound" 错误，函数会尝试修复并重试。如果重试失败，函数会抛出异常。请检查你的 CSV 文件和字段配置文件，确保所有的字段都存在。
- 如果启用了 `ENABLE_ADD_RECORDS`，函数会将请求体和响应体保存到字段配置文件中。请确保你有权限写入字段配置文件。