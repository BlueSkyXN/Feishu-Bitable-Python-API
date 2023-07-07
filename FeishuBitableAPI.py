from GET_APP_ACCESS_TOKEN import GET_APP_ACCESS_TOKEN
from GET_FIELD_INFO import GET_FIELD_INFO, GET_FIELD_ID, GET_FIELD_NAME
from GET_INFO_FROM_URL import GET_INFO_FROM_URL, GET_INFO_FROM_URL_JSON, GET_APPTOKEN_FROM_URL, GET_TABLEID_FROM_URL, GET_VIEWID_FROM_URL
from GET_LOGIN_CODE import GET_LOGIN_CODE
from GET_RECORD_ID import GET_RECORD_ID
from GET_RECORD import GET_RECORD
from GET_TABLE_ID import GET_TABLE_ID
from GET_USER_ACCESS_TOKEN import GET_USER_ACCESS_TOKEN
from GET_VIEW_ID import GET_VIEW_ID

from LIST_FIELDS import LIST_FIELDS
from LIST_RECORDS import LIST_RECORDS
from LIST_TABLES import LIST_TABLES
from LIST_VIEWS import LIST_VIEWS

from REFRESH_USER_ACCESS_TOKEN import REFRESH_USER_ACCESS_TOKEN

from WRITE_APP_ACCESS_TOKEN import WRITE_APP_ACCESS_TOKEN
from WRITE_FIELD_INFO import WRITE_FIELD_INFO
from WRITE_INFO_FROM_URL import WRITE_INFO_FROM_URL
from WRITE_LOGIN_CODE import WRITE_LOGIN_CODE
from WRITE_RECORD_ID import WRITE_RECORD_ID
from WRITE_TABLE_ID import WRITE_TABLE_ID
from WRITE_VIEW_ID import WRITE_VIEW_ID

from CREATE_FIELD import CREATE_FIELD
from CREATE_TABLE import CREATE_TABLE

from CHECK_FIELD_EXIST import CHECK_FIELD_EXIST
from CHECK_FIELD_EXIST_SQL import CHECK_FIELD_EXIST_SQL

from DELETE_FIELDS import DELETE_FIELD
from DELETE_RECORD import DELETE_RECORD

from BUILD_FIELD import BUILD_FIELD

from UPDATE_FIELD import UPDATE_FIELD
from UPDATE_RECORD import UPDATE_RECORD

from ADD_RECORDS_FROM_CSV import ADD_RECORDS_FROM_CSV

from CONVERSION_FIELDS import CONVERSION_FIELDS_HUMAN_TO_MACHINE, CONVERSION_FIELDS_MACHINE_TO_HUMAN


class FeishuBitableAPI:
    def __init__(self):
        pass

    # 调用 ping 函数进行验证
    def ping(self):
        print("pong")
        return "pong"

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

    #LIST_RECORDS
    def LIST_RECORDS(self, app_token=None, table_id=None, page_token=None, page_size=None, config_file=None):
        return LIST_RECORDS(app_token, table_id, page_token, page_size, config_file)
    
    #LIST_TABLES
    def LIST_TABLES(self, app_token=None, user_access_token=None, page_size=None, page_token=None, config_file=None):
        return LIST_TABLES(app_token, user_access_token, page_size, page_token, config_file)
    
    #LIST_VIEWS
    def LIST_VIEWS(self, app_token=None, user_access_token=None, page_size=None, page_token=None, table_id=None, config_file=None):
        return LIST_VIEWS(app_token, user_access_token, page_size, page_token, table_id, config_file)
    
    #REFRESH_USER_ACCESS_TOKEN
    def REFRESH_USER_ACCESS_TOKEN(self, app_access_token=None, refresh_token=None, config_file=None):
        return REFRESH_USER_ACCESS_TOKEN(app_access_token, refresh_token, config_file)
    
    #WRITE_APP_ACCESS_TOKEN
    def WRITE_APP_ACCESS_TOKEN(self, app_id=None, app_secret=None, config_file=None):
        return WRITE_APP_ACCESS_TOKEN(app_id, app_secret, config_file)
    
    #WRITE_FIELD_INFO
    def WRITE_FIELD_INFO(self, field_name=None, field_id=None, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
        return WRITE_FIELD_INFO(field_name, field_id, app_token, table_id, view_id, page_token, page_size, config_file)
    
    #WRITE_INFO_FROM_URL
    def WRITE_INFO_FROM_URL(self, url, config_file="feishu-config.ini"):
        return WRITE_INFO_FROM_URL(url, config_file)
    
    #WRITE_LOGIN_CODE
    def WRITE_LOGIN_CODE(self, redirect_uri=None, app_id=None, config_file=None):
        return WRITE_LOGIN_CODE(redirect_uri, app_id, config_file)
    
    #WRITE_RECORD_ID
    def WRITE_RECORD_ID(self, value, field_name=None, config_file=None):
        return WRITE_RECORD_ID(value, field_name, config_file)
    
    #WRITE_TABLE_ID
    def WRITE_TABLE_ID(self, name, app_token=None, user_access_token=None, page_size=None, page_token=None, config_file=None):
        return WRITE_TABLE_ID(name, app_token, user_access_token, page_size, page_token, config_file)
    
    #WRITE_VIEW_ID
    def WRITE_VIEW_ID(self, view_name, app_token=None, user_access_token=None, page_size=None, page_token=None, config_file=None):
        return WRITE_VIEW_ID(view_name, app_token, user_access_token, page_size, page_token, config_file)
   
    #CREATE_FIELD
    def CREATE_FIELD(self, field_name, field_type=None, app_token=None, table_id=None, config_file=None):
        return CREATE_FIELD(field_name, field_type, app_token, table_id, config_file)
    
    #CREATE_TABLE
    def CREATE_TABLE(self, app_token=None, table_name=None, default_view_name=None, fields=None, config_file=None, fields_file=None):
        return CREATE_TABLE(app_token, table_name, default_view_name, fields, config_file, fields_file)
    
    #CHECK_FIELD_EXIST
    def CHECK_FIELD_EXIST(self, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, csv_file=None, config_file=None):
        return CHECK_FIELD_EXIST(app_token, table_id, view_id, page_token, page_size, csv_file, config_file)
    def CHECK_FIELD_EXIST_CSV(self, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, csv_file=None, config_file=None):
        return CHECK_FIELD_EXIST(app_token, table_id, view_id, page_token, page_size, csv_file, config_file)
    
    #CHECK_FIELD_EXIST_SQL
    def CHECK_FIELD_EXIST_SQL(self, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
        return CHECK_FIELD_EXIST_SQL(app_token, table_id, view_id, page_token, page_size, config_file)

    #DELETE_FIELDS
    def DELETE_FIELD(self, app_token=None, table_id=None, field_id=None, config_file=None):
        return DELETE_FIELD(app_token, table_id, field_id, config_file)
    
    #DELETE_RECORD
    def DELETE_RECORD(self, app_token=None, table_id=None, record_id=None, config_file=None):
        return DELETE_RECORD(app_token, table_id, record_id, config_file)
    
    #BUILD_FIELD
    def BUILD_FIELD(self, csv_file=None, config_file=None):
        return BUILD_FIELD(csv_file, config_file)

    #UPDATE_FIELD
    def UPDATE_FIELD(self, app_token=None, table_id=None, field_id=None, field_name=None, field_type=None, config_file=None):
        return UPDATE_FIELD(app_token, table_id, field_id, field_name, field_type, config_file)
    
    #UPDATE_RECORD
    def UPDATE_RECORD(self, app_token=None, table_id=None, record_id=None, fields=None, config_file=None):
        return UPDATE_RECORD(app_token, table_id, record_id, fields, config_file)
    
    #ADD_RECORDS_FROM_CSV
    def ADD_RECORDS_FROM_CSV(self, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, csv_file=None, config_file=None, field_file=None):
        return ADD_RECORDS_FROM_CSV(app_token, table_id, view_id, page_token, page_size, csv_file, config_file, field_file)
    
    #CONVERSION_FIELDS
    def CONVERSION_FIELDS_HUMAN_TO_MACHINE(self, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
        return CONVERSION_FIELDS_HUMAN_TO_MACHINE(app_token, table_id, view_id, page_token, page_size, config_file)
    def CONVERSION_FIELDS_MACHINE_TO_HUMAN(self, app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
        return CONVERSION_FIELDS_MACHINE_TO_HUMAN(app_token, table_id, view_id, page_token, page_size, config_file)
