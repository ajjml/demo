class dog:
    def sound(self):
        print("barkkkk....")
class cat:
    def sound(self):
        print("meow....")
def make_a_sound(animal):
    animal.sound()

a=dog()
b=cat()
make_a_sound(a)
make_a_sound(b)

