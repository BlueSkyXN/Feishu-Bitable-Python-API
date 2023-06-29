from GET_APP_ACCESS_TOKEN import GET_APP_ACCESS_TOKEN
from GET_FIELD_INFO import GET_FIELD_INFO, GET_FIELD_ID, GET_FIELD_NAME
from GET_INFO_FROM_URL import GET_INFO_FROM_URL,GET_INFO_FROM_URL_JSON,GET_APPTOKEN_FROM_URL,GET_TABLEID_FROM_URL,GET_VIEWID_FROM_URL
from GET_LOGIN_CODE import GET_LOGIN_CODE
from GET_RECORD_ID import GET_RECORD_ID
from GET_RECORD import GET_RECORD
from GET_TABLE_ID import GET_TABLE_ID
from GET_USER_ACCESS_TOKEN import GET_USER_ACCESS_TOKEN
from GET_VIEW_ID import GET_VIEW_ID


from LIST_FIELDS import LIST_FIELDS




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
    
    #GET_RECORD_ID
    def GET_RECORD_ID(self, field_value, field_name=None, config_file=None):
        return GET_RECORD_ID(field_value, field_name, config_file)
    
    #GET_RECORD
    def GET_RECORD(self, app_token=None, table_id=None, record_id=None, config_file=None):
        return GET_RECORD(app_token, table_id, record_id, config_file)
    
    #GET_TABLE_ID
    def GET_TABLE_ID(self, name="数据表", app_token=None, user_access_token=None, page_size=None, page_token=None, config_file=None):
        return GET_TABLE_ID(name, app_token, user_access_token, page_size, page_token, config_file)
    
    #GET_USER_ACCESS_TOKEN
    def GET_USER_ACCESS_TOKEN(self, login_code=None, app_access_token=None, config_file=None):
        return GET_USER_ACCESS_TOKEN(login_code, app_access_token, config_file)
    
    #GET_VIEW_ID
    def GET_VIEW_ID(self, view_name="默认视图", app_token=None, user_access_token=None, page_size=None, page_token=None, config_file=None):
        return GET_VIEW_ID(view_name, app_token, user_access_token, page_size, page_token, config_file)
    
    #LIST_FIELDS
    def LIST_FIELDS(self, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
        return LIST_FIELDS(app_token, table_id, view_id, page_token, page_size, config_file)

    


