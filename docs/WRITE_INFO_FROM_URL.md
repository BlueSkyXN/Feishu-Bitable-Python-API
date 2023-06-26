## WRITE_INFO_FROM_URL 使用指南

`WRITE_INFO_FROM_URL` 函数用于从给定的 URL 中提取信息，并将提取的信息写入配置文件中。

### 函数签名

```python
def WRITE_INFO_FROM_URL(url, config_file="feishu-config.ini"):
    ...
```

### 参数

- `url` (str): 要提取信息的 URL。
- `config_file` (str, optional): 配置文件的路径，默认为 "feishu-config.ini"。

### 返回值

- 如果成功提取信息并写入配置文件，返回一个包含提取的信息的元组 `(app_token, table_id, view_id)`。
- 如果发生错误，返回 `None`。

### 示例

以下是一个示例的运行结果：

```python
url = "https://example.com/base/VwGhbo65BaYLaOsSz1nciWc5ncb?table=tblzDsYuQkXfoy9e&view=vewAgGXuqf"
result = WRITE_INFO_FROM_URL(url)

if result is None:
    print("发生错误，请检查您的输入URL并再试一次。")
else:
    app_token, table_id, view_id = result
    print(f"app_token: {app_token}")
    print(f"table_id: {table_id}")
    print(f"view_id: {view_id}")
    print("成功写入 'feishu-config.ini' 文件")
```

输出：
```
app_token: VwGhbo65BaYLaOsSz1nciWc5ncb
table_id: tblzDsYuQkXfoy9e
view_id: vewAgGXuqf
成功写入 'feishu-config.ini' 文件
```

### 命令行接口

`WRITE_INFO_FROM_URL` 还提供了一个命令行接口，可以直接从命令行中调用该函数。使用 `-u/--url` 参数指定要提取信息的 URL，使用 `-c/--config` 参数指定配置文件路径。

示例命令行调用：

```
$ python WRITE_INFO_FROM_URL.py -u "https://example.com/base/VwGhbo65BaYLaOsSz1nciWc5ncb?table=tblzDsYuQkXfoy9e&view=vewAgGXuqf"
```

命令行参数说明：
- `-u/--url`: 用于提取信息的 URL。
- `-c/--config`: 配置文件路径，默认为 "feishu-config.ini"。
