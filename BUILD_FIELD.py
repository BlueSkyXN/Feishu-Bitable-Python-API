import configparser
import csv
import json
import argparse

def BUILD_FIELD(csv_file="input.csv", config_file="feishu-field.ini"):
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    
    records = []
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        field_names = reader.fieldnames

        for field_name in field_names:
            if field_name not in config.sections():
                config[field_name] = {'type': 'string'}
        with open(config_file, 'w', encoding='utf-8') as configfile:
            config.write(configfile)
        
        for row in reader:
            fields = {}
            for field_name, field_value in row.items():
                if field_name in config.sections():
                    field_type = config[field_name]['type']
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

    request_body = {'records': records}
    return request_body

def BUILD_FIELD_CMD():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default="feishu-field.ini", help='Configuration file')
    parser.add_argument('-f', '--file', default="input.csv", help='CSV file')
    args = parser.parse_args()
    request_body = BUILD_FIELD(args.file, args.config)
    print(json.dumps(request_body, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    BUILD_FIELD_CMD()
