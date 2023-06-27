# GET_RECORD.py 使用文档

该程序 `GET_RECORD.py` 是使用 Python 语言编写的，通过调用飞书 API 实现从指定数据表中获取记录的详细信息。

参考官方API文档 [检索记录](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/get)

## 目录

- [设计思路](#设计思路)
- [输入参数](#输入参数)
  - [CMD 模式](#cmd-模式)
  - [函数模式](#函数模式)
- [输出结果](#输出结果)
- [使用示例](#使用示例)
  - [直接调用](#直接调用)
  - [命令行使用](#命令行使用)

## 设计思路

整个程序的设计思路如下：

1. 读取配置文件（默认为 `feishu-config.ini`）并解析出相关的配置项。
2. 根据输入的参数或配置文件中的默认值构造请求的 URL 和头部信息。
3. 使用 `requests` 库发起 GET 请求获取记录的详细信息。
4. 将响应体解析为 JSON 格式并返回。

## 输入参数

### CMD 模式

该程序支持的输入参数如下：

- `--app_token`：可选参数，飞书应用的令牌
- `--table_id`：可选参数，数据表的 ID
- `--record_id`：可选参数，记录的 ID
- `--config_file`：可选参数，配置文件路径，默认为 `feishu-config.ini`

### 函数模式

- `app_token`：可选参数，飞书应用的令牌。如果不指定，则从配置文件中获取。
- `table_id`：可选参数，数据表的 ID。如果不指定，则从配置文件中获取。
- `record_id`：可选参数，记录的 ID。如果不指定，则从配置文件中获取。
- `config_file`：可选参数，配置文件路径，默认为 `feishu-config.ini`

## 输出结果

该程序的输出结果为记录的详细信息，以 JSON 格式返回。

您可以按照以下方式来调用该函数：

```python
response_body = GET_RECORD(app_token=None, table_id=None, record_id=None, config_file=None)
```

## 使用示例

您可以按照以下方式来使用 `GET_RECORD.py`：

### 直接调用

```python
import json
from GET_RECORD import GET_RECORD

app_token = "your_app_token"
table_id = "your_table_id"
record_id = "your_record_id"

response_body = GET_RECORD(app_token, table_id, record_id)
print(json.dumps(response_body, indent=4, ensure_ascii=False))
```

### 命令行使用

您可以通过命令行方式使用 `GET_RECORD.py`，示例如下：

1. 使用默认的配置文件和参数获取记录：

```
python GET_RECORD.py
```

2. 指定飞书应用令牌、数据表 ID 和记录 ID 获取记录：

```
python GET_RECORD.py --app_token your_app_token --table_id your_table_id --record_id your_record_id
```

3. 通过指定配置文件路径来获取记录：

```
python GET_RECORD.py --config_file /path/to/config.ini
```

请注意，确保您已正确配置配置文件中的相关信息，以及提供正确的飞书应用令牌、数据表 ID 和记录 ID。