import configparser
import argparse

from LIST_FIELDS import LIST_FIELDS
from UPDATE_FIELD import UPDATE_FIELD

def human_to_machine(app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):

    if config_file is None:
        config_file = 'feishu-config.ini'

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    # 如果参数为空，则使用配置文件中的默认值
    if not app_token:
        app_token = config.get('TOKEN', 'app_token')
    if not table_id:
        table_id = config.get('ID', 'table_id')



    fields_map = dict(config.items('FIELD_MAP'))

    # 获取当前的字段
    current_fields = LIST_FIELDS(app_token=app_token, table_id=table_id, view_id=view_id, page_token=page_token, page_size=page_size, config_file=config_file)

    # 遍历当前的字段
    for field in current_fields['data']['items']:
        # 检查当前字段是否在映射中
        if field['field_name'] in fields_map:
            field_id = field['field_id']  # 获取字段的ID
            field_name = fields_map[field['field_name']]  # 获取字段的映射名称
            # 如果在，则更新字段名
            UPDATE_FIELD(app_token=app_token, table_id=table_id, field_id=field_id, field_name=field_name, field_type=1)


def machine_to_human(app_token=None, table_id=None, view_id=None, page_token=None, page_size=None, config_file=None):

    if config_file is None:
        config_file = 'feishu-config.ini'

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    # 如果参数为空，则使用配置文件中的默认值
    if not app_token:
        app_token = config.get('TOKEN', 'app_token')
    if not table_id:
        table_id = config.get('ID', 'table_id')
    if not field_type:
        field_type = config.getint('LIST_FIELDS', 'field_type', fallback=1)
        
    fields_map = dict(config.items('FIELD_MAP'))

    # 获取当前的字段
    current_fields = LIST_FIELDS(app_token=app_token, table_id=table_id, view_id=view_id, page_token=page_token, page_size=page_size, config_file=config_file)

    # 反转字典映射
    reversed_fields_map = {v: k for k, v in fields_map.items()}

    # 遍历当前的字段
    for field in current_fields['data']['items']:
        # 检查当前字段是否在反转映射中
        if field['field_name'] in reversed_fields_map:
            # 如果在，则更新字段名
            #UPDATE_FIELD(app_token=app_token, table_id=table_id, field_id=field['field_id'], field_name=reversed_fields_map[field['field_name']], field_type=1)
            field_id = field['field_id']  # 获取字段的ID
            field_name = reversed_fields_map[field['field_name']] # 获取字段的映射名称
            UPDATE_FIELD(app_token=app_token, table_id=table_id, field_id=field_id, field_name=field_name, field_type=1)

def CONVERSION_FIELDS_CMD():

    parser = argparse.ArgumentParser(description='Human-to-Machine and Machine-to-Human Field Name Conversion')

    parser.add_argument('-c', '--convert_to_machine', action='store_true', help='Convert human field names to machine field names')
    parser.add_argument('-b', '--convert_to_human', action='store_true', help='Convert machine field names to human field names')
    parser.add_argument('--app_token', default=None, help='App Token')
    parser.add_argument('--table_id', default=None, help='Table ID')
    parser.add_argument('--view_id', default=None, help='View ID')
    parser.add_argument('--page_token', default=None, help='Page Token')
    parser.add_argument('--page_size', default=None, help='Page Size')
    parser.add_argument('--config_file', default='feishu-config.ini', help='Config file path')

    args = parser.parse_args()

    if args.convert_to_machine:
        human_to_machine(app_token=args.app_token, table_id=args.table_id, view_id=args.view_id,
                         page_token=args.page_token, page_size=args.page_size, config_file=args.config_file)
    elif args.convert_to_human:
        machine_to_human(app_token=args.app_token, table_id=args.table_id, view_id=args.view_id,
                         page_token=args.page_token, page_size=args.page_size, config_file=args.config_file)
    else:
        print("Please specify either -c or -b option for field name conversion.")

if __name__ == '__main__':
    CONVERSION_FIELDS_CMD()