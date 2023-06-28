# LIST_FIELDS.py 使用指南

`LIST_FIELDS.py` 是一个用于列出飞书表格中的字段的工具。它提供了一个函数 `LIST_FIELDS()`，可以通过给定的飞书配置信息，列出飞书表格中的字段。

参考官方API文档 [列出字段](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-field/list)

## 目录
- [简介](#简介)
- [函数介绍](#函数介绍)
  - [LIST_FIELDS 函数](#list_fields-函数)
  - [LIST_FIELDS_CMD 函数](#list_fields_cmd-函数)
- [使用方法](#使用方法)
- [示例](#示例)
- [设计思路](#设计思路)
- [输入输出](#输入输出)
- [注意事项](#注意事项)

## 简介

LIST_FIELDS.py 是一个 Python 脚本，用于列出飞书表格中的字段。该脚本会调用飞书的 API，获取并打印出表格中的字段列表。

## 函数介绍

### LIST_FIELDS 函数

此函数用于列出飞书表格中的字段。函数的参数包括：

```python
LIST_FIELDS(app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None)
```

### LIST_FIELDS_CMD 函数

此函数用于解析命令行参数并调用 LIST_FIELDS 函数。函数的参数包括：

```python
LIST_FIELDS_CMD()
```

## 使用方法

在命令行中，可以通过以下方式调用 LIST_FIELDS_CMD 函数：

```python
python LIST_FIELDS.py --app_token your_app_token --table_id your_table_id --view_id your_view_id --page_token your_page_token --page_size your_page_size --config_file your_config_file_path
```

其中，`--app_token`、`--table_id`、`--view_id`、`--page_token`、`--page_size` 和 `--config_file` 参数用于指定相应的值。

## 示例

以下是一个使用示例：

```python
python LIST_FIELDS.py --app_token "your_app_token" --table_id "your_table_id" --view_id "your_view_id" --page_token "your_page_token" --page_size 100 --config_file "your_config_file_path"
```

## 设计思路

LIST_FIELDS.py 的设计思路主要包括以下几点：

1. 通过调用飞书的 API，获取表格中的字段列表。
2. 创建一个 ConfigParser 对象，并读取配置文件。
3. 通过 argparse 库解析命令行参数，并调用 LIST_FIELDS 函数列出字段。

## 输入输出

### 输入

如果未提供，将从配置文件中获取。

- `app_token`：应用的 token。
- `table_id`：表格的 ID。
- `view_id`：视图的 ID。
- `page_token`：页面 token。
- `page_size`：页面大小。
- `config_file`：配置文件的路径，默认值为 "feishu-config.ini"。

### 输出

- 如果一切正常，返回飞书 API 的响应，该响应包含了表格中的字段列表。
- 如果在尝试过程中出现错误，会抛出异常。

## 注意事项

- 在使用 LIST_FIELDS.py 时，需要确保已经正确安装了 Python 环境，并且已经安装了 argparse、configparser 和 requests 库。
- 在使用 LIST_FIELDS.py 时，需要确保提供的命令行参数是正确的。
- 在使用 LIST_FIELDS.py 时，需要确保飞书的 API 可以正常工作，并且提供的 token、table_id 和 view_id 是有效的。
- 在使用 LIST_FIELDS.py 时，需要确保配置文件中的信息是正确的，并且文件路径是可访问的。