import csv
import json
import requests
import time

from iterable_wrapper import IterableAPI

# Iterable Instance Credentials 
API_KEY = "94c3333a8e224b32b93a40788d1927cc"

# Instantiate the Iterable API Wrapper Class

ic = IterableAPI(api_key=API_KEY)


def user_update(file):
	
	reader = csv.DictReader(open(str(file), 'r'))

	# Format data in the CSV file so we can make the request
	dictlist = []

	for row in reader:
		dictlist.append(row)

	# loop through each user in list
	for user in dictlist:	
		user_id = None
		# store email, which is used as unique identifier in Iterable API
		email = user.pop("email")
		if "userId" in user:
			user_id = user["userId"]
		# 'user' variable will hold all data related to user('dataFields), which we store
		# in separate key per API docs
		ic.update_user(email=email, data_fields=user, user_id=user_id)
	
	
#Bulk User Update	

def bulk_update(file):
	
	reader = csv.DictReader(open(str(file), 'r'))

	# Format data in the CSV file so we can make the request
	dictlist = []

	for row in reader:

   		dictlist.append(row)

	# chunk data into groups of 50 so we can make reqeusts per Iterable 
	# bulk_update documentation

	# had some trouble with this but found the below list comprehension on
	# stack that worked-- want to work to make this easier to read
	chunks = ([dictlist[i:i + 50] for i in range(0, len(dictlist), 50)])

	#formatting each chunk to work with API 
	for chunk in chunks:
		bulk = []
		for i in chunk:

			person = {}
			user_id = None
			email = i["email"]

			if "userId" in i:
				user_id = i["userId"]

			i.pop("email")
			person["email"] = email
			person["dataFields"] = i
			bulk.append(person)


		ic.bulk_update_user(users= bulk)

# Delete User

def delete_user():
	ic.delete_user(email="carter@gmail.com")

print("working?")

# delete_user()

# API Call #1- User Update

# user_update(file="csv/se_assignment_users.csv")

# Api Call #2- Bulk User Update

# bulk_update(file="se_assignment_users.csv")


