import numpy
import random

from faker import Faker
from iterablepythonwrapper.client import IterableApi

APIKEY="94c3333a8e224b32b93a40788d1927cc"

class GeneratData(object):
	"""docstring for DataGeneration"""
	def __init__(self, api_key, users=0, events=0):
		
		self.users = users
		self.events= events
		self.api_key= api_key


	def create_users(self):
		fake=Faker()
		ic = IterableApi(api_key=self.api_key)

		for i in range(self.users):

			u = fake.profile()
			u.pop('current_location')
			print('blah')
			email = u.pop('mail')
			print(u)

			ic.update_user(email=email, data_fields=u)


	def create_events(self):

		# creates distibution of events 
		events = numpy.random.randint(low=5, high=20, size=self.events)

		print(len(events))
		e = random.choice(events)

		print(e)



data = GenerateData(api_key=APIKEY, users=1, events=10)

data.create_events()
			
			




		