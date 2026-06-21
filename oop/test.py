class Animal(object):
    '''
    动物类
    '''
    
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    '''
    狗类
    '''
    
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    '''
    猫类
    '''
    
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

def test():
    animal = Animal()
    # animal.run()
    dog = Dog()
    # dog.run()
    cat = Cat()
    # cat.run()
    run_twice(dog)
    print(dir(dog))


if __name__ == '__main__':
    test()     
