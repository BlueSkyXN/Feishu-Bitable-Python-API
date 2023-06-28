# DELETE_RECORD.py 使用指南

`DELETE_RECORD.py` 是一个用于删除飞书表格中的记录的工具。它提供了一个函数 `DELETE_RECORD()`，可以通过给定的飞书配置信息和记录ID，删除飞书表格中的指定记录。

参考官方API文档 [删除记录](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/delete)

## 目录
- [简介](#简介)
- [函数介绍](#函数介绍)
  - [DELETE_RECORD 函数](#delete_record-函数)
  - [DELETE_RECORD_CMD 函数](#delete_record_cmd-函数)
- [使用方法](#使用方法)
- [示例](#示例)
- [设计思路](#设计思路)
- [输入输出](#输入输出)
- [注意事项](#注意事项)

## 简介

DELETE_RECORD.py 是一个 Python 脚本，用于删除飞书表格中的记录。该脚本会调用飞书的 API，删除指定的记录。

## 函数介绍

### DELETE_RECORD 函数

此函数用于删除飞书表格中的指定记录。函数的参数包括：

```python
DELETE_RECORD(app_token=None, table_id=None, record_id=None, config_file=None)
```

### DELETE_RECORD_CMD 函数

此函数用于解析命令行参数并调用 DELETE_RECORD 函数。函数的参数包括：

```python
DELETE_RECORD_CMD()
```

## 使用方法

在命令行中，可以通过以下方式调用 DELETE_RECORD_CMD 函数：

```python
python DELETE_RECORD.py --app_token your_app_token --table_id your_table_id --record_id your_record_id --config your_config_file_path
```

其中，`--app_token`、`--table_id`、`--record_id` 和 `--config` 参数用于指定相应的值。

## 示例

以下是一个使用示例：

```python
python DELETE_RECORD.py --app_token "your_app_token" --table_id "your_table_id" --record_id "your_record_id" --config "your_config_file_path"
```

## 设计思路

DELETE_RECORD.py 的设计思路主要包括以下几点：

1. 通过调用飞书的 API，删除指定的记录。
2. 创建一个 ConfigParser 对象，并读取配置文件。
3. 通过 argparse 库解析命令行参数，并调用 DELETE_RECORD 函数删除记录。

## 输入输出

### 输入

- `app_token`：应用的 token。
- `table_id`：表格的 ID。
- `record_id`：要删除的记录的 ID。
- `config_file`：配置文件的路径，默认值为 "feishu-config.ini"。

### 输出

- 如果一切正常，打印一条消息："Successfully deleted record: {record_id}"。
- 如果在尝试过程中出现错误，打印错误信息。

## 注意事项

- 在使用 DELETE_RECORD.py 时，需要确保已经正确安装了 Python 环境，并且已经安装了 argparse、configparser 和 requests 库。
- 在使用 DELETE_RECORD.py 时，需要确保提供的命令行参数是正确的。
- 在使用 DELETE_RECORD.py 时，需要确保飞书的 API 可以正常工作，并且提供的 token、table_id 和 record_id 是有效的。
- 在

使用 DELETE_RECORD.py 时，需要确保配置文件中的信息是正确的，并且文件路径是可访问的。
- 在使用 DELETE_RECORD.py 时，需要确保要删除的记录在飞书表格中确实存在。如果尝试删除一个不存在的记录，可能会导致错误。