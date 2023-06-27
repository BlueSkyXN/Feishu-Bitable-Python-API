# WRITE_LOGIN_CODE.py 使用文档

该程序 `WRITE_LOGIN_CODE.py` 是使用 Python 语言编写的，通过构建登录 URL、获取用户输入的登录后的新 URL，并解析其中的登录授权码（login code），将其写入配置文件中。

参考官方API文档 [获取登录预授权码](https://open.feishu.cn/document/server-docs/authentication-management/login-state-management/obtain-code)

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

1. 读取配置文件 `feishu-config.ini` 或指定的配置文件，获取重定向 URL（redirect_uri）和应用的 ID（app_id）。
2. 如果未提供重定向 URL 或应用的 ID，则尝试从配置文件中获取，如果配置文件中也不存在，则使用默认值。
3. 构建登录 URL，包括重定向 URL、应用的 ID 和状态（state）。
4. 打印登录 URL，提示用户访问该 URL 进行登录。
5. 用户登录后，输入登录后得到的新的 URL。
6. 解析新的 URL，提取其中的登录授权码（login code）。
7. 将登录授权码写入配置文件的 `TOKEN` section 中。
8. 尝试将更新后的配置写入到配置文件中。
9. 打印成功写入配置文件的消息。

## 输入参数

### CMD 模式

该程序支持的输入参数如下：

- `-r/--redirect_uri`：重定向 URL
- `-a/--app_id`：应用的 ID（app_id）
- `-c/--config_file`：配置文件路径

### 函数模式

- `redirect_uri`：重定向 URL
- `app_id`：应用的 ID（app_id）
- `config_file`：配置文件路径

## 输出结果

- 成功将登录授权码写入配置文件时，打印成功写入配置文件的消息。
- 写入配置文件失败时，打印相应的错误消息。

您可以按照以下方式来调用该函数：

```python
WRITE_LOGIN_CODE(redirect_uri=None, app_id=None, config_file=None)
```

## 使用示例

您可以按照以下方式来使用 `WRITE_LOGIN_CODE.py`：

### 直接调用

```python
from WRITE_LOGIN_CODE import WRITE_LOGIN_CODE

redirect_uri = "YOUR_REDIRECT_URI"
app_id = "YOUR_APP_ID"
config_file = "feishu-config.ini"

WRITE_LOGIN_CODE(redirect_uri, app_id, config_file)
```

### 命令行使用

1. 通过指定重定向 URL 和应用的 ID 来将登录授权码写入配置文件：

```
python WRITE_LOGIN_CODE.py -r YOUR_REDIRECT_URI -a YOUR_APP_ID
```

2. 通过指定配置文件路径、重定向 URL 和应用的 ID 来将登录授权码写入配置文件：

```
python WRITE_LOGIN_CODE.py -r YOUR_REDIRECT_URI -a YOUR_APP_ID --config_file /path/to/config.ini


```

请注意，在运行程序之前，确保您已替换示例代码中的 `YOUR_REDIRECT_URI` 和 `YOUR_APP_ID` 为您自己的重定向 URL 和应用的 ID。

