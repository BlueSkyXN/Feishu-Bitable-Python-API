from GET_INFO_FROM_URL import GET_APPTOKEN_FROM_URL, GET_TABLEID_FROM_URL, GET_VIEWID_FROM_URL

class FeishuBitableAPI:
    def __init__(self):
        pass

    def get_app_token_from_url(self, url):
        return GET_APPTOKEN_FROM_URL(url)

    def get_table_id_from_url(self, url):
        return GET_TABLEID_FROM_URL(url)

    def get_view_id_from_url(self, url):
        return GET_VIEWID_FROM_URL(url)