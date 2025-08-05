# class Sample:
#     x = 'Ajmal'
#     def demo(self):
#         print(self.x ,'says hii')

# object=Sample()
# print(object.demo())


#...................................................


class Sample:
    def __init__(self,name,age):
        self.n1=name
        self.a1=age

    def display(self):
        print('..........details.....\n')
        print('\nName :',self.n1)
        print('\nage :',self.a1)

n=input('enter your name :')
a=int(input('enter your age :'))

obj=Sample(n,a)
print(obj.display())

obj1=Sample('s',2)
print(obj1.display())
