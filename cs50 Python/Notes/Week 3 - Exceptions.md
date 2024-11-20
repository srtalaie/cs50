## SyntaxError
- A problem with the code that you typed
- Entirely on you to solve, a problem that you have to go back and fix
- `literal` - something that was typed in
## ValueError
- `Runtime error` that occurs when your code is running. Will require you to  implement safeguards to protect yourself from it.
- ValueError occurs when you try to cast an unsupported value such as casting the string 'cat' to an int `int('cat')`
## Try-Expect
- Error handling keywords `try` and `except` will check if an exception occurs
```
try:
	x = int(input("What is x? "))
except ValueError:
	print("x is not an integer")
	
print(f"x is {x}")
```
## NameError
- Occurs when you are doing something with a variable that you shouldn't such as  a variable not being defined
## else
```
try:
	x = int(input("What is x? "))
except ValueError:
	print("x is not an integer")
else:
	print(f"x is {x}")
```
- `else` block will run if nothing goes wrong
## Reprompting, break
- Allow you to continue the program instead of terminating when the user commits an error
```
while True:
	try:
		x = int(input("What is x? "))
	except ValueError:
		print("x is not an integer")
	else:
		break
		
print(f"x is {x}")
```
## get_int
```
def get_int():
	while True:
		try:
			x = int(input("What is x? "))
		except ValueError:
			print("x is not an integer")
		else:
			return x
```
- `return` will break the loop and return the value of x

```
def main():
	x = get_int()
	print(f"x is {x}")

main()
```
- Can refine `get_int()` further by:
```
def get_int():
	while True:
		try:
			x = int(input("What is x? "))
			return x
		except ValueError:
			print("x is not an integer")
			
```
## pass
- If you want to handle an exception but you want to `pass` or ignore it
```
def get_int():
	while True:
		try:
			x = int(input("What is x? "))
			return x
		except ValueError:
			pass
```
- You are still catching the error, but you are not providing any explanation further
## Function Arguments
```
def get_int(prompt):
	while True:
		try:
			x = int(input(prompt))
			return x
		except ValueError:
			pass
```
- `get_int()` now takes a parameter which will be a prompt which is a string. Which now allows the `main()` function assign it's own variable and have the prompt reflect whatever name it chooses for the variable
```
def main():
	x = get_int("What's x?")
	print(f"x is {x}")

main()
```