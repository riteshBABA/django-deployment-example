import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django
django.setup()

from  appTwo.models import Users
from faker import Faker
import random


fake = Faker()

def population(n=5):

    for entry in range(n):
        fake_name = fake.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        fake_email = fake.email()

        users = Users.objects.get_or_create(fname = fake_fname, 
                                            lname = fake_lname, 
                                            email = fake_email)[0]


if __name__== '__main__':
    print("Started populating")
    population(15)
    print("Data Populated")