# Object Oriented Programming

## Index

+ [Why OOP?](#why-oop)
+ [Classes](#classes)
  + [Data Types](#data-types)
  + [Custom Classes](#custom-classes)
  + [Order Comparisons](#order-comparisons)
+ [Inheritance](#inheritance)
  + [Bad Option 1](#bad-option-1)
  + [Bad Option 2](#bad-option-2)
  + [The Good Option](#the-good-option)
+ [Base Class Strategies](#base-class-strategies)
+ [Helper Classes](#helper-classes)
  + [Bad Fix](#bad-fix)
  + [Good Fix](#good-fix)
+ [Method Types](#method-types)
  + [Instance Methods](#instance-methods)
  + [Class Methods](#class-methods)
  + [Static Methods](#static-methods)
+ [Full Code](#full-code)

## Why OOP?

Say we have a collection of people we want to keep track of. An efficient way to keep track people-related data in Python would be dictionaries, which lets you store a collection of data values that can be called with a key.

```py
mark = {
    "name": "Mark",
    "age": 29,
}

mark['name'] # Mark
mark['age'] # 29
```

We also want our people to be able to do basic tasks, such as introduce themselves to other people. We could make an external function that takes in a person dictionary:

```py
def say_hello(person):
    print(f"Hello, my name is {person['name']}")
    
say_hello(mark) # Hello, my name is Mark
```

And this works for any other objects you pass into the function, assuming each of them have a `name` key:

```py
say_hello(john) # Hello, my name is John

say_hello(steven) # Hello, my name is Steven
```

And so on. This works well enough, but we start to run into a scalability problem. For now, the people dictionaries are small, but there's a lot more to people than just their ages and names:

```py
mark = {
    "name": "Mark",
    "age": 29,
    "height": "6'0",
    "weight": 190,
    "eye_color": "blue",
    "hair_color": "brown",
    "likes": [
        "good books",
        "long walks on the beach"
    ],
    "hates": [
        "country music",
        "the cramp in your leg where your muscle feels like it's twisting into itself"
    ],
    # and on and on and on and on and...
}
```

And even after you've gotten into all the niche aspects of an individual person, you have to do the whole process over again for every other person. Once you have all of the people set up, you still need the people to do things, but some people can do things others can't, and there's no organized way to handle this:

```py
def do_programming_stuff(dev):
    return the_correct_result
    
def run_a_marathon(runner):
    return an_impressive_physical_feat
    
do_programming_stuff(mark) # works great because I am a very smart Python dev

run_a_marathon(mark) # Error: I am so very unhealthy

do_programming_stuff(runner) # Error: this dude isn't a programmer

run_a_marathon(runner) # nobody likes a show-off
```

In addition to the sheer amount of work and difficulty organizing your people, this approach also leads to a ton of copy/pasting at best, and at worst, a lot of time waisted rewritting code and a much higher risk of making subtle typos that can crash your whole program. If only there were a process that scaled efficiently, incorporated important functions, and allowed us to avoid unorganized, repetitive code...

## Classes

### Data Types

If you've written any Python at all, you're already familiar with classes, whether you know it or not. Just about everything in Python, including functions and all the data types, are something called an `object`. Objects have `properties` and `methods` that store data and call functions with inherent data values. You can test this by creating a string:

```py
test_string = "hello world"
```

This `test_string` variable is a string, which is a data type native to Python. Strings don't quite have keys like dictionaries do, but they do still have some properties that are more or less 'hidden' using `dunder`, or "double-under" property names:

```py
print(test_string.__class__) # <class 'str'>
```

Accessing the `class` property of the string returns that strings are, in fact, part of the `str` class. But more important that niche, hidden properties of default classes are their methods. A method is a function created in a class, and atttached to the `instance` of that class. Before explaining what that means, I'll just show an example:

```py
string_1 = "first string"

string_1.upper() # 'FIRST STRING'

string_2 = "second string"

string_2.upper() # 'SECOND STRING'
```

Here, `.upper()` is a string method, meaning that every single string, no matter the size, value, or location, has access to a function called "upper", which converts lowercase letters to uppercase. But you'll notice that no parameters were added to the "upper" function, and that instead of being called externally, it's directly attached to the string itself by a period. That's because behind the scenes, when you create a string variable, you're actually creating an instance of the string class. Here, "upper" is using a method on instance data, which is why the method (lowercase to uppercase conversions) is the same, but the values (the actual word content) is unique. What you don't see is that "upper" is actually using a parameter, a special variable in Python called `self`, which we'll go over in more detail next.

### Custom Classes

It's good to have a basic understanding of how Python's classes work, because you can make your own custom classes, using the `class` keyword. Classes look very similar to dictionaries, but can also include methods, and need a bit more explicit of a set up that just wrapping data in braces. We need to declare "class", name the class (it's standard to capitalize the first letter), and use a special dunder method called `__init__`.

```py
class Person:
    '''Custom data type to represent people'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

The "init" method is a special function that runs once, when the instance is `instantiated` (which is just a fancy programmer way to say "created an instance"). You don't need to call it yourself, it happens automatically, and it's arguably the most important method the class can have. The "self" that allows the instance to call methods with unique data is set up here, by making it the first parameter of init, but both the values and amounts of following parameters are up to you and what you want the class to handle. This function is mandatory* and should be the first function in your class, but you can create any number of other methods your class might need after setting the initialization process up:

\**this isn't actually mandatory but don't worry about why for now*

```py
class Person:
    '''Custom data type to represent people'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print(f"Hello, my name is {self.name}")
```

Instead of an external function with a person dictionary manually plugged in, we can now say "Hello" as a built in function for all of the people objects we create, with each of the "self" values automatically applied. To instantiate your class, use the class name as a keyword and set the values as an argument.

```py
mark = Person(name="Mark", age=29)

mark.say_hello() # Hello, my name is Mark
```

In addition to our custom methods, there are more standard dunder methods you can add to your class to help users work with them. For example, getting some kind of normalized naming convention for the instances. Right now, if you enter "print(mark)" into ipython, you don't get anything particularly useful:

```py
print(mark) # <__main__.Person at 0x&fa36b0a40d0>
```

This just tells the user that this is an instance of `Person`, that it was written in the `main.py` file, and the memory address it's being stored in. Which is cool and all, but nothing about this data helps the user understand what it's for. We can override this default value using another dunder method, `__str__`:

```py
class Person:
    ...
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    ...
```

So now, when the user tries to see what's going on with "mark", they'll get details instead:

```py
print(mark) # Mark, 29 years old
```

### Order Comparisons

You've probably used order comparisons before, as they're pretty standard in all programming languages:

```py
1 > 0 # True
1 == 1 # True
2 < 1 # False
```

But Python doesn't know this magically. Remember that all data types are objects, and that includes integers. The way Python makes these comparisons between data types are with ordering dunder methods:

+ `__eq__(self, other)`: Defines equality comparisons (==)
+ `__ne__(self, other)`: Defines inequality comparisons (!=)
+ `__lt__(self, other)`: Defines less than comparisons (<)
+ `__le__(self, other)`: Defines less than or equal to comparisons (<=)
+ `__gt__(self, other)`: Defines greater than comparisons (>)
+ `__ge__(self, other)`: Defines greater than or equal comparisons (>=)

We can use these to see how instances of our class compare to each other. We have a good amount of freedom to decide what this even means, as with non-number based data types, it isn't perfectly clear what makes one instance greater, lesser, or equal to another. For this example, let's just go with the age value.

```py
class Person:
    '''Custom data type to represent people'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
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
        
        
mark = Person(name="Mark", age=29)
joey = Person(name="Joey", age=29)
leonard = Person(name="Leonard", age=77)

mark == joey # True
joey != leonard # True
mark > leonard # False
```

And so on. You can also use dunder methods to handle when your instances are added, substracted, mulitplied or divided together, as well as any of other basic operations you can perform with the default data types, but I'll let you look into that more on your own time.

## Inheritance

Earlier I mentioned that with loose people dictionaries, we had to write disconnected functions and pass the dictionaries into them manually. In addition to being inefficient, this creates problems when the functions rely on specific types of people, and will fail if they aren't those specific people types. OOP gets around the organization issue by placing the methods inside of the class, but how does it handle the methods that need specific people to operate?

### Bad Option 1

We could just create other classes:

```py
class Programmer:
    '''Class for people who are also programmers'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print(f"Hello, my name is {self.name}")
        
    def do_programming_stuff()
        print(f"I, {self.name}, have performed programming stuff")
        
class Runner:
    '''Class for crazy people who torture themselves'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print(f"Hello, my name is {self.name}")
        
    def run_a_marathon(self):
        print(f"I, {self.name}, am a show-off")
```

But this just runs into the same repetition we started using classes to avoid, as we need to copy `say_hello()`, and any other standardized methods we think of later to every new class that we create.

### Bad Option 2

We could also set up Person to handle all sorts of edge cases:

```py
class Person:
    '''Very complex and messy class for every possible type of person'''
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        
    def say_hello(self):
        print(f"Hello, my name is {self.name}")
        
    def do_programming_stuff(self):
        if self.job == "programmer":
            print(f"I, {self.name}, have performed programming stuff")
        else:
            print(f"I, {self.name}, am not a programmer")
            
    def run_a_marathon(self):
        if self.job == "runner":
            print(f"I, {self.name}, am a show-off")
        else:
            print(f"I, {self.name}, like sleeping in and breathing normally")
```

But this presents plenty of its own issues. For one, we're writing potentially hundreds of methods for every conceivable type of person, that the majority of Person instances will never need to use. Second, having the user input the job they want the user to have also complicates things, as even without typos, they might put "developer" instead of "programmer", or "unhinged lunatic" instead of "runner".

### The Good Option

There is a way to maintain all the utility of the Person class while adding unique utility, and putting a lot of the process on rails to prevent user (or, let's be honest, developer) error, and that's by using something called `inheritance`. When you make a class, you can inherent an other class as a starting point, which gives your new class access to everything in the initial class, as well as anything you want to add.

In order to inherit another class, you need to 1) pass the inherited class as a parameter to the new class, and 2) utilize a special function called ``super()``. The "super" function is what allows you to access everything from the first class into the new class

```py
class Programmer(Person):
    '''Class for super smart computer people like us'''
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.job = "programmer"
        self.langugage = language
        
    def do_programming_stuff(self):
        print(f"I, {self.name}, did a really cool thing with {self.langugage}")
```

Part of instantiating an inherting class is calling the "init" function of the first class in the "init" function of the second class, which you can see above following the `super()` function. Note that the `job` attribute isn't passed in, but is automatically generated when a new instance of Programmer is made. Also note that `language` is declared separately from `name` and `age`. This is because name and age are set up in Person, while language isn't used until it gets to Programmer.

So when you create a new Programmer, you have access to all the values and methods of Person without needing to set them up again:

```py
mark = Programmer(name="Mark", age=29, language="Python")

mark.do_programming_stuff() # I, Mark, did a really cool thing in Python

mark.say_hello() # Hello, my name is Mark
```

This allows you to keep all the generic functionality of Person, while adding all the cool hacking techniques that programmers have. It also allows you to create different types of people with their own unique attributes, without needing to constantly check for various properties before doing so.

```py
class Runner(Person):
    '''I'm out of jokes, I just think running a lot on purpose is crazy'''
    def __init__(self, name, age, shoes):
        super().__init__(name, age)
        self.job = "runner"
        self.shoes = shoes
        
    def run_a_marathon(self):
        print(f"I, {self.name}, need a new pair of {person.shoes} so I can run a marathon and talk about it all the time")
```

If we had the Person class check their job property for do_programming_stuff() and run_a_marathon(), it wouldn't immediately be clear what each Person was capable of, and it'd be a waste of time and memory to give an object a method that will fail 99% of the time. But by separating our concerns into sub-classes, we can be sure that all Programmers make cool stuff and all Runners torture themselves successfully, and we don't need to sacrifice any of the functionality the Person class affords us to do so.

## Base Class Strategies

If you know your building that class that will be inherited, it's a good idea to program the class with that flexibility in mind. For example, we know that we're extending our Person class based around their jobs. We already set up a __str___ method for Person, with just the name and age of the person. This still isn't all the useful, but with the new classes, we can set up a method that includes what that object does as well.

We could give each new class their own naming method:

```py
class Programmer(Person):
    ...
    def __str__(self):
        return f"{self.name}, {self.job}, {self.age} years old"
        
class Runner(Person):
    ...
    def __str__(self):
        return f"{self.name}, {self.job}, {self.age} years old"
```

But remember, we're trying to save time and code less. We can actually avoid having to set a new __str___ for all of our new functions by adding a little bit of extra functionality to Person.

```py
class Person:
    ...
    
    job = None
    
    def __str__(self):
        if self.job:
            return f"{self.name}, {self.job}, {self.age} years old"
        else:
            return f"{self.name}, {self.age} years old"
```

By setting the job value outside of the `__init__` method, we don't let the user determine the value, and instead let the value default to `None` for every instance of Person. Having the str dunder check for a truthy job value makes it so it will always return f"{self.name}, {self.age} years old" when called on an instance of Person, but will always return f"{self.name}, {self.job}, {self.age} years old" when called on an instance of any class that inherits Person.

```py
mark = Programmer(name="Mark", age=29, language="Python")

joey = Runner(name="Joey", age=29, shoes="Nike")

leonard = Person(name="Leonard", age=77)

print(mark) # Mark, programmer, 29 years old

print(joey) # Joey, runner, 29 years old

print(leonard) # Leonard, 77 years old
```

## Helper Classes

Earlier I mentioned that the `__init__` function isn't actually mandatory for your classes, and that's because not all classes will be instantiated. Say you're running a program that uses a lot of math, and repeats the same operations multiple times throughout the code base. A good place to store all these various functions for ease of use would be in a class:

```py
class MathemathicalOperations:
    '''Resuable math functions'''
    def add(x, y):
        return x + y
    
    def subtract(x, y):
        return x - y
    
    def multiply(x, y):
        return x * y
    
    def divide(x, y):
        if y == 0:
            return "cannot divide by 0"
        return x / y
    
    def square(x):
        return x * x
```

Now throughout your code, when you need to make some calculation, you can call the MathematicalOperations class itself and call the methods inside:

```py
MathematicalOperations.add(5, 5) # 10

MathematicalOperations.subtract(99, 45) # 54

MathematicalOperations.multiply(22, 33) # 66

MathematicalOperations.divide(208, 16) # 13

MathematicalOperations.square(4) # 16
```

Python already has a built in `math` module, so this class in particular isn't very useful, but for more complex or custom operations, having a helper class to handle those processes can make your life a whole lot easier.

That being said, this class is incomplete, and a pretty common process can break the whole thing.

"MathematicalOperations" is a pretty long name for an object you'll want to be recalling very often, so a normal workaround is to rename longer objects into something short and sweet:

```py
math_ops = MathematicalOperations()
```

This should allow you to use all the same operations on the much shorter object name, but there's a problem:

```py
math_ops.add(2, 2)

# TypeError: MathematicalOperations.add() takes 2 positional arguments but 3 were given
```

You're not crazy, there are, in fact, only two numbers in `math_ops(2, 2)`, but take a closer look at the other classes. You may notice that do_programming_stuff() in the Programmer class takes in self as a parameter, but when you call the method on an instance, no parameter is passed in:

```py
class Programmer(Perosn):
    ...
    def do_programming_stuff(self):
        ...
        
mark = Programmer(name="Mark", age=29, language="Python")

mark.do_programming_stuff() # I, Mark, did a really cool thing in Python
```

Even though no `__init__` method was explicity written, declaring math_ops still created an instance of MathematicalOperations, creating a self property that gets passed into method call. We include the self paramater in all our methods to account for this, and our math methods failed because we didn't. We have two ways to work around this.

### Bad Fix

We just add the self parameter into each of our methods and call it a day:

```py
class Math:
    '''Resuable math functions'''
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            return "cannot divide by 0"
        return x / y
    
    def square(self, x):
        return x * x
```

### Good Fix

But a better habit to get into is to use `decorators` to give the methods a `static` property:

```py
class Math:
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
```

The `@staticmethod` decorator makes it so the method doesn't need to use the "self" value when it's called, allowing you to create an instance with a short name and not sacrifice any functionality. The reason this is better than just adding self to functions that don't need it is because more complex classes can have a combination of `instance methods`, which are methods that utilize a specific instance of a class, `class methods`, which are methodss that access data from the class itself rather than any instance in particular, and `static methods` which operate completely independently, but are stored in an object for convenience and utility.

## Method Types

### Instance Methods

These methods tend to get the biggest benefit of being in classes, as they give you the benefits of having unique and customizable data while still having the structure that comes with a uniform data type. All instance functions need the have the self parameter, as they utilize specific instance data.

```py
class Person:
    ...
    def say_hello(self):
        print(f"Hello, my name is {self.name}")
```

`say_hello()` is an instance method because the output will be different and unique to every instance of Person (or any other class that inherits Person).

### Class Methods

These methods are still tied to the class, but to the entire class rather than an specific instance of it. You'll likely see new() or create() or something along those lines as what's called a `factory method`, which means a class method that creates a new instance of that class:

```py
class ClassName:
    ...
    
    @classmethod
    def create_new(cls, value):
        return cls(value)
        
new_instance = ClassName.create_new("value")
```

But it can also be a useful way to store data about all of the instances. For example, if we're dealing with a lot of people, it might be a good idea to have something of a census. We can make a value called `population` and use class methods to keep track of it:

```py
class Person:
    ...
    population = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1
    
    @classmethod
    def crnt_pop(cls):
        return cls.population
```

A good benefit of setting this up in the base class is that the population also increases for every new instance of a Programmer and Runner too, as they both inherit Person. Being a class method means that you can call it on every single instance of every single Person and Person-adjacent class, as well as on the Person and every Person-adjacent class itself:

```py
mark = Programmer(name="Mark", age=29, language="Python")

mark.crnt_pop() # 1

joey = Runner(name="Joey", age=29, shoes="Nike")

Runner.crnt_pop() # 2
```

### Static Methods

These are the helper functions that don't utilize either the instance or the class, but are stored along with them for organization and ease of access. It's also useful if you want to format the data the user gives you into a different structure before you make it an actual value, such as fixing any issues with the name:

```py
import re # reformatting module

class Person:
    ...
    
    @staticmethod
    def format_name(name):
        cleaned_name = re.sub(r'[^a-zA-Z]', '', name)
        formatted_name = cleaned_name.lower().capitalize()
        return formatted_name
        
    def __init__(self, name, age):
        self.name = Person.format_name(name)
        self.age = age
        Person.population += 1
        
leonard = Person(name="leo3narD", age=77)

leonard.name # Leonard
```

There's no reason `format_name` needs to be directly inside the Person class, but because it's entirely relevant to creating Person names, it's beneficial to have it directly attached. That way if there's any issue with the logic or new functionality needs to be added, the developer doesn't need to look for the function doing the work.

## Full Code

```py
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
```
