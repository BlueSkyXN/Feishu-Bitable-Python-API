# 使用指导 / User Guide

此仓库包含多个脚本，用于处理和操作飞书表格的数据。以下是每个脚本的简要描述。

## GET_INFO_FROM_URL.py

这个脚本用于从给定的URL中提取信息。主要功能是从飞书URL中提取`app_token`、`table_id`和`view_id`三个重要的参数。

### 函数用法

- `EXTRACT_PARAMETERS(url)`: 这个函数接收一个URL作为参数，并从中解析出`app_token`、`table_id`和`view_id`。
- `GET_APPTOKEN_FROM_URL(url)`: 这个函数接收一个URL作为参数，并返回从中提取的`app_token`。
- `GET_TABLEID_FROM_URL(url)`: 这个函数接收一个URL作为参数，并返回从中提取的`table_id`。
- `GET_VIEWID_FROM_URL(url)`: 这个函数接收一个URL作为参数，并返回从中提取的`view_id`。

### 命令行用法

在命令行中使用以下命令运行脚本，并传入一个URL：

```shell
python GET_INFO_FROM_URL.py -u YOUR_URL
```

脚本会打印出提取到的app_token、table_id和view_id。


## WRITE_INFO_FROM_URL.py

这个脚本主要用于将从给定的URL中提取的信息（如`app_token`、`table_id`和`view_id`等）写入到配置文件中。

### 函数用法

- `WRITE_INFO_FROM_URL(url)`: 这个函数接收一个URL作为参数，并将从URL中提取的`app_token`、`table_id`和`view_id`写入到名为'feishu-config.ini'的配置文件中。
- `WRITE_INFO_FROM_URL_CMD()`: 这个函数主要用于解析命令行参数，并调用`WRITE_INFO_FROM_URL(url)`函数，将从URL中提取的信息写入到配置文件中。

### 命令行用法

在命令行中使用以下命令运行脚本，并传入一个URL：

```shell
python WRITE_INFO_FROM_URL.py -u YOUR_URL
```
脚本会将从URL中提取的app_token、table_id和view_id等信息写入到名为'feishu-config.ini'的配置文件中。

## LIST_DATATABLES.py

这个脚本主要用于列出Feishu数据表。可以通过命令行参数或者配置文件传入相关参数。

### 函数用法

- `LIST_DATATABLES(app_token=None, user_access_token=None, page_token=None, page_size=None)`: 这个函数主要用于发起请求，列出Feishu数据表。它接受四个可选参数：`app_token`、`user_access_token`、`page_token`和`page_size`。如果这些参数为空，函数将从名为'feishu-config.ini'的配置文件中读取默认值。

### 命令行用法

在命令行中使用以下命令运行脚本，并传入需要的参数（可选）：

```shell
python LIST_DATATABLES.py --app_token YOUR_APP_TOKEN --user_access_token YOUR_USER_ACCESS_TOKEN --page_token YOUR_PAGE_TOKEN --page_size YOUR_PAGE_SIZE
```
脚本将列出Feishu数据表并将结果以json形式打印出来。

## GET-TABLEID.py

这个脚本主要用于通过数据表的名字来获取其ID。

### 函数用法

- `GET_TABLE_ID(name="数据表")`: 这个函数主要用于通过名字来获取数据表的ID。它接收一个名字作为参数，并返回对应的ID。如果找不到对应的数据表，将返回"NONE"。

### 命令行用法

在命令行中使用以下命令运行脚本，并传入需要的参数（可选）：

```shell
python GET-TABLEID.py -i YOUR_TABLE_NAME
```
脚本将通过数据表的名字来获取其ID，并将结果打印出来。