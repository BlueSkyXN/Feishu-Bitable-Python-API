import argparse
from LIST_DATATABLES import LIST_DATATABLES

def GET_TABLE_ID(name="数据表"):
    response = LIST_DATATABLES()

    for item in response["data"]["items"]:
        if item["name"] == name:
            return item["table_id"]

    return "NONE"

def GET_TABLE_ID_CMD():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default="数据表", help='数据表的名字')
    args = parser.parse_args()
    table_id = GET_TABLE_ID(args.input)
    print(table_id)

if __name__ == "__main__":
    GET_TABLE_ID_CMD()
