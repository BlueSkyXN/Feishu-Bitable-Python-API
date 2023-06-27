# REFRESH_USER_ACCESS_TOKEN.py 使用文档

该程序 `REFRESH_USER_ACCESS_TOKEN.py` 是使用 Python 语言编写的，通过调用飞书开放平台的接口刷新用户的访问令牌（access token）。

参考官方API文档 [刷新 user_access_token](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/authen-v1/authen/refresh_access_token)

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

1. 读取配置文件（默认为 `feishu-config.ini`），获取应用访问令牌（app_access_token）和刷新令牌（refresh_token）。
2. 构建请求的URL、请求头和请求体。
3. 发送请求到飞书的认证接口，使用刷新令牌来获取新的用户访问令牌。
4. 检查响应状态码和响应体中的code字段，判断访问令牌刷新是否成功。
5. 如果成功，更新配置文件中的用户访问令牌（user_access_token）和刷新令牌（refresh_token）。
6. 返回新的用户访问令牌。

## 输入参数

### CMD 模式

该程序支持的输入参数如下：

- `-a/--app_token`：应用访问令牌（app_access_token）
- `-r/--refresh`：刷新令牌（refresh_token）
- `--config_file`：配置文件路径，默认为 `feishu-config.ini`

### 函数模式

- `app_access_token`：应用访问令牌（app_access_token）
- `refresh_token`：刷新令牌（refresh_token）
- `config_file`：配置文件路径，默认为 `feishu-config.ini`

## 输出结果

- 成功刷新用户访问令牌时，返回新的用户访问令牌（access_token）的值。
- 刷新用户访问令牌失败时，返回 `None`。

您可以按照以下方式来调用该函数：

```python
user_access_token = REFRESH_USER_ACCESS_TOKEN(app_access_token=None, refresh_token=None, config_file=None)
```

## 使用示例

您可以按照以下方式来使用 `REFRESH_USER_ACCESS_TOKEN.py`：

### 直接调用

```python
from REFRESH_USER_ACCESS_TOKEN import REFRESH_USER_ACCESS_TOKEN

app_token = "YOUR_APP_TOKEN"
refresh_token = "YOUR_REFRESH_TOKEN"
user_access_token = REFRESH_USER_ACCESS_TOKEN(app_token, refresh_token)
print(f"User Access Token: {user_access_token}")
```

### 命令行使用

1. 通过指定应用访问令牌和刷新令牌来刷新用户访问令牌：

```
python REFRESH_USER_ACCESS_TOKEN.py -a YOUR_APP_TOKEN -r YOUR_REFRESH_TOKEN
```

2. 通过指定配置文件路径、应用访问令牌

和刷新令牌来刷新用户访问令牌：

```
python REFRESH_USER_ACCESS_TOKEN.py -a YOUR_APP_TOKEN -r YOUR_REFRESH_TOKEN --config_file /path/to/config.ini
```

3. 直接运行程序，使用默认的配置文件和参数：

```
python REFRESH_USER_ACCESS_TOKEN.py -a YOUR_APP_TOKEN -r YOUR_REFRESH_TOKEN
```

请注意，在运行程序之前，确保您已替换示例代码中的 `YOUR_APP_TOKEN` 和 `YOUR_REFRESH_TOKEN` 为您自己的应用访问令牌和刷新令牌。

