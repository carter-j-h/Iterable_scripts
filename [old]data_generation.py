from faker import Faker

fake=Faker()

bucket=[]

for i in range(0,10):
	person = fake.profile

	bucket.append(person)


print(bucket)