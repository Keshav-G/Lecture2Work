def interface():
	while True:
		print("/nBlood Test Analysis")
		print("Options")
		print("9 - Quit")
		choice = input("Enter an option: ")
		if choice == "9":
			return
def input_HDL_data():
	HDL_data = input("Please enter your HDL result: ")
	return int(HDL_data)

def analyze_HDL_data(result):
	if result >= 60:
		return "Normal"
	elif result >= 40 and result < 60:
		return "Borderline low"
	else:
		return "Low"

def output_HDL_data(result)
	print("Your HDL status is: " + result)

def HDL_driver():
	# Get Data
	HDL_result = input_HDL_data()
	
	# Analyze Data
	status = analyze_HDL_data(HDL_result)	
 
	# Output Data
	output_HDL_data(status)

interface()
HDL_driver()
