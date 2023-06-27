# GET_USER_ACCESS_TOKEN.py 使用文档

该程序 `GET_USER_ACCESS_TOKEN.py` 是使用 Python 语言编写的，通过调用飞书开放平台的接口获取用户的访问令牌（access token）。

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

1. 读取配置文件（默认为 `feishu-config.ini`），获取应用访问令牌（app_access_token）。
2. 构建请求的URL、请求头和请求体。
3. 发送请求到飞书的认证接口，获取用户的访问令牌。
4. 检查响应状态码和响应体中的code字段，判断访问令牌获取是否成功。
5. 如果成功，更新配置文件中的用户访问令牌（user_access_token）和刷新令牌（refresh_token）。
6. 返回用户访问令牌和刷新令牌。

## 输入参数

### CMD 模式

该程序支持的输入参数如下：

- `-l/--login_code`：登录预授权码
- `--config_file`：配置文件路径，默认为 `feishu-config.ini`

### 函数模式

- `login_code`：登录预授权码
- `config_file`：配置文件路径，默认为 `feishu-config.ini`

## 输出结果

- 成功获取用户访问令牌时，返回用户访问令牌（user_access_token）和刷新令牌（refresh_token）的值。
- 获取用户访问令牌失败时，返回 `None`。

您可以按照以下方式来调用该函数：

```python
user_token, refresh_token = GET_USER_ACCESS_TOKEN(login_code, config_file=None)
```

## 使用示例

您可以按照以下方式来使用 `GET_USER_ACCESS_TOKEN.py`：

### 直接调用

```python
from GET_USER_ACCESS_TOKEN import GET_USER_ACCESS_TOKEN

login_code = "YOUR_LOGIN_CODE"
user_token, refresh_token = GET_USER_ACCESS_TOKEN(login_code)
print(f"user_access_token: {user_token}")
print(f"refresh_token: {refresh_token}")
```

### 命令行使用

1. 通过指定登录预授权码来获取用户访问令牌：

```
python GET_USER_ACCESS_TOKEN.py -l YOUR_LOGIN_CODE
```

2. 通过指定配置文件路径和登录预授权码来获取用户访问令牌：

```
python GET_USER_ACCESS_TOKEN.py -l YOUR_LOGIN_CODE --config_file /path/to/config.ini
```

3. 直接运行程序，使用默认的配置文件和参数：

```
python GET_USER_ACCESS_TOKEN.py -l YOUR_LOGIN_CODE
```

请注意，在运行程序之前，确保您已替换示例代码中的 `YOUR_LOGIN_CODE` 为您自己的登录预授权码。