from datetime import datetime


timestamp = datetime.now().strftime('%s')
data = [{
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683669600,
			"delta": 0.14575000000000002,
			"deltaCurrency": 0.3052768817204301,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683673200,

			"delta": 0.14800000000000002,
			"deltaCurrency": 0.3097768817204301,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683676800,

			"delta": 0.14700000000000002,
			"deltaCurrency": 0.3077768817204301,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683680400,

			"delta": 0.14550000000000002,
			"deltaCurrency": 0.3047768817204301,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683684000,

			"delta": 0.14575,
			"deltaCurrency": 0.3052768817204301,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683687600,

			"delta": 0.18975,
			"deltaCurrency": 0.3932768817204301,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683691200,

			"delta": 0.289,
			"deltaCurrency": 0.59177688172043,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683694800,

			"delta": 0.36850000000000005,
			"deltaCurrency": 0.7507768817204301,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683698400,

			"delta": 0.35400000000000004,
			"deltaCurrency": 0.7217768817204302,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683702000,

			"delta": 0.07925,
			"deltaCurrency": 0.1722768817204301,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683705600,

			"delta": 0.3115,
			"deltaCurrency": 0.6367768817204301,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683709200,

			"delta": 0.24300000000000002,
			"deltaCurrency": 0.4997768817204301,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683712800,

			"delta": 0.39825,
			"deltaCurrency": 0.8102768817204302,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683716400,

			"delta": 0.56875,
			"deltaCurrency": 1.15127688172043,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683720000,

			"delta": 0.15975000000000003,
			"deltaCurrency": 0.3332768817204301,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683723600,

			"delta": 0.028,
			"deltaCurrency": 0.06977688172043012,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683727200,

			"delta": 0.00525,
			"deltaCurrency": 0.024276881720430108,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683730800,

			"delta": 0.01125,
			"deltaCurrency": 0.0362768817204301,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683734400,

			"delta": 0.2275,
			"deltaCurrency": 0.4687768817204301,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683738000,

			"delta": 0.19199999999999998,
			"deltaCurrency": 0.39777688172043013,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683741600,

			"delta": 0.3135,
			"deltaCurrency": 0.64077688172043,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683745200,

			"delta": 0.27725,
			"deltaCurrency": 0.56827688172043,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683748800,

			"delta": 0.21500000000000002,
			"deltaCurrency": 0.44377688172043006,
			"valuesType": 1
		}, {
			"deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
			"timestamp": 1683752400,

			"delta": 0.14625,
			"deltaCurrency": 0.30627688172043005,
			"valuesType": 1
		}]
sum_consumption_1 = sum([el['delta'] for el in data])
sum_consumption_2 = sum([el['delta'] for el in data if el['timestamp'] < int(timestamp)])

#sum_feedin = sum([abs(el['delta']) for el in data if el['delta'] < 0])
#sum_generation = sum([el['value'] for el in data])
#x = [el['timestamp'] for el in data]
#timestamp = [(datetime.fromtimestamp(el['timestamp']).strftime('%H:%M'), el['timestamp']) for el in data]

print(sum_consumption_1)
print(sum_consumption_2)
print(timestamp)

test_data = [2, 3, 4, 5, 6]

result = [sum(el*el) for el in range(10)]

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

