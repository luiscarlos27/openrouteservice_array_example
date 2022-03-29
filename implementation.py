import requests
import pandas as pd
import json

locations2 = [[-88.51, 18.044258333333],
              [-88.50, 18.082659999999],[-88.49424666666, 18.148731666666],
              [-88.49324333333, 18.155798333333],[-88.482095, 18.152313333333], [-88.48013333333, 18.14988],[-88.4925, 18.15439],
              [-88.50277, 18.153128333333],[-88.50955, 18.1528333], [-88.50345, 18.148745]]

body = {"locations":locations2,"metrics":["distance","duration"],"units":"m"}
headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': 'your-api-key',
    'Content-Type': 'application/json; charset=utf-8'
}
call = requests.post('http://localhost:8080/ors/v2/matrix/driving-car', json=body, headers=headers)

print(call.status_code, call.reason)
print(call.text)
temp = json.loads(call.text)
print(temp['durations'])
table = pd.DataFrame(temp['durations'])
table.head()

print(table)


