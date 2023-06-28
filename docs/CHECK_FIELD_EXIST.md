# CHECK_FIELD_EXIST.py 使用指南

`CHECK_FIELD_EXIST.py` 是一个用于检查并创建飞书表格中不存在的字段的工具。它提供了一个函数 `CHECK_FIELD_EXIST()`，可以通过给定的 CSV 文件和飞书配置信息，检查并创建不存在的字段。

## 目录
- [简介](#简介)
- [函数介绍](#函数介绍)
  - [CHECK_FIELD_EXIST 函数](#check_field_exist-函数)
- [使用方法](#使用方法)
- [示例](#示例)
- [设计思路](#设计思路)
- [输入输出](#输入输出)
- [注意事项](#注意事项)

## 简介

CHECK_FIELD_EXIST.py 是一个 Python 脚本，用于检查并创建飞书表格中不存在的字段。该脚本首先会调用 LIST_FIELDS 函数来获取飞书表格的字段列表，然后与 CSV 文件中的字段进行比对，如果有不存在的字段，就会调用 CREATE_FIELD 函数来创建新的字段。

## 函数介绍

### CHECK_FIELD_EXIST 函数

此函数用于检查并创建飞书表格中不存在的字段。函数的参数包括：

```python
CHECK_FIELD_EXIST(app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, csv_file=None, config_file=None)
```

## 使用方法

在命令行中，可以通过以下方式调用 CHECK_FIELD_EXIST 函数：

```python
python CHECK_FIELD_EXIST.py --app_token your_app_token --table_id your_table_id --view_id your_view_id --page_token your_page_token --page_size your_page_size --csv_file your_csv_file_path --config_file your_config_file_path
```

其中，`--app_token`、`--table_id`、`--view_id`、`--page_token`、`--page_size`、`--csv_file` 和 `--config_file` 参数用于指定相应的值。

## 示例

以下是一个使用示例：

```python
python CHECK_FIELD_EXIST.py --app_token "your_app_token" --table_id "your_table_id" --view_id "your_view_id" --page_token "your_page_token" --page_size 100 --csv_file "your_csv_file_path" --config_file "your_config_file_path"
```

## 设计思路

CHECK_FIELD_EXIST.py 的设计思路主要包括以下几点：

1. 通过调用 LIST_FIELDS 函数获取飞书表格的字段列表。
2. 从 CSV 文件中读取字段列表。
3. 比对飞书表格的字段列表和 CSV 文件的字段列表，找出不存在的字段。
4. 对于每个不存在的字段，调用 CREATE_FIELD 函数来创建新的字段。
5. 通过 argparse 库解析命令行参数，并调用 CHECK_FIELD_EXIST 函数进行字段检查和创建。

## 输入输出

### 输入

- `app_token` (str, optional): 飞书应用的访问令牌。如果未提供，将从配置文件中获取。
- `table_id` (str, optional): 飞书表格的唯一标识符。如果未提供，将从配置文件中获取。
- `view_id` (str, optional): 飞书视图的唯一标识符。如果未提供，将从配置文件中获取。
- `page_token` (str, optional): 分页查询的页标识符。如果未提供，将从配置文件中获取。
- `page_size` (int, optional): 分页查询的页大小。如果未提供，将从配置文件中获取，默认为 100。
- `csv_file` (str, optional): CSV 文件的路径。如果未提供，将从配置文件中获取。
- `config_file` (str, optional): 配置文件的路径。如果未提供，默认为 `feishu-config.ini`。

### 输出

- 如果一切正常，对于每个成功创建的字段，会打印一条消息："字段 {field} 已成功创建"。
- 如果在尝试过程中出现错误，会抛出异常。

## 注意事项

- 在使用 CHECK_FIELD_EXIST.py 时，需要确保已经正确安装了 Python 环境，并且已经安装了 argparse、configparser 和 pandas 库。
- 在使用 CHECK_FIELD_EXIST.py 时，需要确保 LIST_FIELDS 和 CREATE_FIELD 函数可以正常工作。
- 在使用 CHECK_FIELD_EXIST.py 时，需要确保提供的命令行参数是正确的。
- 在使用 CHECK_FIELD_EXIST.py 时，需要确保 CSV 文件中的字段名与飞书表格中的字段名一致。