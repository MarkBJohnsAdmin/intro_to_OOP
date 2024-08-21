import re

class Person():
    '''Custom data type to represent people'''
    job = None
    population = 0
    
    @staticmethod
    def format_name(name):
        cleaned_name = re.sub(r'[^a-zA-Z]', '', name)
        formatted_name = cleaned_name.lower().capitalize()
        return formatted_name
    
    def __init__(self, name, age):
        self.name = Person.format_name(name)
        self.age = age
        Person.population += 1
        
    def __str__(self):
        if self.job:
            return f"{self.name}, {self.job}, {self.age} years old"
        else:
            return f"{self.name}, {self.age} years old"
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __ne__(self, other):
        return self.age != other.age
        
    def __lt__(self, other):
        return self.age < other.age
    
    def __le__(self, other):
        return self.age <= other.age
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __ge__(self, other):
        return self.age >= other.age
        
    def say_hello(self):
        print(f"Hello, my name is {self.name}")
        
    @classmethod
    def crnt_pop(cls):
        return cls.population


class Programmer(Person):
    '''Class for super smart computer people like us'''
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.job = "programmer"
        self.langugage = language
          
    def do_programming_stuff(self):
        print(f"I, {self.name}, did a really cool thing with {self.langugage}")

        
class Runner(Person):
    '''Class for the clinically insane'''
    def __init__(self, name, age, shoes):
        super().__init__(name, age)
        self.job = "runner"
        self.shoes = shoes
        
    def run_a_marathon(self):
        print(f"I, {self.name}, need a new pair of {self.shoes} so I can run a marathon and talk about it all the time")
        
mark = Programmer(name="Mark", age=29, language="Python")
joey = Runner(name="Joey", age=29, shoes="Nike")
leonard = Person(name="leo3narD", age=77)

class MathemathicalOperations:
    '''Resuable math functions'''
    
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y == 0:
            return "cannot divide by 0"
        return x / y
    
    @staticmethod
    def square(x):
        return x * x
    
math_ops = MathemathicalOperations()
    