from GET_APP_ACCESS_TOKEN import GET_APP_ACCESS_TOKEN
from GET_FIELD_INFO import GET_FIELD_INFO, GET_FIELD_ID, GET_FIELD_NAME
from GET_INFO_FROM_URL import GET_INFO_FROM_URL,GET_INFO_FROM_URL_JSON,GET_APPTOKEN_FROM_URL,GET_TABLEID_FROM_URL,GET_VIEWID_FROM_URL
from GET_LOGIN_CODE import GET_LOGIN_CODE

class FeishuBitableAPI:
    def __init__(self):
        pass

    #GET_APP_ACCESS_TOKEN
    def GET_APP_ACCESS_TOKEN(self, app_id=None, app_secret=None, config_file=None):
        return GET_APP_ACCESS_TOKEN(app_id, app_secret, config_file)
    
    #GET_FIELD_INFO
    def GET_FIELD_INFO(self, field_name=None, field_id=None, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
        return GET_FIELD_INFO(field_name, field_id, app_token, table_id, view_id, page_token, page_size, config_file)
    def GET_FIELD_ID(self, field_name, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
        return GET_FIELD_ID(field_name, app_token, table_id, view_id, page_token, page_size, config_file)
    def GET_FIELD_NAME(self, field_id, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
        return GET_FIELD_NAME(field_id, app_token, table_id, view_id, page_token, page_size, config_file)

    #GET_INFO_FROM_URL
    def GET_INFO_FROM_URL(self, url):
        return GET_INFO_FROM_URL(url)
    def GGET_INFO_FROM_URL_JSON(self, url):
        return GET_INFO_FROM_URL_JSON(url)
    def GET_APPTOKEN_FROM_URL(self, url):
        return GET_APPTOKEN_FROM_URL(url)
    def GET_TABLEID_FROM_URL(self, url):
        return GET_TABLEID_FROM_URL(url)
    def GET_VIEWID_FROM_URL(self, url):
        return GET_VIEWID_FROM_URL(url)
    
    #GET_LOGIN_CODE
    def GET_LOGIN_CODE(self, redirect_uri=None, app_id=None, config_file=None):
        return GET_LOGIN_CODE(redirect_uri, app_id, config_file)