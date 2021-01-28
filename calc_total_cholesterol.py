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
			print("\nRunning HDL Driver")
			HDL_driver()
		elif choice == "2":
			print("\nRunning LDL Driver")
			LDL_driver()
		elif choice == "3":
			print("\nRunning Total Cholesterol Driver")
			Total_Cholesterol_Driver()
		else:
			print("Please enter 1, 2, 3, or 9")

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
# HDL Only Section
def output_HDL_data(result):
	print("Your HDL status is: " + result)

def HDL_driver():
	# Get Data
	HDL_result = input_HDL_data()
	
	# Analyze Data
	status = analyze_HDL_data(HDL_result)	
 
	# Output Data
	output_HDL_data(status)

# LDL Only Section
def input_LDL_data():
	LDL_data = input("Please enter your LDL result: ")
	return int(LDL_data)

def analyze_LDL_data(result):
	if result < 130:
		return "Normal"
	elif 130 <= result <= 159:
		return "Borderline High"
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


# Total Cholesterol Section
def analyze_total_data(LDL, HDL):
	total = LDL + HDL
	if total < 200:
		return "Normal"
	elif 200 <= total <= 239:
		return "Borderline High"
	else:
		return "High"

def output_total_data(result):
	print("Your total cholesterol level is: " + result)

def Total_Cholesterol_Driver():
	# Get Data
	LDL_result = input_LDL_data()
	HDL_result = input_HDL_data()
	
	# Analyze Data
	status = analyze_total_data(LDL_result, HDL_result)	
 
	# Output Data
	output_total_data(status)

interface()
