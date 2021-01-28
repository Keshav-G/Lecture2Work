def interface():
	while True:
		print("\nBlood Test Analysis")
		print("Options")
		print("1 - HDL Analysis")
		print("2 - LDL Analysis")
		print("3 - Total Cholesterol Level Analysis")
		print("9 - Quit")
		choice = input("Enter an option: ")
		if choice == "9":
			return
		elif choice == "1":
			print("Running HDL Driver")
			HDL_driver()
		elif choice == "2":
			print("Running LDL Driver")
			LDL_driver()
		elif choice == "3":
			print("Running Total Cholesterol Driver")
			Total_Cholesterol_Driver()
		else:
			"Please enter 1, 2, 3, or 9"

def input_HDL_data():
	HDL_data = input("Please enter your HDL result: ")
	return int(HDL_data)

def analyze_HDL_data(result):
	if result >= 60:
		return "Normal"
	elif 40 <= result < 60:
		return "Borderline low"
	else:
		return "Low"

def output_HDL_data(result):
	print("Your HDL status is: " + result)

def HDL_driver():
	# Get Data
	HDL_result = input_HDL_data()
	
	# Analyze Data
	status = analyze_HDL_data(HDL_result)	
 
	# Output Data
	output_HDL_data(status)

interface()
