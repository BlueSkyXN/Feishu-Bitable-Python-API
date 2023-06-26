# WRITE_TABLE_ID.py 使用指南

## 目录
- [简介](#简介)
- [函数介绍](#函数介绍)
  - [WRITE_TABLE_ID 函数](#write_table_id-函数)
  - [WRITE_TABLE_ID_CMD 函数](#write_table_id_cmd-函数)
- [使用方法](#使用方法)
- [示例](#示例)
- [设计思路](#设计思路)
- [输入输出](#输入输出)
- [注意事项](#注意事项)

## 简介

WRITE_TABLE_ID.py 是一个 Python 脚本，用于将从 GET_TABLE_ID 获取的 table_id 写入到配置文件。该脚本首先会调用 GET_TABLE_ID 函数来获取数据表的 ID，然后将这个 ID 写入到配置文件中。

## 函数介绍

### WRITE_TABLE_ID 函数

此函数用于将从 GET_TABLE_ID 获取的 table_id 写入到配置文件。函数的参数包括：

```python
WRITE_TABLE_ID(name, app_token=None, user_access_token=None, page_size=None, page_token=None, config_file="feishu-config.ini")
```

### WRITE_TABLE_ID_CMD 函数

此函数用于解析命令行参数并调用 WRITE_TABLE_ID 函数。函数的参数包括：

```python
WRITE_TABLE_ID_CMD()
```

## 使用方法

在命令行中，可以通过以下方式调用 WRITE_TABLE_ID_CMD 函数：

```python
python WRITE_TABLE_ID.py -n 数据表名 --app_token your_app_token --user_access_token your_user_access_token --page_size your_page_size --page_token your_page_token --config_file your_config_file_path
```

其中，`-n` 参数用于指定要查询的数据表的名称，`--app_token`、`--user_access_token`、`--page_size`、`--page_token` 和 `--config_file` 参数用于指定相应的值。

## 示例

以下是一个使用示例：

```python
python WRITE_TABLE_ID.py -n "测试数据表" --app_token "your_app_token" --user_access_token "your_user_access_token" --page_size 10 --page_token "your_page_token" --config_file "your_config_file_path"
```

## 设计思路

WRITE_TABLE_ID.py 的设计思路主要包括以下几点：

1. 通过调用 GET_TABLE_ID 函数获取数据表的 ID。
2. 创建一个 ConfigParser 对象，并读取配置文件。
3. 尝试从 name 获取 table_id，如果提取的值不存在，将其置为空字符串。
4. 检查配置文件是否存在名为 'ID' 的 section，如果不存在则添加。
5. 在 'ID' section 下添加 table_id。
6. 尝试将新的配置写入到配置文件中。
7. 通过 argparse 库解析命令行参数，并调用 WRITE_TABLE_ID 函数将 table_id 写入到配置文件中。

## 输入输出

### 输入

- `name`：要查询的数据表的名称。
- `app_token`：应用的 token。
- `user_access_token`：用户的访问 token。
- `page_size`：页面大小。
- `

page_token`：页面 token。
- `config_file`：配置文件的路径，默认值为 "feishu-config.ini"。

### 输出

- 如果一切正常，返回提取的值。
- 如果在尝试过程中出现错误，返回 None。

## 注意事项

- 在使用 WRITE_TABLE_ID.py 时，需要确保已经正确安装了 Python 环境，并且已经安装了 argparse 和 configparser 库。
- 在使用 WRITE_TABLE_ID.py 时，需要确保 GET_TABLE_ID 函数可以正常工作。
- 在使用 WRITE_TABLE_ID.py 时，需要确保提供的命令行参数是正确的。
