import json
import requests
import time

while True:
    actuation_value = {'data' : '4'}
    data_json = json.dumps(sensor_values)
    payload = data_json
    print(data_json)
    r = requests.get('http://host:port/route', json=payload)
    print(r.text)
    time.sleep(1)
