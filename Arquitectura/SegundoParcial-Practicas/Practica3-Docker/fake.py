from faker import Faker

fake = Faker()

for i in range(5):
    print(fake.email())
    #print(fake.md5())
    #print('----------------------------')

