import csv

# http wrapper for the Iterable Api
from iterablepythonwrapper.client import IterableApi


def file_upload(file):
	
	f = open(file)
	reader = csv.reader(f)

	# Stores first row fiels names to be referenced later
	fields = next(reader)
	rows = list(reader)
	#print(len(rows))
	for i in range(0, len(rows), 2):
		chunks =[]
		print(reader[i])



print(file_upload(file='sample-csv/mock_data.csv'))