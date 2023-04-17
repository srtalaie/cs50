
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
- 