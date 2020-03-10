
import sys
class Person:

    def get_info(self):
        print ("2222")
# <unbound method Person.get_info>
a=Person.get_info
print (a)
a(Person())
# bound method Person.get_info
b=Person().get_info
print (b)
print (b.__name__)
print (sys.__name__)