# GET_APP_ACCESS_TOKEN.py 使用文档

该程序 `GET_APP_ACCESS_TOKEN.py` 是使用 Python 语言编写的，通过调用飞书开放平台的接口获取应用访问令牌（app access token）。

参考官方API文档 [自建应用获取 app_access_token](https://open.feishu.cn/document/server-docs/authentication-management/access-token/app_access_token_internal)

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

1. 读取配置文件 `feishu-config.ini`，获取应用的 ID（app_id）和密钥（app_secret）。
2. 构建请求的URL、请求头和请求体。
3. 发送请求到飞书的认证接口，使用应用的 ID 和密钥来获取应用访问令牌。
4. 检查响应状态码和响应体中的字段，判断应用访问令牌获取是否成功。
5. 返回应用访问令牌。

## 输入参数

### CMD 模式

该程序支持的输入参数如下：

- `-i/--id`：应用的 ID（app_id）
- `-s/--secret`：应用的密钥（app_secret）

### 函数模式

- `app_id`：应用的 ID（app_id）
- `app_secret`：应用的密钥（app_secret）

## 输出结果

- 成功获取应用访问令牌时，返回应用访问令牌（app_access_token）的值。
- 获取应用访问令牌失败时，返回 `None`。

您可以按照以下方式来调用该函数：

```python
app_access_token = GET_APP_ACCESS_TOKEN(app_id=None, app_secret=None)
```

## 使用示例

您可以按照以下方式来使用 `GET_APP_ACCESS_TOKEN.py`：

### 直接调用

```python
from GET_APP_ACCESS_TOKEN import GET_APP_ACCESS_TOKEN

app_id = "YOUR_APP_ID"
app_secret = "YOUR_APP_SECRET"
app_access_token = GET_APP_ACCESS_TOKEN(app_id, app_secret)
print(f"app_access_token: {app_access_token}")
```

### 命令行使用

1. 通过指定应用的 ID 和密钥来获取应用访问令牌：

```
python GET_APP_ACCESS_TOKEN.py -i YOUR_APP_ID -s YOUR_APP_SECRET
```

2. 直接运行程序，使用默认的配置文件和参数：

```
python GET_APP_ACCESS_TOKEN.py
```

请注意，在运行程序之前，确保您已替换示例代码中的 `YOUR_APP_ID` 和 `YOUR_APP_SECRET` 为您自己的应用的 ID 和密钥。

以上是 `GET_APP_ACCESS_TOKEN.py` 程序的使用文档，如果您有任何问题或需要进一步的帮助，请随时提问。