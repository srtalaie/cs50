## Libraries
- Files of code that other people or ourself that you can use in your programs
- Python like does this through **modules**
## Modules
- A library with one or more functions and other features built into it
- The purpose is to encourage reusability of code
- Example Library that python comes with:
	- random.py
## import
- Mechanism for you to load a module into your program so you can use those functions

using random.py library to simulate a coin flip
```
import random

coin = random.choice(["heads", "tails"])
print(coin)
```
## from
- Keyword used to load in a specific function **from** a module , instead of importing everything from the module
```
from random import choice

coin = choice(["heads", "tails"])
print(coin)
```
## randint
- **random.randint(a, b)** - Function in the random library that returns a random number between **a** and **b**  inclusive (ex/ a = 1, b = 10 you would get a random number between 1 and 10 including the 1 and 10)
```
import random

number = random.randint(1, 10)
print(number)
```
## shuffle
- **shuffle(x)** - Function in the random library that takes a list of values and shuffles the list. This function does not return a new list but just shuffles the list in the argument
```
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
	print(card)
```
## statistics
- Library used to preform analysis on data sets
- **mean** - function used to find average
```
import statistics

print(staistics.mean([100, 90]))
```
## Command-line Arguments
- Allow you to provide input when you are executing at the command line
- You can use **sys** library to access the command line arguments via **sys.argv**
	- **sys.argv** is a list of what the user typed in the command line
```
import sys

print("hello, my name is", sys.argv[1])

$ python hello.py David
hello, my name is David
```
- In the above sys.argv is a list of ```["hello.py", "David"]```
- To avoid the index out of range exception if a user does not enter their name after running the program
```
import sys

try:
	print("hello, my name is", sys.argv[1])
except IndexError:
	print("Too few arguments")
```

```
import sys

if len(sys.argv) < 2:
	print("Too few arguments")
elif len(sys.argv) > 2:
	print("Too many arguments")
else:
	print("hello, my name is", sys.argv[1])
```
## sys.exit
- Allows you to exit the program and print out the provided string
- Using **sys.exit** you can structure your code as below and avoid the bottom line printing an error even after the checks
```
import sys

# Check for errors
if len(sys.argv) < 2:
	sys.exit("Too few arguments") 
elif len(sys.argv) > 2:
	sys.exit("Too many arguments")

# Print name tags
print("hello, my name is", sys.argv[1])
```
## Slices
- Allows you to take a subset of a list
```
import sys

if len(sys.argv) < 2:
	sys.exit("Too few arguments") 

for arg in sys.argv[1:]:
	print("hello, my name is", arg)
```
- Above it sets the list that you are looping over to begin at the 1 index rather than 0 so as to avoid the system printing out the first arg which is the program's name
## Packages
- 3rd party libraries that you can install on your machine
- **PyPI** (Python Package Index) - [PyPI](pypi.org) is a site where you can search for and download packages
- **pip** - package manager that comes with python that allows you to install packages onto your machine
say.py
```
import cowsay
import sys

if len(sys.argv) == 2:
	cowsay.cow("hello, " + sys.argv[1])
```
## APIs
- **API** (Application Programing Interface) - 3rd party services that you can write code to talk to
- You can access APIs using the **requests** package
- Usually the data that you access via an API will return its data in **JavaScript Object Notation** (JSON) format which is a standard text format for data
itunes.py
```
import requests
import sys

if len(sys.argv) != 2:
	sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(response.json())
```
using python's json library you can print out your JSON in a readable format using **json.dumps()**
```
import json
import requests
import sys

if len(sys.argv) != 2:
	sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(json.dumps(response.json()), indent=2)
```
print out the songs which in the data is under "results" and has the key "trackName"
```
import json
import requests
import sys

if len(sys.argv) != 2:
	sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

obj = response.json()

for result in obj["results"]:
	print(result["trackName"])
```
## Custom Libraries
- Bundle up code that you continue to use in your programs
sayings.py
```
def main():
	hello("world")
	goodbye("world")

def hello(name):
	print(f"Hello, {name}")

def goodbye(name):
	print(f"Goodbye, {name}")

main()
```
say.py
```
import sys

from sayings import hello

if len(sys.argv) == 2:
	hello(sys.argv[1])

$ python say.py David
hello, world
goodbye, world
Hello, David
```
- You need to call ```main``` such as:
sayings.py
```
def main():
	hello("world")
	goodbye("world")

def hello(name):
	print(f"Hello, {name}")

def goodbye(name):
	print(f"Goodbye, {name}")

if __name__ == "__main__":
	main()
```
- ```__name__``` is a special symbol in Python whose value is automatically set to ``main`` when you run a program from a command line. Now with that line, if you import ``hello`` then it will only output ``Hello, David``