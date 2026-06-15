# student.py

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def printScore(self):
        print(f'{self.name}: {self.score}')