import configparser
import csv
import json
import os

def read_config(config_file):
    # 读取feishu-field.ini配置文件
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    return config

def update_config(config, config_file, field_names):
    # 如果配置文件中不存在当前CSV文件的字段，就添加到配置文件中
    for field_name in field_names:
        if field_name not in config.sections():
            config[field_name] = {'type': 'string'}  # 默认添加为string类型
    # 将更新后的配置文件保存
    with open(config_file, 'w', encoding='utf-8') as configfile:
        config.write(configfile)

def build_fields(config, csv_file):
    # 创建空的记录列表
    records = []
    # 读取CSV文件
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        field_names = reader.fieldnames
        update_config(config, 'feishu-field.ini', field_names)

        for row in reader:
            fields = {}
            for field_name, field_value in row.items():
                if field_name in config.sections():
                    field_type = config[field_name]['type']
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
    return records

def main():
    config_file = 'feishu-field.ini'
    csv_file = 'input.csv'
    config = read_config(config_file)
    records = build_fields(config, csv_file)

    # 创建请求体
    request_body = {'records': records}

    print(json.dumps(request_body, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()
