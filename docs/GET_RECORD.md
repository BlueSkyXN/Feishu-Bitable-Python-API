# GET_RECORD.py 使用文档

该程序 `GET_RECORD.py` 是使用 Python 语言编写的，通过调用飞书开放平台 API，获取指定数据表中的记录信息。

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

1. 读取配置文件（默认为 `feishu-config.ini`），并解析出相应的配置项。
2. 构造请求的 URL 和头部信息。
3. 发起 GET 请求，获取指定记录的信息。
4. 返回响应体的 JSON 形式。

## 输入参数

### CMD 模式

该程序支持的输入参数如下：

- `--app_token`：应用令牌，用于访问飞书开放平台的 API。如果不指定，则从配置文件中获取。
- `--table_id`：数据表 ID。如果不指定，则从配置文件中获取。
- `--record_id`：记录 ID。如果不指定，则从配置文件中获取。
- `--user_access_token`：用户访问令牌，用于用户授权访问。如果不指定，则从配置文件中获取。

### 函数模式

- `app_token`：应用令牌，用于访问飞书开放平台的 API。如果不指定，则从配置文件中获取。
- `table_id`：数据表 ID。如果不指定，则从配置文件中获取。
- `record_id`：记录 ID。如果不指定，则从配置文件中获取。
- `user_access_token`：用户访问令牌，用于用户授权访问。如果不指定，则从配置文件中获取。

## 输出结果

该程序返回一个 JSON 对象，包含指定记录的信息。

您可以按照以下方式来调用该函数：

```python
response_body = GET_RECORD(app_token=None, table_id=None, record_id=None, user_access_token=None)
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
user_access_token = "your_user_access_token"

response_body = GET_RECORD(app_token, table_id, record_id, user_access_token)
print(json.dumps(response_body, indent=4))
```

### 命令行使用

1. 使用默认的配置文件和参数，获取记录信息：

```
python GET_RECORD.py
```

2. 通过命令行参数指定应用令牌、数据表 ID、记录 ID 和用户访问令牌，获取记录信息：

```
python GET_RECORD.py --app_token your_app_token --table_id your_table_id --record_id your_record_id --user_access_token your_user_access_token
```

3. 

通过指定配置文件路径来获取记录信息：

```
python GET_RECORD.py --config_file /path/to/config.ini
```

请注意，以上示例中的参数值为示意，实际使用时需要替换为有效的参数值。