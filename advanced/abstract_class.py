from abc import ABCMeta, abstractmethod

#abstract class是寫來被繼承的
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def make_sound(self):
        pass




class Dog(Animal):
    def make_sound(self):
        print('bark')

class Cat(Animal):
    def make_sound(self):
        print('meow')


class Person(Animal):
    def make_sound(self):
        print('hi')


d = Dog()
d.make_sound()
c = Cat()
c.make_sound()
p = Person()
p.make_sound()

