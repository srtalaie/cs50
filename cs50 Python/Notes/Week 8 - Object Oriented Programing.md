## Tuples
student.py
```
def main():
	name = get_name()
	house = get_house()
	print(f"{name} from {house}")

def get_name():
	return input("Name: ")

def get_house():
	return input("House: ")

if __name__ == "__main__":
	main()
```

```
def main():
	name, house = get_student()
	print(f"{name} from {house}")

def get_student():
	name = input("Name: ")
	house = input("House: ")
	return name, house
	
if __name__ == "__main__":
	main()
```
- Tuples - type of data that is a collection of values, different from a list as it is immutable. Above `return name, house` is not two values but a tuple and one value. You can use parentheses to explicitly designate it as a tuple `return (name, house)`. Tuples can be indexed similarly to lists.

```
def main():
	student = get_student()
	print(f"{student[0]} from {student[1]}")

def get_student():
	name = input("Name: ")
	house = input("House: ")
	return (name, house)
	
if __name__ == "__main__":
	main()
```
- You use a tuple instead of a list when you know the values are not going to be changed
## Dictionaries
- Dictionaries collection of keys and values. Allows you to semantically associate keys to their values
student.py
```
def main():
	student = get_student()
	print(f"{student['name']} from {student['house']}")

def get_student():
	name = input("Name: ")
	house = input("House: ")
	return {"name": name, "house": house}
	
if __name__ == "__main__":
	main()
```
- Dictionaries like lists are mutable
## Classes and Objects
- Allows you to create your own data types
- Class - a blueprint for pieces of data that you can re-use. Primary feature of object oriented programming
 student.py
```
class Student:
	

def main():
	student = get_student()
	print(f"{student.name} from {student.house}")

def get_student():
	student = Student()
	student.name = input("Name: ")
	student.house = input("House: ")
	return student
	
if __name__ == "__main__":
	main()
```
- Classes have `attributes` that are properties that they hold inside of them. They are accessed using the `.` dot operator. Also known as `instance variables`
- Anytime you create a class you are using objects
- Setting `student = Student()` you are creating a `Student` object or creating an instance of the `Student` class
```
class Student:
	

def main():
	student = get_student()
	print(f"{student.name} from {student.house}")

def get_student():
	name = input("Name: ")
	house = input("House: ")
	student = Student(name, house)
	return student
	
if __name__ == "__main__":
	main()
```
- You can pass in arguments into classes to allow for error-checking
## Instance Methods
- Classes come with certain methods that you can define. They allow you to determine behavior in a standard way.
student.py
```
class Student:
	def __init__(self, name, house):
		self.name = name
		self.house = house

def main():
	student = get_student()
	print(f"{student.name} from {student.house}")

def get_student():
	name = input("Name: ")
	house = input("House: ")
	return Student(name, house)
	
if __name__ == "__main__":
	main()
```
- `__init__` - used to initialize the contents of the class
- `student = Student(name, house)` -  a constructor call that is creating the instance of `Student`
```
class Student:
	def __init__(self, name, house):
		if not name:
			raise ValueError("Missing Name")
		if house not in ["Gryffindor","Hufflepuff","Ravenclaw", "Slytherin"]:
			raise ValueError("Invalid House")
		self.name = name
		self.house = house

def main():
	student = get_student()
	print(f"{student.name} from {student.house}")

def get_student():
	name = input("Name: ")
	house = input("House: ")
	try:
		return Student(name, house)
	except Value:
		print("Error")
	
if __name__ == "__main__":
	main()
```
- `raise` - keyword used to raise exceptions
## String Method
- `__str__` - special method that if called will display object as string
```
class Student:
	def __init__(self, name, house):
		if not name:
			raise ValueError("Missing Name")
		if house not in ["Gryffindor","Hufflepuff","Ravenclaw", "Slytherin"]:
			raise ValueError("Invalid House")
		self.name = name
		self.house = house
		
	def __str__(self):
		return(f"{self.name} from {self.house}")

def main():
	student = get_student()
	print(f"{student.name} from {student.house}")

def get_student():
	name = input("Name: ")
	house = input("House: ")
	try:
		return Student(name, house)
	except Value:
		print("Error")
	
if __name__ == "__main__":
	main()
```
## Custom Methods
```
class Student:
	def __init__(self, name, house, patronus):
		if not name:
			raise ValueError("Missing Name")
		if house not in ["Gryffindor","Hufflepuff","Ravenclaw", "Slytherin"]:
			raise ValueError("Invalid House")
		self.name = name
		self.house = house
		self.patronuns = patronus
		
	def __str__(self):
		return(f"{self.name} from {self.house}")

	def charm(self):
		match self.patronus:
			case "Stag":
				return "🦌"
			case "Otter":
				return "🦦"
			case "Jack Russell Terrier":
				return "🐕"
			case _:
				return "🪄"

def main():
	student = get_student()
	print("Expecto Patronum!")
	print(student.charm())

def get_student():
	name = input("Name: ")
	house = input("House: ")
	patronus = input("Patronus: ")
	try:
		return Student(name, house, patronus)
	except Value:
		print("Error")
	
if __name__ == "__main__":
	main()
```
## Properties, Getters, and Setters
- Properties - an attribute that has more defense mechanisms put into place and allow the programmer with more control over them. Use the keyword `@property`
- Properties can be utilized to harden our code. In Python, we define properties using function “decorators”, which begin with `@`.
```
class Student:
	def __init__(self, name, house):
		self.name = name
		# Still calls the setter method
		self.house = house
		
	def __str__(self):
		return(f"{self.name} from {self.house}")

	# Getter
	@property
	def name(self):
		return self._name
		
	# Setter
	@name.setter
	def name(self, name):
		if not name:
			raise ValueError("Missing Name")
		self._name = name
		
	# Getter
	@property
	def house(self):
		return self._house

	# Setter
	@house.setter
	def house(self, house):
		if house not in ["Gryffindor","Hufflepuff","Ravenclaw", "Slytherin"]:
					raise ValueError("Invalid House")
		self._house = house

def main():
	student = get_student()
	print(student)

def get_student():
	name = input("Name: ")
	house = input("House: ")
	try:
		return Student(name, house)
	except Value:
		print("Error")
	
if __name__ == "__main__":
	main()
```
- `Getter` - function in a class that gets an attribute. Defined as `@property` above the function and the function is named exactly like what you want the property to be called
- `Setter` function in a class that sets an attribute. Defined as name of the getter function with setter before it `@house.setter`
-  Why `_house` and not `house`? `house` is a property of our class, with functions via which a user attempts to set our class attribute. `_house` is that class attribute itself. The leading underscore, `_`, indicates to users they need not (and indeed, shouldn’t!) modify this value directly. `_house` should _only_ be set through the `house` setter. Notice how the `house` property simply returns that value of `_house`, our class attribute that has presumably been validated using our `house` setter. When a user calls `student.house`, they’re getting the value of `_house` through our `house` “getter”.
## Types and Classes
- While not explicitly stated in past portions of this course, you have been using classes and objects the whole way through.
- If you dig into the documentation of `int`, you’ll see that it is a class with a constructor. It’s a blueprint for creating objects of type `int`. You can learn more in Python’s documentation of [`int`](https://docs.python.org/3/library/functions.html#int).
- Strings too are also a class. If you have used `str.lower()`, you were using a method that came within the `str` class. You can learn more in Python’s documentation of [`str`](https://docs.python.org/3/library/stdtypes.html#str).
- `list` is also a class. Looking at that documentation for `list`, you can see the methods that are contained therein, like `list.append()`. You can learn more in Python’s documentation of [`list`](https://docs.python.org/3/library/stdtypes.html#list).
- `dict` is also a class within Python. You can learn more in Python’s documentation of [`dict`](https://docs.python.org/3/library/stdtypes.html#dict).
- To see how you have been using classes all along, go to your console and type `code type.py` and then code as follows:
    
    ```
    print(type(50))
    ```
    
    Notice how by executing this code, it will display that the class of `50` is `int`.
    
- We can also apply this to `str` as follows:
    
    ```
    print(type("hello, world"))
    ```
    
    Notice how executing this code will indicate this is of the class `str`.
    
- We can also apply this to `list` as follows:
    
    ```
    print(type([]))
    ```
    
    Notice how executing this code will indicate this is of the class `list`.
    
- We can also apply this to a `list` using the name of Python’s built-in `list` class as follows:
    
    ```
    print(type(list()))
    ```
    
    Notice how executing this code will indicate this is of the class `list`.
    
- We can also apply this to `dict` as follows:
    
    ```
    print(type({}))
    ```
    
    Notice how executing this code will indicate this is of the class `dict`.
    
- We can also apply this to a `dict` using the name of Python’s built in `dict` class as follows:
    
    ```
    print(type(dict()))
    ```
    
    Notice how executing this code will indicate this is of the class `dict`.
## Class Methods
-   Sometimes, we want to add functionality to a class itself, not to instances of that class.
- `@classmethod` is a function that we can use to add functionality to a class as a whole.
hat.py
```
import random

class Hat:
	def __init__(self):
		self.houses =["Gryffindor","Hufflepuff","Ravenclaw", "Slytherin"]
		
	def sort(self, name):
		house = random.choice(self.houses)
		print(f"{name} is in {house}")

hat = Hat()
hat.sort("Harry")
```

```
$ python hat.py
Harry is in Slytherin
```
- We may want, though, to run the `sort` function without creating a particular instance of the sorting hat (there’s only one, after all!). We can modify our code as follows:
hat.py
```
import random

class Hat:
	houses =["Gryffindor","Hufflepuff","Ravenclaw", "Slytherin"]

	@classmethod
	def sort(cls, name):
		print(f"{name} is in {random.choice(cls.houses)}")

Hat.sort("Harry")
```
- Notice how the `__init__` method is removed because we don’t need to instantiate a hat anywhere in our code. `self`, therefore, is no longer relevant and is removed. We specify this `sort` as a `@classmethod`, replacing `self` with `cls`. Finally, notice how `Hat` is capitalized by convention near the end of this code, because this is the name of our class.
- student.py
```
class Student:
	def __init__(self, name,house):
		self.name = name
		self.house = house

	def __str__(self):
		reutrn f"{self.name} from {self.house}"

	@classmethod
	def get(cls):
		name = input("Name: ")
		house = input("House: ")
		return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()
```
## Inheritance
- Inheritance is, perhaps, the most powerful feature of object-oriented programming.
- It just so happens that you can create a class that “inherits” methods, variables, and attributes from another class.
wizard.py
```
class Wizard:
	def __init__(self, name):
		if not name:
			raise ValueError("Missing Name")
		self.name = name

class Student(Wizard):
	def __init__(self, name, house):
		super().__init__(name)
		self.house = house
		
class Professor(Wizard):
	def __init__(self, name, subject):
		super().__init__(name)
		self.subject = subject
```
- Notice that there is a class above called `Wizard` and a class called `Student`. Further, notice that there is a class called `Professor`. Both students and professors have names. Also, both students and professors are wizards. Therefore, both `Student` and `Professor` inherit the characteristics of `Wizard`. Within the “child” class `Student`, `Student` can inherit from the “parent” or “super” class `Wizard` as the line `super().__init__(name)` runs the `init` method of `Wizard`. Finally, notice that the last lines of this code create a wizard called Albus, a student called Harry, and so on.
## Operator Overloading
- Some operators such as `+` and `-` can be “overloaded” such that they can have more abilities beyond simple arithmetic.
vault.py
```
class Vault:
	def __init__(self, galleons=0, sickles=0, knuts=0):
		self.galleons = galleons
		self.sickles = sickles
		self.knuts = knuts

	def __str__(self):
		print f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Valut(galleons, sickles, knuts)
print(total)

$ python vault.py
100 Galleons, 50 Sickles, 25 Knuts
25 Galleons, 50 Sickles, 100 Knuts
125 Galleons, 100 Sickles, 125 Knuts
```

```
class Vault:
	def __init__(self, galleons=0, sickles=0, knuts=0):
		self.galleons = galleons
		self.sickles = sickles
		self.knuts = knuts

	def __str__(self):
		print f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

	def __add__(self, other):
		galleons = self.galleons + other.galleons
		sickles = self.sickles + other.sickles
		knuts = self.knuts + other.knuts
		return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + wealey
print(total)

$ python vault.py
100 Galleons, 50 Sickles, 25 Knuts
25 Galleons, 50 Sickles, 100 Knuts
125 Galleons, 100 Sickles, 125 Knuts
```
- Notice how the `__str__` method returns a formatted string. Further, notice how the `__add__` method allows for the addition of the values of two vaults. `self` is what is on the left of the `+` operand. `other` is what is right of the `+`.