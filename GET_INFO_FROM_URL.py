import argparse
from urllib.parse import urlparse, parse_qs

def extract_parameters(url):
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)

    app_token = parsed_url.path.split('/')[-1]
    table_id = params.get('table', [None])[0]
    view_id = params.get('view', [None])[0]

    return app_token, table_id, view_id

def GET_APPTOKEN_FROM_URL(url):
    app_token, _, _ = extract_parameters(url)
    return app_token

def GET_TABLEID_FROM_URL(url):
    _, table_id, _ = extract_parameters(url)
    return table_id

def GET_VIEWID_FROM_URL(url):
    _, _, view_id = extract_parameters(url)
    return view_id

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=True, help='用于提取参数的URL')
    args = parser.parse_args()

    app_token, table_id, view_id = extract_parameters(args.url)

    print(f"app_token: {app_token}")
    print(f"table_id: {table_id}")
    print(f"view_id: {view_id}")
