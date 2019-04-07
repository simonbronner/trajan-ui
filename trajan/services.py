from datetime import datetime
import requests
import os

def generate_trajan_url(ticker, d_from, d_to):
    trajan_url = os.environ.get('TRAJAN_SERVICE_URL', "http://localhost:8000/")
    if not d_to:
        return (trajan_url + "stock/%s/%s" % (ticker, d_from))
    return (trajan_url + "stock/%s/%s/%s" % (ticker, d_from, d_to))

def process_record(r):
    day_as_date = datetime.strptime(r.get('day'), '%Y-%m-%dT%H:%M:%SZ')
    r.update({'day' : day_as_date})
    return r

def invoke_trajan_service(ticker, d_from, d_to):
    url = generate_trajan_url(ticker, d_from, d_to)
    r = requests.get(url)
    status_code = r.status_code
    if status_code != 200:
        return (status_code, None)
    result = list(map(process_record, r.json()))
    return (status_code, result)
