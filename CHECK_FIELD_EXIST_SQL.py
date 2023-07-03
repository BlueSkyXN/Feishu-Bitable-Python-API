import configparser
import pymysql
from LIST_FIELDS import LIST_FIELDS
from CREATE_FIELD import CREATE_FIELD

def CHECK_FIELD_EXIST_SQL(app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):
    if config_file is None:
        config_file = 'feishu-config.ini'

    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    if not app_token:
        app_token = config.get('TOKEN', 'app_token')
    if not table_id:
        table_id = config.get('ID', 'table_id')
    if not view_id:
        view_id = config.get('ID', 'view_id')
    if not page_token:
        page_token = config.get('LIST_FIELDS', 'page_token', fallback=None)
    if not page_size:
        page_size = config.get('LIST_FIELDS', 'page_size', fallback=100)

    # 获取飞书中的字段列表
    response = LIST_FIELDS(app_token=app_token, table_id=table_id, view_id=view_id, page_token=page_token, page_size=page_size, config_file=config_file)
    feishu_fields = [item['field_name'] for item in response['data']['items']]

    # 获取数据库表的列名
    db_host = config.get('DB', 'host')
    db_user = config.get('DB', 'user')
    db_password = config.get('DB', 'password')
    db_database = config.get('DB', 'database')
    db_port = config.getint('DB', 'port')

    conn = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_database, port=db_port)
    cursor = conn.cursor()

    check_query = config.get('SQL', 'check_query')
    cursor.execute(check_query)
    db_columns = [column[0] for column in cursor.fetchall()]

    conn.close()

    # 检查每个需要检查的字段是否在飞书字段列表中，如果不在，就创建新的字段
    for column in db_columns:
        if column not in feishu_fields:
            CREATE_FIELD(field_name=column, field_type=1, app_token=app_token, table_id=table_id, config_file=config_file)
            print(f"字段 {column} 已成功创建")

if __name__ == "__main__":
    # 调用函数进行字段检查和创建
    CHECK_FIELD_EXIST_SQL(config_file='feishu-config.ini')
