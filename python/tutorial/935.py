class Dog:
    tricks = []

    def __init__(self,name):
        self.name = name
    
    def add_trick(self,trick):
        self.tricks.append(trick)

d = Dog('fibo')
e = Dog('buddy')
d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks)

