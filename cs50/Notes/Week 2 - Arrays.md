
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
- Way of storing data, back to back in the computer's memory so you can access each individual member easily
```
//Create an area of size 3
int scores[3];

/*  Assigns the following values to the scores array
	72 to the 1st one (index of 0)
	73 to the 2nd one (index of 1)
	33 to the 3rd one (index of 2)
*/
socres[0] = 72;
socres[1] = 73;
socres[2] = 33;
```
- When stored in memory, the elements of the array are contiguous
```
#include <cs50.h>
#include <stdio.h>

const int N = get_int("How many scores? ");

float average(int array[]);

int main(void)
{
	int scores[N];
	for (int i = 0; i < N; i++)
	{
		scores[i] = get_int("Score%i: ", i += 1);
	}
	printf("Average: %f\n", average(N, scores));
}

float average(int length, int array[])
{		
	int sum = 0;
	for (int i = 0; i < length; i++)
	{
		sum += array[i];
	}
	return sum / (float) length;
}
```
- Above is a way to dynamically code a way to get a student's score using arrays. When first initializing an array you leave the square brackets empty ex/ ```int array[]```
- In C you must remember the length of the array yourself, such that you cannot "ask" the array its length

## String
- Strings in memory do not have a defined length, such that they take up as much memory as its lenght
- A string is just an array of characters 
```
string s = "HI!;

//Broken down the array would be the following
s[0] = `H`;
s[1] = 'I';
s[2] = '!'; 
s[3] = \0;
```
- Every string has 1 byte added to the end of it to show the string is done, so in memory a string's length is the amount of chars + 1 byte. "\\0" is '0' written out as a char also known as a null character
```
#include <stdio.h>

int main(void)
{
	char c1 = 'H';
	char c2 = 'I';
	char c3 = "!";
	printf("%c%c%c\n", c1, c2, c3);
}

Ouput:
HI!

//This would be the same as above

#include <cs50.h>
#include <stdio.h>

int main(void)
{
	string s = "HI!";
	printf("%c%c%c\n", s[0], s[1], s[2]);
}

Ouput:
HI!
```

```
#include <cs50.h>
#include <stdio.h>

int main(void)
{
	string s = "HI!";
	string t = "BYE!";
	
	printf("%s\n", s);
	printf("%s\n", t);
}

Output:
HI!
BYE!
```

```
#include <cs50.h>
#include <stdio.h>

int main(void)
{
	string words[2];
	
	words[0] = "HI!";
	words[1] = "BYE!";
	
	printf("%c%c%c\n", words[0][0], words[0][1], words[0][2]);
	printf("%c%c%c\n", words[1][0], words[1][1], words[1][2]);
}

Output:
HI!
BYE!
```
- When you have an array of arrays the first index in the bracket represents the array and the second index in the bracket represents the element at that index within the array denoted in the first index
```
#include <cs50.h>
#include <stdio.h>

int main(void)
{
	string name = get_string("What is your name? ");

	int n = 0;
	while (name[n] != '\0')
	{
		n++;
	}
	printf("%i", n);
}
```
- Above is an example of how you would find the length of a string. In the while loop you check for the null char that is at the end of every string, so the loop will iterate n until it reaches the null char
- In C there is a whole library for strings, called **string.h**. Below is an easier way to implement the previous code
```
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
	string name = get_string("What is your name? ");
	int n = strlen(name)
	printf("%i", n);
}
```
- **ctype.h** lets you check data types and functions that are useful
- Below is code that will iterate over a user provided string and change all the characters to upper case
```
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
	string s = get_string("Before: ");
	printf("After: ");
	for (int i = 0; i < strlen(s); i++)
	{
		if (s[i] >= 'a' && s[i] <= 'z')
		{
			printf("%c", s[i] - 32);
		}
		else
		{
			printf("%c", s[i]);
		}
	}
	printf("\n");
}
```
- Because in the ASCII chart the chars have numbers that correspond to the letters. For the lower case letters the corresponding upper case letter is always -32 away. For example "a" = 97 & "A" = 65
- An easier implementation of the above code with **ctype.h**
```
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
	string s = get_string("Before: ");
	printf("After: ");
	for (int i = 0; i < strlen(s); i++)
	{
		if (islower(s[i]))
		{
			printf("%c", toupper(s[i]));
		}
		else
		{
			printf("%c", s[i]);
		}
	}
	printf("\n");
}
```
- The two functions **islower** and **toupper** do the math in the previous example for you
- **toupper** ignores already upper case letters so an even better implementation would be
```
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
	string s = get_string("Before: ");
	printf("After: ");
	for (int i = 0; i < strlen(s); i++)
	{
		printf("%c", toupper(s[i]));
	}
	printf("\n");
}
```
- You do not need to ask the length of the string each time in the loop so a better way to do it would be:
```
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
	string s = get_string("Before: ");
	printf("After: ");
	for (int i = 0, n = strlen(s); i < n; i++)
	{
		printf("%c", toupper(s[i]));
	}
	printf("\n");
}
```
- Where i is changing and n is constant, this way the loop does not constantly have to check the length of s at each iteration

## Command Line Arguments
- Can be accessed in programs, let you express your whole thought at once
- By removing "void" in the main function you are telling the compilier that the function will take in arguments
- ```argc``` is argument count while ```argv``` is all the words that you are going type in the command line as arguments 
```
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
	printf("hello, %s\n", argv[1]);
}

$ ./greet David
hello, David
```
- argv\[0] is ./greet while argv\[1] is what the user enters as their name
```
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
	if (argc == 2)
	{
		printf("hello, %s\n", argv[1]);
	}
	else
	{
		printf("hello, world \n");
	}
}

$ ./greet David
hello, David
```
- Now the program checks to see if the user has included any argument s besides the first one that runs the program. If so then it will run the first line in the if statement, if not then it wil run the else block
- In C the two main way to write main functions is ```int main(void)``` or ```int main(argc, string argv[])```
- **cowsay** is a program already installed that a user can use in the command line to have an ascii art cow say what the user enters in the command line
```
$ cowsay hello, world
```
or if you want to change the cow to a duck
```
$ cowsay -f duck hello, world
```

## Exit Status
- Whenever the main function exits, it returns an integer that you can use to figure out the reason i.e. error codes
- The int in ```int main(void)``` indicates that main will return an integer, or its exit status as a code. Most of the time it is 0 meaning it exited properly
```
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
	if (argc != 2)
	{
		printf("Missing command-line argument\n");
		return 1;
	}
	else
	{
		printf("hello, %s\n", argv[1]);
		return 0;
	}
}

$ ./greet
Missing command-line argument
$ echo $?
1
$ ./greet David
$ echo $?
0
hello, David
```
- By typing ```echo $?``` you can see what exit status yoru program has eneded with.

## Cryptography
- Art of encrypting info
- Encryption is the act of changing plaintext into cyphertext
- plaintext + key :luc_arrow_right: cipher :luc_arrow_right: ciphertext
- Decryption is the reverse of the encryption process