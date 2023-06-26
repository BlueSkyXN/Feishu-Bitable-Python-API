# LIST_RECORDS.py 文档

`LIST_RECORDS.py` 是一个用于列出飞书多维表格中指定表格的记录的工具。它提供了一个名为 `LIST_RECORDS()` 的函数，可以通过给定的参数或配置文件来获取记录列表。

参考官方API文档 [列出记录](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/list)

## 使用指南

### 命令行方式

通过命令行参数直接运行 `LIST_RECORDS.py` 脚本可以获取记录列表。以下是命令行参数的说明：

```bash
python LIST_RECORDS.py --app_token <app_token> --table_id <table_id> --page_token <page_token> --page_size <page_size> --config_file <config_file_path>
```

- `--app_token`：飞书应用的唯一标识符 (app token)。
- `--table_id`：指定要获取记录的表格 ID。
- `--page_token`：分页标记，用于获取下一页的记录列表。
- `--page_size`：分页大小，指定每页返回的记录数量。
- `--config_file`：配置文件路径，指定配置文件的位置。默认为 "feishu-config.ini"。

### 导入模块方式

您也可以将 `LIST_RECORDS.py` 脚本导入为模块，并使用 `LIST_RECORDS()` 函数来获取记录列表。以下是函数定义和参数说明：

```python
def LIST_RECORDS(app_token=None, table_id=None, page_token=None, page_size=None, config_file=None):
    # 函数体...

# 使用示例
response_body = LIST_RECORDS(app_token, table_id, page_token, page_size, config_file)
print(response_body)
```

- `app_token`：飞书应用的唯一标识符 (app token)。如果未提供，将从配置文件中获取默认值。
- `table_id`：要获取记录的表格 ID。如果未提供，将从配置文件中获取默认值。
- `page_token`：分页标记，用于获取下一页的记录列表。如果未提供，将从配置文件中获取默认值。
- `page_size`：分页大小，指定每页返回的记录数量。如果未提供，将从配置文件中获取默认值。
- `config_file`：配置文件路径，指定配置文件的位置。默认为 "feishu-config.ini"。

## 设计思路

`LIST_RECORDS.py` 的设计思路是通过飞书多维表格 API 来获取记录列表。它使用 HTTP GET 请求访问 API，并根据提供的参数来定制请求。以下是设计思路的概述：

1. 读取配置文件：首先，脚本会读取配置文件（默认为 "feishu-config.ini"）以获取默认的 app_token、table_id、page_token 和 page_size 值。

2. 解析命令行参数：如果使用命令行方式运行脚本，它会解析命令行参数并覆盖配置文件中的默认值。

3. 构造请求：根据提供的参数，脚本会构造包含认证

信息和查询参数的请求 URL 和请求头。

4. 发起请求：使用 Python 的 `requests` 库发送 HTTP GET 请求，并获取响应体。

5. 解析响应：将响应体解析为 JSON 格式，并返回记录列表。

## 输入输出

### 输入

`LIST_RECORDS.py` 脚本接受以下参数作为输入：

- `app_token`：飞书应用的唯一标识符 (app token)。
- `table_id`：要获取记录的表格 ID。
- `page_token`：分页标记，用于获取下一页的记录列表。
- `page_size`：分页大小，指定每页返回的记录数量。
- `config_file`：配置文件路径，指定配置文件的位置。

如果这些参数未提供，则脚本将尝试从配置文件中获取默认值。

### 输出

输出是一个包含记录列表的 JSON 对象。每个记录包含其详细信息，如记录的字段值等。

## 示例

以下是使用 `LIST_RECORDS.py` 脚本的示例：

```bash
python LIST_RECORDS.py --app_token appbcbWCzen6D8dezhoCH2RpMAh --table_id tblKz5D60T4JlfcT --page_token pgKz5D60T4JlfcT --page_size 10 --config_file feishu-config.ini
```

上述命令会使用指定的参数来获取记录列表，并将结果打印为 JSON 格式的输出。

```python
from LIST_RECORDS import LIST_RECORDS

app_token = "appbcbWCzen6D8dezhoCH2RpMAh"
table_id = "tblKz5D60T4JlfcT"
page_token = "pgKz5D60T4JlfcT"
page_size = 10
config_file = "feishu-config.ini"

response_body = LIST_RECORDS(app_token, table_id, page_token, page_size, config_file)
print(json.dumps(response_body, indent=4))
```

以上示例会获取指定表格的记录列表，并将结果以 JSON 格式输出。

比如官方的示例响应体

```json
{
	"code": 0,
	"msg": "success",
	"data": {
		"has_more": true,
		"page_token": "recG70uhxh",
		"total": 8,
		"items": [{
			"fields": {
				"索引": "索引列多行文本类型",
				"多行文本": "多行文本内容1",
				"数字": "100",
				"单选": "选项1",
				"多选": ["选项1", "选项2"],
				"日期": 1674206443000,
				"复选框": true,
				"人员": [{
					"avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/b2-7619-4b8a-b27b-c72d90b06a2j~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp",
					"email": "zhangsan.leben@bytedance.com",
					"en_name": "ZhangSan",
					"id": "ou_2910013f1e6456f16a0ce75ede950a0a",
					"name": "张三"
				}, {
					"avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/v2_q86-fcb6-4f18-85c7-87ca8881e50j~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp",
					"email": "lisi.00@bytedance.com",
					"en_name": "LiSi",
					"id": "ou_e04138c9633dd0d2ea166d79f548ab5d",
					"name": "李四"
				}],
				"电话号码": "13126166666",
				"超链接": {
					"link": "https://bitable.feishu.cn",
					"text": "飞书多维表格官网"
				},
				"附件": [{
					"file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd",
					"name": "飞书.jpeg",
					"size": 32975,
					"tmp_url": "https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url?file_tokens=Vl3FbVk11owlgpxpqsAbBrtFcrd&extra={"bitablePerm":{"tableId":"tblBJyX6jZteblYv","rev":90}}",
					"type": "image/jpeg",
					"url": "https://open.feishu.cn/open-apis/drive/v1/medias/Vl3FbVk11owlgpxpqsAbBrtFcrd/download?extra={"bitablePerm":{"tableId":"tblBJyX6jZteblYv","rev":90}}"
				}],
				"单向关联": [{
					"record_ids": ["recnVYsuqV"],
					"table_id": "tblBJyX6jZteblYv",
					"text": "索引列多行文本类型",
					"text_arr": ["索引列多行文本类型"],
					"type": "text"
				}],
				"双向关联": [{
					"record_ids": ["recG70uhxh"],
					"table_id": "tblBJyX6jZteblYv",
					"text": "索引列多行文本类型",
					"text_arr": ["索引列多行文本类型"],
					"type": "text"
				}],
				"地理位置": {
					"address": "东长安街",
					"adname": "东城区",
					"cityname": "北京市",
					"full_address": "天安门广场，北京市东城区东长安街",
					"location": "116.397755,39.903179",
					"name": "天安门广场",
					"pname": "北京市"
				},
				"公式": [{
					"text": "false",
					"type": "text"
				}],
				"创建时间": 1675244156000,
				"更新时间": 1677556020000,
				"修改人": {
					"avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp",
					"email": "",
					"en_name": "测试1",
					"id": "ou_92945f86a98bba075174776959c90eda",
					"name": "测试1"
				},
				"创建人": {
					"avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp",
					"email": "",
					"en_name": "测试1",
					"id": "ou_92945f86a98bba075174776959c90eda",
					"name": "测试1"
				},
				"条码": "123",
				"查找引用": [{
					"text": "多行文本内容1",
					"type": "text"
				}],
				"自动编号-自定义": "017no20230201",
				"自动编号-默认": "17",
				"货币": "1",
				"进度": "0.66"
			},
			"id": "recG70uhxh",
			"record_id": "recG70uhxh"
		}]
	}
}
```