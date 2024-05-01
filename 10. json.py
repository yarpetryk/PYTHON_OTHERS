data = [{
		"timestamp": 1666742425,
		"value": 510.26582278481015
	}, {
		"timestamp": 1666746002,
		"value": 439.5444444444444
	}, {
		"timestamp": 1666749607,
		"value": 416.32876712328766
	}, {
		"timestamp": 1666753214,
		"value": 485
	}, {
		"timestamp": 1666756805,
		"value": 1828.2967032967033
	}, {
		"timestamp": 1666760444,
		"value": 2441.3508771929824
	}, {
		"timestamp": 1666764016,
		"value": 2714.1688311688313
	}, {
		"timestamp": 1666767625,
		"value": 2628.652777777778
	}, {
		"timestamp": 1666771215,
		"value": 2593.284090909091
	}, {
		"timestamp": 1666774805,
		"value": 3842
	}, {
		"timestamp": 1666778403,
		"value": 4742
	}, {
		"timestamp": 1666782039,
		"value": 2638.983333333333
	}, {
		"timestamp": 1666785661,
		"value": -1606.327868852459
	}, {
		"timestamp": 1666789253,
		"value": -285.6666666666667
	}, {
		"timestamp": 1666792954,
		"value": 278.3369565217391
	}, {
		"timestamp": 1666796584,
		"value": 1052
	}, {
		"timestamp": 1666800015,
		"value": 799.5316455696203
	}, {
		"timestamp": 1666803629,
		"value": 1494
	}, {
		"timestamp": 1666807247,
		"value": 2809
	}, {
		"timestamp": 1666810946,
		"value": 2684.4418604651164
	}, {
		"timestamp": 1666814412,
		"value": 1616.627659574468
	}, {
		"timestamp": 1666818004,
		"value": 572
	}, {
		"timestamp": 1666821612,
		"value": 513.4375
	}, {
		"timestamp": 1666825284,
		"value": 380.1159420289855
	}]

suma_consumption = sum([el['value'] for el in data if el['value'] >= 0])
suma_feedin = sum([abs(el['value']) for el in data if el['value'] < 0])
print(suma_consumption, suma_feedin)


