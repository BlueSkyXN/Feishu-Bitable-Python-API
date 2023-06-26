# GET_INFO_FROM_URL

## 简介

`GET_INFO_FROM_URL` 是一个用于从 URL 中提取信息的 Python 程序。它可以解析 URL，并提取出其中的 app_token、table_id 和 view_id。

## 目录
- [简介](#简介)
- [使用指南](#使用指南)
  - [安装依赖](#安装依赖)
  - [使用方法](#使用方法)
- [输入输出](#输入输出)
  - [GET_INFO_FROM_URL](#get_info_from_url)
  - [GET_INFO_FROM_URL_JSON](#get_info_from_url_json)
  - [GET_APPTOKEN_FROM_URL](#get_apptoken_from_url)
  - [GET_TABLEID_FROM_URL](#get_tableid_from_url)
  - [GET_VIEWID_FROM_URL](#get_viewid_from_url)
- [示例](#示例)
  - [GET_INFO_FROM_URL 示例](#get_info_from_url-示例)
  - [GET_INFO_FROM_URL_JSON 示例](#get_info_from_url_json-示例)
  - [GET_APPTOKEN_FROM_URL 示例](#get_apptoken_from_url-示例)
  - [GET_TABLEID_FROM_URL 示例](#get_tableid_from_url-示例)
  - [GET_VIEWID_FROM_URL 示例](#get_viewid_from_url-示例)
- [设计思路](#设计思路)

## 使用指南

### 安装依赖

在运行 `GET_INFO_FROM_URL` 之前，需要确保你的环境已安装以下依赖：

- `argparse`: 用于解析命令行参数
- `urllib.parse`: 用于解析 URL
- `json`: 用于处理 JSON 数据

### 使用方法

运行 `GET_INFO_FROM_URL` 的示例命令格式如下：

```shell
python GET_INFO_FROM_URL.py -u <url>
```

或

```shell
python GET_INFO_FROM_URL.py --url <url>
```

其中，`<url>` 是要提取信息的 URL。

## 输入输出

好的，以下是对每个函数的输入和输出的详细说明：

### GET_INFO_FROM_URL

**函数说明**：从 URL 中提取信息并返回包含提取的信息的字典。

**输入**：
- `url`（字符串）：要提取信息的 URL。

**输出**：
- `info`（字典）：包含提取的信息的字典，包括以下键值对：
  - `"app_token"`: 提取的 app_token。
  - `"table_id"`: 提取的 table_id。
  - `"view_id"`: 提取的 view_id。

### GET_INFO_FROM_URL_JSON

**函数说明**：从 URL 中提取信息并返回以 JSON 格式表示的信息字典。

**输入**：
- `url`（字符串）：要提取信息的 URL。

**输出**：
- `json_info`（字符串）：以 JSON 格式表示的信息字典。

### GET_APPTOKEN_FROM_URL

**函数说明**：从 URL 中提取 app_token 并返回。

**输入**：
- `url`（字符串）：要提取 app_token 的 URL。

**输出**：
- `app_token`（字符串）：提取的 app_token。

### GET_TABLEID_FROM_URL

**函数说明**：从 URL 中提取 table_id 并返回。

**输入**：
- `url`（字符串）：要提取 table_id 的 URL。

**输出**：
- `table_id`（字符串）：提取的 table_id。

### GET_VIEWID_FROM_URL

**函数说明**：从 URL 中提取 view_id 并返回。

**输入**：
- `url`（字符串）：要提取 view_id 的 URL。

**输出**：
- `view_id`（字符串）：提取的 view_id。

以上是对每个函数的详细输入和输出说明。

如果你有更多的问题，欢迎继续提问。


## 示例

以下是对各个函数的使用示例：

### GET_INFO_FROM_URL 示例

```python
url = "https://example.com/base/VwGhbo65BaYLaOsSz1nciWc5ncb?table=tblzDsYuQkXfoy9e&view=vewAgGXuqf"
info = GET_INFO_FROM_URL(url)
print("获取的信息字典:")
print(info)
```

输出：
```
获取的信息字典:
{'app_token': 'VwGhbo65BaYLaOsSz1nciWc5ncb', 'table_id': 'tblzDsYuQkXfoy9e', 'view_id': 'vewAgGXuqf'}
```

### GET_INFO_FROM_URL_JSON 示例

```python
url = "https://example.com/base/VwGhbo65BaYLaOsSz1nciWc5ncb?table=tblzDsYuQkXfoy9e&view=vewAgGXuqf"
json_info = GET_INFO_FROM_URL_JSON(url)
print("以 JSON 格式表示的信息字典:")
print(json_info)
```

输出：
```
以 JSON 格式表示的信息字典:
{"app_token": "VwGhbo65BaYLaOsSz1nciWc5ncb", "table_id": "tblzDsYuQkXfoy9e", "view_id": "vewAgGXuqf"}
```

### GET_APPTOKEN_FROM_URL 示例

```python
url = "https://example.com/base/VwGhbo65BaYLaOsSz1nciWc5ncb?table=tblzDsYuQkXfoy9e&view=vewAgGXuqf"
app_token = GET_APPTOKEN_FROM_URL(url)
print("提取的 app_token:")
print(app_token)
```

输出：
```
提取的 app_token:
VwGhbo65BaYLaOsSz1nciWc5ncb
```

### GET_TABLEID_FROM_URL 示例

```python
url = "https://example.com/base/VwGhbo65BaYLaOsSz1nciWc5ncb?table=tblzDsYuQkXfoy9e&view=vewAgGXuqf"
table_id = GET_TABLEID_FROM_URL(url)
print("提取的 table_id:")
print(table_id)
```

输出：
```
提取的 table_id:
tblzDsYuQkXfoy9e
```

### GET_VIEWID_FROM_URL 示例

```python
url = "https://example.com/base/VwGhbo65BaYLaOsSz1nciWc5ncb?table=tblzDsYuQkXfoy9e&view=vewAgGXuqf"
view_id = GET_VIEWID_FROM_URL(url)
print("提取的 view_id:")
print(view_id)
```

输出：
```
提取的 view_id:
vewAgGXuqf
```

以上是对各个函数的使用示例。你可以根据需要选择相应的函数进行调用，并查看输出结果。

如果你有更多的问题，欢迎继续提问。

## 设计思路

1. 解析 URL：使用 `urllib.parse.urlparse()` 函数解析输入的 URL，获取其各个组成部分。
2. 提取参数：使用 `urllib.parse.parse_qs()` 函数提取 URL 的查询参数，并将其存储在一个字典中。
3. 获取 app_token：从 URL 的路径中提取 app_token，即路径的最后一部分。
4. 获取 table_id 和 view_id：从查询参数中获取 table_id 和 view_id，如果不存在，则将它们设为 `None`。
5. 构建信息字典：将 app_token、table_id 和 view_id 存储在一个字典中。
6. 返回结果：返回提取的信息字典。

