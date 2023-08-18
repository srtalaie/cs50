## Source Code
- Code that the program wrote
- Computers don't understand source code, only binary which is called **Machine Code** 

## Compiling
- source code :luc_arrow_right: **compiler** :luc_arrow_right: machine code
- Converting source code written in a human legible language (source code) into machine code that the computer can read

## Correctness, Design, Style
- How to evaluate the quality of the code
- Correctness - does it do what you need it to do
- Design - subjective, better the design often the faster it is ran or the more maintainable it is
- Style - aesthetics of the code, computer may not care but the human does and it makes it more easily legible

## Libraries & Documentation
- Library - 3rd party code that gives you access to functions, etc.
- Header Files - area where you **include** 3rd party functions you want to have in your code
- Documentation (Docs) - insturctions/manuals that help you understand what is included in 3rd party libraries ex/ [manual](http://manual.cs50.io/#stdio.h). Auhtoritative source of what you can do / how you can do something with the library
- cs50.h - library to help with input/output [docs](http://manual.cs50.io/#cs50.h) 

## Format Code
- ex/ ```printf("hello, %s\n", answer)``` where ```%s``` serves as a placeholder for the value of answer

## Types
- Data types (primatives)
	- string (text)
	- bool (true or false)
	- char (single character)
	- double (big decimal)
	- float (decimal)
	- int (number)
	- long (big number)
- You need to declare your types before the variable you are assigning a value to

## Conditionals
```
if (x < y) 
{
	printf("x is less than y");
}
```
-  within the parentheses is the conditional statement that is being evaluated, if true then the code within the curly braces is ran
```
if (x < y)
{
	printf("x is less than y");
}
else 
{
	printf("x is greater than y");
}
```
- Same as above, but if the conditional statement evaluates to false than the code within the curly braces after else is ran
```
if (x < y)
{
	printf("x is less than y");
} 
else if (x > y)
{
	printf("x is greater than y");
}
else if (x == y)
{
	printf("x is equal to y");
}
```
- when evaluating equality you use two equal signs (\=\=)
- a better version of the code would be just to use an else block instead of the last else if because the quality is implied if less than or greater than are false.
```
if (x < y)
{
	printf("x is less than y");
} 
else if (x > y)
{
	printf("x is greater than y");
}
else
{
	printf("x is equal to y");
}
```

## Loops & Variables
```
int counter = 0;
//Each is a way to increment by 1
counter = counter + 1;
counter += 1;
counter++;

//Each is a way to decrement by 1
counter = counter - 1;
counter -= 1;
counter--;
```
- Initialize variable with type, when you update the variable you do not need to include the type
```
int counter = 3;
while (counter > 0)
{
	printf("meow\n");
	counter = counter - 1;
}
```
- While loop, loops while condition is still met
- Loop will print meow to console 3 times. Each iteration of loop it will check counter to see if the condition is met (counter being greater than 0 still), if condition is met then "meow" will be printed to the console.
```
for (int i = 0; i < 3; i++)
{
	printf("meow\n");
}
```
- For loop does the same as above but it consolidates most of the logic to the beginning of the loop

## Command Line commands
- cd - change directory, used to change the current directory, needs to be paired with the path
- ls - list, lists all of the files/directories in the current directory
- mv - move, move contents of a file into a new file  ```
mv [current location] [location you wish to ove it to]
- cp - copy a file
- mkdir - make a directory
- rm - remove a file
- rmdir - remove a directory

## Do While Loops
```
	int n;
	do
	{
		n = get_int("Size: ");
	}
	while (n < 1);
```
- Loop will run until the while conditional is met

## Nested Loops
```
#include <cs50.h>
#include <stdio.h>

int main(void) 
{
	int n;
	do
	{
		n = get_int("Size: ");
	}
	while (n < 1);
	
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			printf('#');
		}
		
		printf("\n");
	}
}



/* Output if user assigns 3 to n:
	###
	###
	###
*/
```
- Before the outer loop iterates once, the inner loop will iterate once

## Comments
- Notes you write that explain what your code is doing

## Abstraction
- Comments can be a good way to start a program, gives you a high level solution
```
#include <stdio.h>

int get_size(void);
void print_grid(int size);

int main(void)
{
	//Get size of grid
	int n = get_size();
	
	//Print grid of bricks
	print_grid(n);
}

int get_size(void)
{
	int n;
	do
	{
		n = get_int("Size: ");
	}
	while (n < 1);
	return n;
}

void print_grid(int size)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			printf('#');
		}
		printf("\n");
	}
}
```
- When wiriting functions you right the output format first, in the get_size function case it is an int and in the parentheses any input, if none you write void. Return is the keyword that is used that will return whatever is after the keyword as the output for the function.
- When writing void as the type of the output you are declaring that the function will do something, but not return any value
- Including the function names outside of main but before it lets compilier know that the functions will be declared in the file but after main
- Abstraction is the process of only showing the necessary details to the user and hiding the other details in the background
	- In this case it is declaring the functions at the bottom

## Integer Overflow
- Computer only has a finite amount of memory (RAM)
- Limitation on how high you can count because of this
- Smallest amount the computer can represent is 32 0's which equals 0
- Biggest would be 32 1's which equals 4294967295
- But because you need negative numbers than an int can only represent -2147483648 to 2147483647
- A situation when you run out of bits is **integer overflow**
- Solution is to use long which allocates more memory to represent the number

## Truncation
- When working with numbers with decimals you may truncate the value, meaning you lose everything after the decimal
- Solution is to use floating point values or **floats**

## Type Casting
- Converting one data type to another by explicitly telling the compilier you want to do so
```
long x = get_long("x: ");
long y = get_long("y: ");

float z = (float) x / (float) y;
printf("%f\n", z)
```

## Floating-point Impercesion
- Using a finite amount of memory, you will not be able to represent how percise numbers can be because there is a boundary
- When dealing with a decimal that repeats the computer just gives the closets approximation it can
- **Double** will use twice as many bits as a float but still suffers from the impercesion