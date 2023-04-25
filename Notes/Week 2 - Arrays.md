
## Compiling
- Convert source code into machine code
```
$ make hello
```
- In this case make isn't the compilier, but utilizes **clang** (c language) under the hood
- In order to compile your code into an executable on your own you would have to
```
$ clang hello.c
```
- The output after using ls in the command line looks like the below. Where ```a.out``` stands for assembler output and is the executable you would run to run the program compiled from the source code
```
$ clang hello.c
$ ls
$ a.out
$ ./a.out
hello, world
```
- Clang supports command line arguments, which are words or key phrases that you type after the command to preform a special output
```
$ clang -o hello hello.c
$ ./hello
hello, world
```
- This allows you to compile the source code into a file you name. But this line is ultimately just running ```make``` in the command line
```
$ clang -o hello hello.c -lcs50
$ ./hello
hello, joe
```
- The last argument ```-lcs50``` lets the compilier know that it needs to include a separate  library on the hard drive
- **4 Steps of Compiling** (whole process is just called Compiling)
	- **Preprocessing**
		- In C anything with a '#' is marked for preprocessing. For example ```#include <cs50.h>``` lets the compilier know to find and add the contents of the file into the source code so it can use the functions from the included code.
	- **Compiling**
		- Compilier converts source code into **assembly code**, which is closer to what computers understand.
	- **Assembling**
		- Takes the **assembly language** and converts it into **machine code**
	- **Linking**
		- Links the machine code from the source code with the machine code from the included code from preprocessing
- **Decompiling** - reversing the process, converting it from machine code back to the source code. Logic is retained, but function names and variable names are not retained. Also machine code does not care about whether a for or while loop was used as long as the logic is the same. Makes **reverse engineering** difficult and time consuming

## Debugging
- Can use ```printf()``` print your variables to console to check and see if it is correct
- **Debugger** - software written to help debug code
	- **Breakpoint** - place to stop running code. When program runs in the debugger you can step through the code line by line. This line of code is where the code will pause and await debugging commands
	- Debugger keeps track of variables that exist in the function
	- Control buttons in the debugger
		- **Continue** - will run your program all the way through to completion and terminate the debugger instance
		- **Step Over** - debugger will run the highlighted code, but not step by step
		- **Step Into** - will run highlighted code but step by step, including showing functions that may be included but not in the source code (will only show this if they are on the computer's hard drive as well)

## Arrays
- 