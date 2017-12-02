import csv
import time
import requests
import json

# Marketo Instance Credentials 
url = "https://298-TCJ-281.mktorest.com"
client_id = "649686eb-fbb6-4eeb-823d-4710fec8a25b"
client_secret = "cvGN7iYCgPLl7xcWWa9jdXoehCdOHUSC"


class MarketoAPI():
	"""docstring for MarketoAPI"""	

	def __init__(self, url, client_id, client_secret):
		
		self.url = url
		self.client_id = client_id
		self.client_secret = client_secret
		self.expire_time = 0
		# as soon as we instantiate class we want to grab an access token so we can make requests
		self.access_token = self.grant_access_token()

	def grant_access_token(self):
		
		r = requests.get(self.url+"/identity/oauth/token?grant_type=client_credentials&client_id="+self.client_id+"&client_secret="+self.client_secret)
		
		if (r.status_code==200):
			data = r.json()
			# access token comes back in seconds, so we want to keep track when this token will expire so we can 
			# refresh it when necessary
			self.expire_time = time.time() + data["expires_in"]
			# store the access token
			self.access_token = data["access_token"]
			return data["access_token"]
		else:
			raise Exception(str(r.raise_for_status()))


	def reset_expire_time(self, expiresIn):
		self.expire_time = time.time() + expiresIn

	def api_call(self, method, call, params=None, headers=None, data=None, json=None):

		if params is None:
			params = {}
		if headers is None:
			headers = {}
		if data is None:
			data = {}
		if json is None:
			json ={}
		if data is None:
			data ={}

		# this is where we check to verify the access token is valid
		# if it is not, we refresh and attempt to get a new valid token
		if self.expire_time < time.time():
			self.access_token = self.grant_access_token()

		# store the access token in the header per Marketo documentation
		headers["Content-type"] = "application/json"
		headers["Authorization"] = "Bearer "+self.access_token

		# marke the request following the 'requests.request' method
		r = requests.request(method=method, url=self.url+call, params=params,
							 headers=headers, data=data, json=json)
		print(r.raise_for_status())
		return r.json()


	def get_lead_by_id(self, lead):

		call = "/rest/v1/leads/"+str(lead)+".json?"
		method = "GET"
		return self.api_call(method, call)


	def get_campaigns(self, workspace_name):

		call = "/rest/v1/campaigns.json?"
		method = "GET"
		params = workspace_name

		return self.api_call(method, call, params)

	def push_to_marketo(self, leads, action="createOrUpdate", lookup_field=None,
						 program_name=None):

		call = "/rest/v1/leads/push.json?"
		method = "POST"
		payload = {"input": leads}
		if action is not None:
			payload["action"] = str(action)
		if lookup_field is not None:
			payload["lookupField"] = str(lookup_field)
		if program_name is not None:
			payload["programName"] = str(program_name)
		if program_name is None:
			payload["programName"] = "Marketing Campaign"

		# reqeusts module allows you to pass json directly via a 'json' parameter
		# instead of encoding the dictionary
		return self.api_call(method, call, json=payload)



# Instantiate class
mc = MarketoAPI(url, client_id, client_secret)

# print(mc.grant_access_token())
# print(mc.access_token)
# print(mc.get_lead_by_id(5))
# print(mc.get_campaigns("Default"))

reader = csv.DictReader(open('se_assignment_users.csv', 'r'))
# reader = csv.DictReader(open('marketo_test.csv', 'r'))


dictlist = []
for row in reader:
   dictlist.append(row)


chunks = ([dictlist[i:i + 50] for i in range(0, len(dictlist), 50)])

print(len(chunks))
# for c in chunks:

# 	mc.push_to_marketo(leads=c)






		