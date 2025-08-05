#single Inheritence

#one child class inherits from one parent class

#syntax
# class parent:
#     fuction1

# class child(parent):
#     function2

# obj=child()

#Eg:

class Collage():
    def open(self):
        return 'College Open'
class Student(Collage):
    def msg(self):
        return 'New Student'

obj=Student()
print(obj.msg())