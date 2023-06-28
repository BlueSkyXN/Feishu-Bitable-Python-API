# BUILD_FIELD.py 使用文档

该程序 `BUILD_FIELD.py` 是使用 Python 语言编写的，用于根据 CSV 文件构建飞书字段配置，并生成请求体。

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

1. 读取 CSV 文件的第一行，即字段名称。
2. 读取配置文件，并检查是否存在对应字段的配置。如果不存在，则将字段添加到配置文件中。
3. 遍历 CSV 文件的每一行，根据字段的配置类型进行数据转换。
4. 构建请求体，将转换后的数据以记录的形式添加到请求体中。
5. 根据需要，将请求体写入配置文件。

## 输入参数

### CMD 模式

该程序支持的输入参数如下：

- `-i/--input`：指定输入的 CSV 文件路径，默认为 `input.csv`。
- `-c/--config`：指定配置文件路径，默认为 `feishu-field.ini`。

### 函数模式

- `csv_file`：输入的 CSV 文件路径，默认为 `input.csv`。
- `config_file`：配置文件路径，默认为 `feishu-field.ini`。

## 输出结果

该程序将生成一个请求体，其中包含了根据 CSV 文件构建的字段配置信息。

## 使用示例

您可以按照以下方式使用 `BUILD_FIELD.py`：

### 直接调用

```python
import json
from BUILD_FIELD import BUILD_FIELD

input_file = "input.csv"
config_file = "feishu-field.ini"

request_body = BUILD_FIELD(input_file, config_file)
print(json.dumps(request_body, indent=4, ensure_ascii=False))
```

### 命令行使用

1. 使用默认的输入文件和配置文件路径，生成请求体：

```
python BUILD_FIELD.py
```

2. 指定输入文件和配置文件路径，生成请求体：

```
python BUILD_FIELD.py -i input.csv -c feishu-field.ini
```