import pandas as pd

def create_csv(file_name, output_one, output_two):
	"""
	The main function used to complete Task #1
	Takes in a CSV file, then creates two new files.
	The first new file is the same as the input file, and the second new file is the transposed version of the input file

	Args:
		FileName: The name of the  CSV file to read.
		output_one: The first output file to write to, will contain the contents of FileName.
		output_two: The second output file to write to, will contain the reversed contents of FileName.
	"""
	file = pd.read_csv(file_name, header=None)
	file.to_csv(output_one, header=False, index=False)
	file.T.to_csv(output_two, header=False, index=False)

if __name__ == "__main__":
	create_csv("gender_submission.csv","Output.csv","Output2.csv")
