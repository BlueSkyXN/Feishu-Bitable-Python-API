# GET_TABLE_ID.py 使用指南

`GET_TABLE_ID.py` 是一个用于检索子表 ID 的工具。它提供了一个函数 GET_TABLE_ID()，可以通过给定的子表名称获取子表的 ID。

## 目录
1. [简介](#简介)
2. [函数介绍](#函数介绍)
   2.1 [GET_TABLE_ID 函数](#GET_TABLE_ID-函数)
   2.2 [GET_TABLE_ID_CMD 函数](#GET_TABLE_ID_CMD-函数)
3. [使用方法](#使用方法)
4. [示例](#示例)
5. [设计思路](#设计思路)
6. [输入输出](#输入输出)
7. [注意事项](#注意事项)

## 简介

GET_TABLE_ID.py 是一个 Python 脚本，用于通过给定的名称获取数据表的 ID。它提供了命令行接口，可以方便地指定查询的数据表名称和其他参数，并返回匹配的数据表的 ID。如果没有找到匹配的数据表，将返回 "NONE"。

## 函数介绍

### GET_TABLE_ID 函数

```python
GET_TABLE_ID(name="数据表", app_token=None, user_access_token=None, page_size=None, page_token=None, config_file=None)
```

此函数用于通过给定的名称获取表的 ID。它接受以下参数：

- `name`（可选）：要查询的数据表的名称，默认值为 "数据表"。
- `app_token`（可选）：应用的 token。
- `user_access_token`（可选）：用户的访问 token。
- `page_size`（可选）：页面大小。
- `page_token`（可选）：页面 token。
- `config_file`（可选）：配置文件的路径，默认值为 "feishu-config.ini"。

### GET_TABLE_ID_CMD 函数

```python
GET_TABLE_ID_CMD()
```

此函数用于解析命令行参数并调用 GET_TABLE_ID 函数。它通过命令行参数指定要查询的数据表的名称和其他参数，并打印出匹配的数据表的 ID。

命令行参数包括：

- `-i` 或 `--input`（可选）：要查询的数据表的名称，默认值为 "数据表"。
- `-n` 或 `--name`（可选）：要查询的数据表的名称。
- `--app_token`（可选）：应用的 token。
- `--user_access_token`（可选）：用户的访问 token。
- `--page_size`（可选）：页面大小。
- `--page_token`（可选）：页面 token。
- `--config_file`（可选）：配置文件的路径，默认值为 "feishu-config.ini"。

## 使用方法

在命令行中，可以使用以下命令来调用 GET_TABLE_ID_CMD 函数：

```bash
python GET_TABLE_ID.py -n 数据表名 --app_token your_app_token --user_access_token your_user_access_token --page_size your_page_size --page_token your_page_token --config_file your_config_file_path
```

其中，`-n` 参数用于指定要查询的数据表的名称，`--app_token`、`--user_access_token`、`--page_size`、`--page_token` 和 `--config_file` 参数用于指定相应的值。

## 示例

以下是一个使用示例：

```bash
python GET_TABLE_ID.py -n "测试数据表" --app_token "your

_app_token" --user_access_token "your_user_access_token" --page_size 10 --page_token "your_page_token" --config_file "your_config_file_path"
```

在这个示例中，我们查询的数据表的名称为 "测试数据表"，应用的 token 为 "your_app_token"，用户的访问 token 为 "your_user_access_token"，页面大小为 10，页面 token 为 "your_page_token"，配置文件的路径为 "your_config_file_path"。

执行以上命令后，脚本将解析命令行参数并调用 GET_TABLE_ID 函数来获取表的 ID。如果找到了名称匹配的数据表，它将打印出对应的 ID。如果没有找到匹配的数据表，它将打印出 "NONE"。

## 设计思路

GET_TABLE_ID.py 的设计思路主要包括以下几点：

1. 通过调用 LIST_TABLES 函数获取所有的数据表信息。
2. 在返回的所有数据表信息中，寻找名称匹配的数据表。
3. 如果找到了名称匹配的数据表，返回其 ID；如果没有找到，返回 "NONE"。
4. 通过 argparse 库解析命令行参数，并调用 GET_TABLE_ID 函数获取表的 ID。

## 输入输出

### 输入

- `name`（可选）：要查询的数据表的名称，默认值为 "数据表"。
- `app_token`（可选）：应用的 token。
- `user_access_token`（可选）：用户的访问 token。
- `page_size`（可选）：页面大小。
- `page_token`（可选）：页面 token。
- `config_file`（可选）：配置文件的路径，默认值为 "feishu-config.ini"。

### 输出

- 如果找到了名称匹配的数据表，返回其 ID。
- 如果没有找到名称匹配的数据表，返回 "NONE"。

## 注意事项

- 在使用 GET_TABLE_ID.py 时，需要确保已经正确安装了 Python 环境，并且已经安装了 argparse 库。
- 在使用 GET_TABLE_ID.py 时，需要确保 LIST_TABLES 函数可以正常工作。
- 在使用 GET_TABLE_ID.py 时，需要确保提供的命令行参数是正确的。
