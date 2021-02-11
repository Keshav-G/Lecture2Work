def test_analyze_HDL_data_1():
	from blood_tests import analyze_HDL_data as HDL
	result1 = HDL(39)
	actual1 = "Low"
	assert result1 == actual1

def test_analyze_HDL_data_2():
	from blood_tests import analyze_HDL_data as HDL
	result2 = HDL(40)
	actual2 = "Borderline Low"
	assert result2 == actual2

def test_analyze_HDL_data_3():
	from blood_tests import analyze_HDL_data as HDL
	result3 = HDL(50)
	actual2 = "Borderline Low"
	assert result3 == actual2

def test_analyze_HDL_data_4():
	from blood_tests import analyze_HDL_data as HDL
	result4 = HDL(59)
	actual2 = "Borderline Low"
	assert result4 == actual2

def test_analyze_HDL_data_5():
	from blood_tests import analyze_HDL_data as HDL	
	result5 = HDL(60)
	actual3 = "Normal"
	assert result5 == actual3

def test_analyze_HDL_data_6():
	from blood_tests import analyze_HDL_data as HDL
	result6 = HDL(70)
	actual3 = "Normal"
	assert result6 == actual3
