from faker import Faker
import random

fake = Faker()

domains = ['@pridemail.com' , '@zingermail.com' , '@whoamail.com' , '@oofmail.com']

def main():
    number_of_emails = int(input("How many emails you want?: "))


    for i in range(number_of_emails):
        name = fake.name()
        name = name.replace(" ","")
        name = name.lower()

        num = random.randint(0,1000)
        num = str(num)

        domain = random.choice(domains)

        e_name = name
        e_name += num

        full_email = e_name+domain

        url = "https://mailsac.com/inbox/"

        #print(url+e_name+domain)
        print(full_email)
        #print('======================')


main()