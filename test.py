from GET_INFO_FROM_URL import GET_INFO_FROM_URL, GET_INFO_FROM_URL_JSON, GET_APPTOKEN_FROM_URL, GET_TABLEID_FROM_URL, GET_VIEWID_FROM_URL

# 测试 GET_INFO_FROM_URL 函数
def test_GET_INFO_FROM_URL():
    url = "https://example.com/base/VwGhbo65BaYLaOsSz1nciWc5ncb?table=tblzDsYuQkXfoy9e&view=vewAgGXuqf"
    info = GET_INFO_FROM_URL(url)
    print("GET_INFO_FROM_URL:")
    print(f"URL: {url}")
    print(f"Info: {info}")
    print()

# 测试 GET_INFO_FROM_URL_JSON 函数
def test_GET_INFO_FROM_URL_JSON():
    url = "https://example.com/base/VwGhbo65BaYLaOsSz1nciWc5ncb?table=tblzDsYuQkXfoy9e&view=vewAgGXuqf"
    json_info = GET_INFO_FROM_URL_JSON(url)
    print("GET_INFO_FROM_URL_JSON:")
    print(f"URL: {url}")
    print(f"JSON Info: {json_info}")
    print()

# 测试 GET_APPTOKEN_FROM_URL 函数
def test_GET_APPTOKEN_FROM_URL():
    url = "https://example.com/base/VwGhbo65BaYLaOsSz1nciWc5ncb?table=tblzDsYuQkXfoy9e&view=vewAgGXuqf"
    app_token = GET_APPTOKEN_FROM_URL(url)
    print("GET_APPTOKEN_FROM_URL:")
    print(f"URL: {url}")
    print(f"App Token: {app_token}")
    print()

# 测试 GET_TABLEID_FROM_URL 函数
def test_GET_TABLEID_FROM_URL():
    url = "https://example.com/base/VwGhbo65BaYLaOsSz1nciWc5ncb?table=tblzDsYuQkXfoy9e&view=vewAgGXuqf"
    table_id = GET_TABLEID_FROM_URL(url)
    print("GET_TABLEID_FROM_URL:")
    print(f"URL: {url}")
    print(f"Table ID: {table_id}")
    print()

# 测试 GET_VIEWID_FROM_URL 函数
def test_GET_VIEWID_FROM_URL():
    url = "https://example.com/base/VwGhbo65BaYLaOsSz1nciWc5ncb?table=tblzDsYuQkXfoy9e&view=vewAgGXuqf"
    view_id = GET_VIEWID_FROM_URL(url)
    print("GET_VIEWID_FROM_URL:")
    print(f"URL: {url}")
    print(f"View ID: {view_id}")
    print()

# 执行测试函数
test_GET_INFO_FROM_URL()
test_GET_INFO_FROM_URL_JSON()
test_GET_APPTOKEN_FROM_URL()
test_GET_TABLEID_FROM_URL()
test_GET_VIEWID_FROM_URL()
