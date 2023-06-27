# WRITE_APP_ACCESS_TOKEN.py 使用文档

该程序 `WRITE_APP_ACCESS_TOKEN.py` 是使用 Python 语言编写的，通过调用 `GET_APP_ACCESS_TOKEN` 函数获取应用访问令牌，并将其写入配置文件中。

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

1. 读取配置文件 `feishu-config.ini` 或指定的配置文件，获取应用的 ID（app_id）和密钥（app_secret）。
2. 调用 `GET_APP_ACCESS_TOKEN` 函数，获取应用访问令牌。
3. 检查获取到的应用访问令牌是否存在，如果不存在，则将其置为空字符串。
4. 检查配置文件中是否存在名为 `TOKEN` 的 section，如果不存在，则添加该 section。
5. 在 `TOKEN` section 下添加应用访问令牌（app_access_token）。
6. 将更新后的配置写入到配置文件中。
7. 返回获取到的应用访问令牌。

## 输入参数

### CMD 模式

该程序支持的输入参数如下：

- `-i/--id`：应用的 ID（app_id）
- `-s/--secret`：应用的密钥（app_secret）
- `--config_file`：配置文件路径

### 函数模式

- `app_id`：应用的 ID（app_id）
- `app_secret`：应用的密钥（app_secret）
- `config_file`：配置文件路径

## 输出结果

- 成功将应用访问令牌写入配置文件时，返回已写入的应用访问令牌的值。
- 写入配置文件失败时，返回 `None`。

您可以按照以下方式来调用该函数：

```python
app_access_token = WRITE_APP_ACCESS_TOKEN(app_id=None, app_secret=None, config_file=None)
```

## 使用示例

您可以按照以下方式来使用 `WRITE_APP_ACCESS_TOKEN.py`：

### 直接调用

```python
from WRITE_APP_ACCESS_TOKEN import WRITE_APP_ACCESS_TOKEN
from GET_APP_ACCESS_TOKEN import GET_APP_ACCESS_TOKEN

app_id = "YOUR_APP_ID"
app_secret = "YOUR_APP_SECRET"
config_file = "feishu-config.ini"

app_access_token = GET_APP_ACCESS_TOKEN(app_id, app_secret, config_file)
result = WRITE_APP_ACCESS_TOKEN(app_id, app_secret, config_file)

if result is None:
    print("发生错误，请检查您的输入并再试一次。")
else:
    print(f"app_access_token: {result}")
    print("成功写入配置文件")
```

### 命令行使用

1. 通过指定应用的 ID 和密钥来将应用访问令牌写入配置文件：

```
python WRITE_APP_ACCESS_TOKEN.py -i YOUR_APP_ID -

s YOUR_APP_SECRET --config_file /path/to/config.ini
```

2. 直接运行程序，使用默认的配置文件和参数：

```
python WRITE_APP_ACCESS_TOKEN.py
```

请注意，在运行程序之前，确保您已替换示例代码中的 `YOUR_APP_ID` 和 `YOUR_APP_SECRET` 为您自己的应用的 ID 和密钥。
