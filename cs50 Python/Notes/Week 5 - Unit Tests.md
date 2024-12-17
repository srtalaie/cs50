## Unit Test
- Code used to test code that you wrote
- Unit Testing specifically is testing individual units of your program, typically functions
## Calculator Test
calculator.py
```
def main():
	x - int(input("What's x? "))
	print("x squared is", square(x))

def square(n):
	return n * n

if __name__ == "__main__":
	main()
```

test_calculator.py
```
from caluclator import square

def main():
	test_square()

def test_square():
	if square(2) != 4:
		print("2 squared was not 4")
	if square(3) != 9:
		print("3 squared was not 9")

if __name__ == "__main__":
	main()
```
## Assert
- Keyword in python that allows you to assert something is true, and if it is no errors occur. If it is not true then an error will display
test_calculator.py
```
from caluclator import square

def main():
	test_square()

def test_square():
	assert square(2) == 4
	assert square(3) == 9

if __name__ == "__main__":
	main()
```
## AssertionError
test_calculator.py
```
from caluclator import square

def main():
	test_square()

def test_square():
	try:
		assert square(2) == 4
	except AssertionError:
		print("2 squared was not 4")
	try:
		assert square(3) == 9
	except AssertionError:
		print("3 squared was not 9")
	try:
		assert square(-2) == 4
	except AssertionError:
		print("-2 squared was not 4")
	try:
		assert square(-3) == 9
	except AssertionError:
		print("-3 squared was not 9")
	try:
		assert square(0) == 0
	except AssertionError:
		print("0 squared was not 0")

if __name__ == "__main__":
	main()
```
## pytest
- 3rd party library for unit tests
test_calculator.py
```
from calculator import square

def test_square():
	assert square(2) == 4
	assert square(3) == 9
	assert square(-2) == 4
	assert square(-3) == 9
	assert square(0) == 0

```
- To test using `pytest` you first import the module with `pip install pytest` and then run the below
```
$ pytest test_calculator.py
```
## Categories of Tests
test_calculator.py
```
from calculator import square

def test_positive():
	assert square(2) == 4
	assert square(3) == 9

def test_negative():
	assert square(-2) == 4
	assert square(-3) == 9

def test_zero():
	assert square(0) == 0
```
## Testing for Exceptions
test_calculator.py
```
from calculator import square
import pytest

def test_positive():
	assert square(2) == 4
	assert square(3) == 9

def test_negative():
	assert square(-2) == 4
	assert square(-3) == 9

def test_zero():
	assert square(0) == 0
	
def test_str():
	with pytest.raises(TypeError):
		square("cat")
```
## Side Effects and Testing
hello.py
```
def main():
	name = input("What's your name? ")
	hello(name)
	
def hello(to="world"):
	print("hello,", to)
	
if __name__ == "__main__":
	main()
```
test_hello.py
```
from hello import hello

def test_hello():
	assert hello("David") == "hello, David"
```
- The function cannot be tested this way because it is not retuning a value. It just has a side effect of printing something in the console. Changing the hello function to not have a side effect (best practice) but have it return the actual string and change `main()` to print the return value of `hello()`
```
def main():
	name = input("What's your name? ")
	print(hello(name))
	
def hello(to="world"):
	retunrn f"hello, {to}
	
if __name__ == "__main__":
	main()
```
- Now the below test will work
```
from hello import hello

def test_hello():
	assert hello("David") == "hello, David"
```
- Testing the default
```
from hello import hello

def test_default():
	assert hello() == "hello, world"

def test_argument():
	assert hello("David") == "hello, David"
```
## Collection of Tests
- pytest supports having folder of tests
test/test_hello.py
```
from hello import hello

def test_default():
	assert hello() == "hello, world"

def test_argument():
	assert hello("David") == "hello, David"
```
test/\_\_init__.py
```
```
- Having this `__init__.py` in the folder tells python this folder `test` is a package which is a module or modules that are organized in a folder
- Now running `pytest test` will run all tests within that folder