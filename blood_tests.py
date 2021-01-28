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

def HDL_driver():
	# Get Data
	input_HDL_data()
	
	# Analyze Data
	analyze_HDL_data()	
 
	# Output Data
	output_HDL_data

interface()
