def interface():
	while True:
		print("\nLDL Blood Test Analysis")
		print("Options")
		print("1 - LDL Analysis")
		print("9 - Quit")
		choice = input("Enter an option: ")
		if choice == "9":
			return
		if choice == "1":
			print("Running LDL Driver")
			LDL_driver()
def input_LDL_data():
	LDL_data = input("Please enter your LDL result: ")
	return int(LDL_data)

def analyze_LDL_data(result):
	if result < 130:
		return "Normal"
	elif 130 <= result <= 159:
		return "Borderline high"
	elif 160 <= result <= 189:
		return "High"
	else:
		return "Very High"

def output_LDL_data(result):
	print("Your LDL status is: " + result)

def LDL_driver():
	# Get Data
	LDL_result = input_LDL_data()
	
	# Analyze Data
	status = analyze_LDL_data(LDL_result)	
 
	# Output Data
	output_LDL_data(status)

interface()
