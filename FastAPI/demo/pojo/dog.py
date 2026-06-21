class Dog(object):
    """Dog类"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'Dog {self.name} is running...')

    def eat(self):
        print(f'Dog {self.name} is eating meat...')
