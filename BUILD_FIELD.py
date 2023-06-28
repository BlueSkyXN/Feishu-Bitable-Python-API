import csv
import configparser
import json
import argparse

def BUILD_FIELD(csv_file=None, config_file=None):
    if config_file is None:
        config_file = 'feishu-field.ini'
    if csv_file is None:
        csv_file = 'input.csv'

    # 读取CSV文件的第一行（字段名称）
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        field_names = next(reader)

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    # 如果配置文件中不存在'FIELD_TYPE' section，就创建一个
    if not config.has_section('FIELD_TYPE'):
        config.add_section('FIELD_TYPE')

    # 如果配置文件中不存在当前CSV文件的字段，就添加到配置文件中
    for field_name in field_names:
        if not config.has_option('FIELD_TYPE', field_name):
            config.set('FIELD_TYPE', field_name, 'string')  # 默认添加为string类型

    # 决定是否将请求体写入配置文件
    save_to_config = False

    # 创建空的记录列表
    records = []

    # 读取CSV文件
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            fields = {}
            for field_name, field_value in row.items():
                if config.has_option('FIELD_TYPE', field_name):
                    field_type = config.get('FIELD_TYPE', field_name)
                    # 根据飞书API字段类型进行数据转换
                    if field_type == 'number':
                        field_value = int(field_value)
                    elif field_type == 'boolean':
                        field_value = bool(field_value)
                    elif field_type == 'array':
                        field_value = field_value.split(',')
                    elif field_type == 'object':
                        field_value = json.loads(field_value)
                    fields[field_name] = field_value
            records.append({'fields': fields})

    # 构建请求体
    request_body = {'records': records}
    
    if save_to_config:
        # 如果配置文件中不存在'BUILD_FIELD' section，就创建一个
        if not config.has_section('BUILD_FIELD'):
            config.add_section('BUILD_FIELD')
        config.set('BUILD_FIELD', 'request_body', json.dumps(request_body, ensure_ascii=False))
        with open(config_file, 'w', encoding='utf-8') as configfile:
            config.write(configfile)

    return request_body


def BUILD_FIELD_CMD():
    parser = argparse.ArgumentParser(description='Build Feishu field from CSV file.')
    parser.add_argument('-i', '--input', default="input.csv", help='Input CSV file.')
    parser.add_argument('-c', '--config', default="feishu-field.ini", help='Configuration file.')
    args = parser.parse_args()
    request_body = BUILD_FIELD(args.input, args.config)
    print(json.dumps(request_body, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    BUILD_FIELD_CMD()
