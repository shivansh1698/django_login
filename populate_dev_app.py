import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','starter_pro.settings')

import django
django.setup()

import random
from dev_app.models import people

firstnames = ['mike','john','kate','alice','perry','tommy','ralphie']
lastnames = ['smith','johnson','brown','cullens','jackson','hendricks']
domains = ['gmail','ymail','facebook','orkut','instagram','whatsapp','twitter']
numbers = [1,2,3,4,5,6,7,8,9,0]


def add_people():
    fn = random.choice(firstnames)
    ln = random.choice(lastnames)
    dom = random.choice(domains)
    em = str(fn) + str(ln) + str(random.choice(numbers)) + "@" + str(dom) + ".com"
    p = people.objects.get_or_create(FirstName=fn,LastName=ln,Email=em)[0]
    p.save()
    return p

def populate(N=10):
    for i in range(N):
        person = add_people()

if __name__== '__main__':
    print("populating script")
    populate(10)
    print("populating complete")