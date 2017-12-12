from faker import Faker
from iterablepythonwrapper.client import IterableApi

APIKEY="94c3333a8e224b32b93a40788d1927cc"





class DataGeneration(object):
	"""docstring for DataGeneration"""
	def __init__(self, users=0, events=0):
		
		self.users = users
		self.events= events


	def create_users(self):
		fake=Faker()
		ic = IterableApi(api_key=APIKEY)

		for i in range(self.users):

			u = fake.profile()
			u.pop('current_location')

			email = u.pop('mail')
			print(u)

			ic.update_user(email=email, data_fields=u)



data = DataGeneration(users=1, events=0)

data.create_users()
			
			




		