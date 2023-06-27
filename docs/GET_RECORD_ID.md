# GET_TABLE_ID.py 使用文档

该程序 `GET_TABLE_ID.py` 是使用 Python 语言编写的，通过调用 `LIST_RECORDS.py` 中的函数实现从数据表中获取具有特定字段值的记录的 ID。

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

1. 读取配置文件（默认为 `feishu-config.ini`），并解析出 LIST_RECORDS 部分对应的 key 值。
2. 调用 `LIST_RECORDS()` 函数获取数据表中的所有记录。
3. 遍历响应中的每一个记录，判断该记录中指定字段的值是否等于给定的值。
4. 如果找到了符合条件的记录，返回该记录的 ID；否则返回 `NONE`。

## 输入参数

### CMD 模式

该程序支持的输入参数如下：

- `-f/--field/--field_name/--name/--key`：指定需要查找的字段名
- `-v/--value`：必选参数，指定需要查找的字段值
- `--config_file`：配置文件路径，默认为 `feishu-config.ini`

其中 `-f/--field/--field_name/--name/--key` 五个参数是等效的，只需要使用其中一个即可指定要查找的字段名。

### 函数模式

- `field_value`：需要查找的字段值
- `field_name`：需要查找的字段名，默认为 None。如果不指定，则从配置文件中获取。
- `config_file`：配置文件路径，默认为 `feishu-config.ini`

## 输出结果

- 找到符合条件的记录时，返回该记录的 ID
- 未找到符合条件的记录时，返回字符串 `NONE`

您可以按照以下方式来调用该函数：

```python
record_id = GET_RECORD_ID(field_value, field_name=None, config_file=None)
```

## 使用示例

您可以按照以下方式来使用 `GET_TABLE_ID.py`：

### 直接调用

```python
from GET_TABLE_ID import GET_RECORD_ID

field_value = "张三"
record_id = GET_RECORD_ID(field_value)
print(record_id)
```

### 命令行使用

1. 查找字段 `name` 的值为 `张三` 的记录：

```
python GET_TABLE_ID.py -f name -v 张三
```

2. 通过指定配置文件路径来查找记录：

```
python GET_TABLE_ID.py -f name -v 张三 --config_file /path/to/config.ini
```

3. 直接运行程序，使用默认的配置文件和参数：

```
python GET_TABLE_ID.py --value 张三
```
