# GET_TABLE_ID.py 使用指南

## 一、简介

GET_TABLE_ID.py 是一个 Python 脚本，用于通过给定的名称获取数据表的 ID。该脚本首先会调用 LIST_TABLES 函数来获取所有的数据表信息，然后在这些信息中寻找名称匹配的数据表，并返回其 ID。如果没有找到名称匹配的数据表，脚本会返回 "NONE"。

## 二、函数介绍

### 1. GET_TABLE_ID 函数

此函数用于通过给定的名称获取表的 ID。函数的参数包括：

- `name`：要查询的数据表的名称，默认值为 "数据表"。
- `app_token`：应用的 token。
- `user_access_token`：用户的访问 token。
- `page_size`：页面大小。
- `page_token`：页面 token。
- `config_file`：配置文件的路径，默认值为 "feishu-config.ini"。

### 2. GET_TABLE_ID_CMD 函数

此函数用于解析命令行参数并调用 GET_TABLE_ID 函数。函数的参数包括：

- `-i` 或 `--input`：要查询的数据表的名称，默认值为 "数据表"。
- `-n` 或 `--name`：要查询的数据表的名称。
- `--app_token`：应用的 token。
- `--user_access_token`：用户的访问 token。
- `--page_size`：页面大小。
- `--page_token`：页面 token。
- `--config_file`：配置文件的路径，默认值为 "feishu-config.ini"。

## 三、使用方法

在命令行中，可以通过以下方式调用 GET_TABLE_ID_CMD 函数：

```python
python GET_TABLE_ID.py -n 数据表名 --app_token your_app_token --user_access_token your_user_access_token --page_size your_page_size --page_token your_page_token --config_file your_config_file_path
```

其中，`-n` 参数用于指定要查询的数据表的名称，`--app_token`、`--user_access_token`、`--page_size`、`--page_token` 和 `--config_file` 参数用于指定相应的值。

## 四、示例

以下是一个使用示例：

```python
python GET_TABLE_ID.py -n "测试数据表" --app_token "your_app_token" --user_access_token "your_user_access_token" --page_size 10 --page_token "your_page_token" --config_file "your_config_file_path"
```

在这个示例中，我们查询的数据表的名称为 "测试数据表"，应用的 token 为 "your_app_token"，用户的访问 token 为 "your_user_access_token"，页面大小为 10，页面 token 为 "your_page_token"，配置文件的路径为 "your_config_file_path"。

## 五、设计思路

GET_TABLE_ID.py 的设计思路主要包括以下几点：

1. 通过调用 LIST_TABLES 函数获取所有的数据表信息。
2. 在返回的所有数据表信息中，寻找名称匹配的数据表。
3. 如果找到了名称匹配的数据表，返回其 ID；如果没有找到，返回 "NONE"。
4. 通过 argparse 库解析

命令行参数，并调用 GET_TABLE_ID 函数获取表的 ID。

## 六、输入输出

### 输入

- `name`：要查询的数据表的名称，默认值为 "数据表"。
- `app_token`：应用的 token。
- `user_access_token`：用户的访问 token。
- `page_size`：页面大小。
- `page_token`：页面 token。
- `config_file`：配置文件的路径，默认值为 "feishu-config.ini"。

### 输出

- 如果找到了名称匹配的数据表，返回其 ID。
- 如果没有找到名称匹配的数据表，返回 "NONE"。

## 七、注意事项

- 在使用 GET_TABLE_ID.py 时，需要确保已经正确安装了 Python 环境，并且已经安装了 argparse 库。
- 在使用 GET_TABLE_ID.py 时，需要确保 LIST_TABLES 函数可以正常工作。
- 在使用 GET_TABLE_ID.py 时，需要确保提供的命令行参数是正确的。