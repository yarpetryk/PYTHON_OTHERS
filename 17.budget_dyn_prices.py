import requests
from requests.auth import HTTPBasicAuth

def budget_dyn_price():

    url = "https://backend.powerfox.energy/api/3.0/report/0/consumption"
    auth = HTTPBasicAuth('lsqateam@gmail.com', 'Abc123!!')
    body = {
        "deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
        "division": 0,
        "mainDevice": True,
        "reportType": "monthlyValues",
        "startTime": 1714514400
    }

    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()
    print(data)

    result = sum(el['deltaCurrency'] for el in data['consumption']['reportValues'])
    print("Result: " + str(result))

budget_dyn_price()