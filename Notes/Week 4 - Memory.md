
## Memory
- **Bit Map** -  type of image pattern of 0's and 1's

## Hexadecimal
- Combination of 6 numbers and letters that represent some RGB code
- When you need more than 10 digits, you start to use english alpha 
  (i.e. 0 1 2 3 4 5 6 7 8 9 A B C D E F). This is **Hexadecimal** or **base-16**.
- Each pair of hexadecimal digits can count as high as 255 which is the highest value you can have for a RGB value.
- ex/ 11111111 = FF from binary to hexadecimal
- ex/ 0000FF = 0 Red, 0 Green, 255 Blue

## Addresses
- Computers use hexadecimal for addresses in memory, to make clear that the number is in hexadecimal we prefix the address with "0x"
- In C you can use
	- **&** - tells you the address in memory
	- **\*** - tells the computer where to go into memory
```
int n = 50;
printf("%p\n", &n);

Output:
0x7ffcc784a04c
```

## Pointers
- A variable that contains the address of some value. An address of something in the computer's memory.
```
int n = 50;
int *p = &n;
```
- Above sets the address of n to the variable p. The star in front of p lets the system know that p is a pointer.
```
#include <stdio.h>

int main(void)
{
	int n = 50;
	
	//When declaring a pointer you have to include the '*'
	int *p = &n;
	
	//When you want to go to an address (dereference a pointer) you   include the '*'
	printf("%i\n", *p);
}

//Ouput
50
```

## Strings
- A string in a computer's memory looks like: | H | I | ! | \\0 | with each in it's own byte.
```
string s = "HI!";
s[0] = 'H';
```
- The computer will store each character in memory in sequence. i.e. 'H' = 0x123, 'I' = 0x124, '!' = 0x125, '\\0' = 0x126.
- For the actual variable of s it is just a **pointer** to the first character in memory, therefore s is 0x123. It only stores the first address because strings are nul terminated ('\\0') so it knows that the whole string is from s to the place in memory untill the nul character.
- **String** is a synonym for a pointer to a characetr
	```char *s = "HI!"; ``` is the same as ```string s = "HI!";```
- This can be done like the following:
```
typedef int integer;

```
- Above we create a synonym for **integer** as **int**
- For **strings** it looks like:
```
typedef char *string;
```
- The **cs50** library has the above definition included in it, which is why the keyword **string** has worked when defining a variable of type **string**
- **Strings** are the addresses of the first character in memory
```
#include <stdio.h>

int main(void)
{
	/*
	How you declare a string without cs50 library
	*/
	char *s = "HI!";
	printf("%p\n", s);
}

//Ouput
0x9024a7f49f83
```
- Changing ```%p``` to ```%s``` in ```printf()``` will instead print out the string: ```HI!```. The function ```printf()``` knows to go to the address without having to include ```*s*```
```
#include <stdio.h>

int main(void)
{
	/*
	How you declare a string without cs50 library
	*/
	char *s = "HI!";
	printf("%p\n", s);
	printf("%p\n", &s[0]);
	printf("%p\n", &s[1]);
	printf("%p\n", &s[2]);
	printf("%p\n", &s[3]);
}

//Ouput
0x9024a7f49f83
0x9024a7f49f83
0x9024a7f49f84
0x9024a7f49f85
0x9024a7f49f86
```

## Pointer Arithmetic
```
#include <stdio.h>

int main(void)
{
	char *s = "HI!";
	printf("%c\n", s[0]);
	printf("%c\n", s[1]);
	printf("%c\n", s[2]);
}

//Ouput
H
I
!
```

```
#include <stdio.h>

int main(void)
{
	char *s = "HI!";
	printf("%c\n", *s);
	printf("%c\n", (*s+1));
	printf("%c\n", (*s+2));
}

//Ouput
H
I
!
```
- Because addresses are in sequential order you can go to the following addresses by adding 1, 2... and so on for the length of the string

```
#include <stdio.h>

int main(void)
{
	char *s = "HI!";
	printf("%s\n", s);
	printf("%s\n", s+1);
	printf("%s\n", s+2);
}

//Ouput
HI!
I!
!
```
- Above is how to print substrings of strings

## Comparing Strings
```
#include <cs50.h>
#include <stdio.h>

int main(void)
{
	string s = get_string("s: ");
	string t = get_string("s: ");

	if (s == t)
	{
		printf("Same\n");
	}
	else
	{
		printf("Different\n");
	}
}

//Output
s: HI!
t: HI!
Different

```
- When using ```==``` you are comparing their places in memory, although the strings are the same they are not in the same places in memory
```
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
	string s = get_string("s: ");
	string t = get_string("s: ");

	if (strcmp(s, t) == 0)
	{
		printf("Same\n");
	}
	else
	{
		printf("Different\n");
	}
}

//Output
s: HI!
t: HI!
Same
```
- ```strcmp()``` goes to both locations in memory and moves left to right comparing each character until the nul terminator

## Copying
```
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
	string s = get_string("s: ");

	string t = s;

	t[0] = toupper(t[0]);

	printf("%s\n", s);
	printf("%s\n", t);
}

//Input
s: hi!
//Output
s: Hi!
t: Hi!
```
- Above copies the memory address, therefore it copies the address into the new address. Because they are the same address you end up captiallizing both s and t because they point to the same values in memory
```
malloc
free
```
- **Malloc** (memory allocation) is a function that you can use to ask the OS for some number of bytes. It returns the address of the the first byte of memory. Because it is not nul terminated you have to remember how many bytes you requested.
- **Free** lets you pass an address back to the OS to free up the memory. Can be a cause of hanging or bugs if you forget to free up memory
```
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	char *s = get_string("s: ");

	/*
		Ask the computer for a new address in memory of the
		same amount of space as the user's input. 
		+1 is for the nul terminator
	*/
	char *t = malloc(strlen(s) + 1);

	//You go just beyond the boundary for the nul char
	for (int i = 0; i < strlen(s) + 1; i++)
	{
		t[i] = s[i];
	}

	/*
		Safeguard to make sure t contains at least 1 char
		to uppercase
	*/
	if (strlen(t) > 0)
	{
		t[0] = toupper(t[0]);
	}

	printf("%s\n", s);
	printf("%s\n", t);
}

//Input
s: hi!
//Output
s: hi!
t: Hi!
```
- Calling **malloc** gives a chunk of memory that is of the length of s for t. t is now pointing to that empty space in memory
- For loop therefore goes through the empty space in memory and  copies over the values of s to t
- Optimization why you should not call a function in the condition of the for loop because you are calling the function each iteration. Therefore:
```
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	char *s = get_string("s: ");

	/*
		Ask the computer for a new address in memory of the
		same amount of space as the user's input. 
		+1 is for the nul terminator
	*/
	char *t = malloc(strlen(s) + 1);

	//You go just beyond the boundary for the nul char
	for (int i = 0, n = strlen(s) + 1; i < n; i++)
	{
		t[i] = s[i];
	}

	/*
		Safeguard to make sure t contains at least 1 char
		to uppercase
	*/
	if (strlen(t) > 0)
	{
		t[0] = toupper(t[0]);
	}

	printf("%s\n", s);
	printf("%s\n", t);
}

//Input
s: hi!
//Output
s: hi!
t: Hi!
```
- In the condition you can intialize 2 variables at the beginning, the start and the upper limit of the condition
```
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	char *s = get_string("s: ");

	/*
		Ask the computer for a new address in memory of the
		same amount of space as the user's input. 
		+1 is for the nul terminator
	*/
	char *t = malloc(strlen(s) + 1);

	strcpy(t, s);

	/*
		Safeguard to make sure t contains at least 1 char
		to uppercase
	*/
	if (strlen(t) > 0)
	{
		t[0] = toupper(t[0]);
	}

	printf("%s\n", s);
	printf("%s\n", t);
}

//Input
s: hi!
//Output
s: hi!
t: Hi!
```
- Using ```strcpy()``` you can skip the whole for loop
- ```get_string()``` and ```malloc()``` both CAN return **null** which will cause the program to crash so you need to include safeguards for those as well
```
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	char *s = get_string("s: ");
	if (s == NULL)
	{
		return 1;
	}

	/*
		Ask the computer for a new address in memory of the
		same amount of space as the user's input. 
		+1 is for the nul terminator
	*/
	char *t = malloc(strlen(s) + 1);
	if (t == NULL)
	{
		return 1;
	}

	strcpy(t, s);

	/*
		Safeguard to make sure t contains at least 1 char
		to uppercase
	*/
	if (strlen(t) > 0)
	{
		t[0] = toupper(t[0]);
	}

	printf("%s\n", s);
	printf("%s\n", t);
	
	return 0;
}

//Input
s: hi!
//Output
s: hi!
t: Hi!
```
- When using **malloc** you also need to use **free** to free up the memory you asked for. So at the end of the program you call **free** and pass it **t**
```
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	char *s = get_string("s: ");
	if (s == NULL)
	{
		return 1;
	}

	/*
		Ask the computer for a new address in memory of the
		same amount of space as the user's input. 
		+1 is for the nul terminator
	*/
	char *t = malloc(strlen(s) + 1);
	if (t == NULL)
	{
		return 1;
	}

	strcpy(t, s);

	/*
		Safeguard to make sure t contains at least 1 char
		to uppercase
	*/
	if (strlen(t) > 0)
	{
		t[0] = toupper(t[0]);
	}

	printf("%s\n", s);
	printf("%s\n", t);

	free(t);

	return 0;
}

//Input
s: hi!
//Output
s: hi!
t: Hi!
```

## Valgrind
- 