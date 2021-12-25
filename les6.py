class Animal:
    __population = []
    _protected_var = '_____'

    def __init__ (self, article, sex, carnivorous):
        self.sex = sex
        self.carnivorous = carnivorous
        self.article = article
        Animal.__population.append(self)

    def breeding(self, other):
        if self.sex is other.sex
            raise ValueError('Однополые браки обнулены!')
        return Animal(self.article, self.sex, other.carnivorous)

class Homo(Animal):

    def __init__(self, sex, name):
        super().__init__('Homo', sex, 'Any')
        self.name = name



some_ex = Animal('Рыба', 'M', False)
some_ex2 = Animal('Лошадь', 'F', True)
some_homo = Homo('M', 'ВАСЯ')
some_child = some_ex.breeding(some_ex2)
try:
    some_child2 = some_child.breeding(some_ex)
except ValueError as e:
    print(e)

print(1)

print(1)
