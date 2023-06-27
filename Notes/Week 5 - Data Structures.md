
## Abstract Data Types
- Can represent anything, how you implement it is up to you

## Stacks & Queues
- **Queues** - FIFO (first in first out) data structure.
	- **Enqueue** - Adding something to the end of a queue
	- **Dequeue** - Opposite, removing something from the front of a queue
- **Stacks** - LIFO (last in first out) data structure.
	- An example would be an email inbox, where the newest message is shown at the top. So you would not have to dig pages later to find it.
	- **Push** - push something on top of the stack
	- **Pop** - remove something on top of the stack
```
const int CAPACITY = 50;

typedef struct
{
	person people[CAPACITY];
	int size;
}
stack;
```

## Resizing Arrays
- Normally difficult to re-size an array because of how it is stored in memory. When adding to an array you append it to the end of the array but in memory there may be other values there already being stored.
- You can however have at the end of an array a pointer to a space in memory where the added value exists.

- Having a fixed array 
```
#include <stdio.h>

int main(void)
{
	int list[3];

	list[0] = 1;
	list[1] = 2;
	list[2] = 3;

	for (int i = 0; i < 3; i++)
	{
		printf("%i\n", list[i]);
	}
}
```

- Using malloc copy old array into new array that is larger. This is inefficient though.
```
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
	int *list = malloc(3 * sizeof(int));
	//Malloc can return NULL if there is no memory
	if (list == NULL)
	{
		return 1;
	}
	
	list[0] = 1;
	list[1] = 2;
	list[2] = 3;

	//Can allocate more memory to a new array
	int *temp = malloc(4 * sizeof(int));
	if (temp == NULL)
	{
		free(list);
		return 1;
	}
	
	//Copy old array into the new array
	for (int i = 0; i < 3; i++)
	{
		temp[i] = list[i];
	}
	
	//Add the new variable
	temp[3] = 4;
	
	//Free list in memory
	free(list);

	//Have list now point to temp which is the new array
	list = temp;
	
	for (int i = 0; i < 3; i++)
	{
		printf("%i\n", list[i]);
	}

	//Freeing the new chunk of memory (which was temp)
	free(list);
	return 0;
}
```

- The easier way using **realloc**. Realloc takes 2 arguments (the old array and the size of the new array). Realloc handles all of the copying over of the old array to the new. Realloc also frees up the old chunk of memory for you as well.
```
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
	int *list = malloc(3 * sizeof(int));
	//Malloc can return NULL if there is no memory
	if (list == NULL)
	{
		return 1;
	}
	
	list[0] = 1;
	list[1] = 2;
	list[2] = 3;

	//Using realloc, gives new address
	int *temp = realloc(list, 4 * sizeof(int));
	if (temp == NULL)
	{
		free(list);
		return 1;
	}
	//List now points to new chunk of memory
	list = temp;

	//New location is given its value
	temp[3] = 4;
	
	for (int i = 0; i < 3; i++)
	{
		printf("%i\n", list[i]);
	}

	//Freeing the new chunk of memory (which was temp)
	free(list);
	return 0;
}
```

## **Operators**:
- **struct** - lets us build a structure in memory
-  **.** - dot operator let's you go into a struct to access its variables
-  **\***-  star operator used to declare pointers, and dereference them
- When you want to use a dot and star together you use '**->**'

## Linked Lists
- **Linked Lists** - allow you to stitch together values in memory
- **Node** - container in code for storing values
	- Because node contains a reference to itself within it's typedef you must include the name after ```struct``` as well as in the reference for the data type of ```*next```
```
typedef sturct node
{
	int number;
	struct node *next;
}
node;
```
- With nodes you can easily add new nodes to the linked list. Downside being you use twice as much memory than you would if you use a traditional array. Also you can not index into it  because the list is not contiguous, thus sacrificing **Binary-Search**
```
typedef sturct node
{
	int number;
	struct node *next;
}
node;

//Initialize an empty linked list of 0
node *list = NULL;

//Returns an address for variable n which is a node
node *n = malloc(sizeof(node));

//Sets the number at n to 1 and next to NULL
n->number = 1;
n->next = NULL;

//List is pointing at the first node
list = n;

//Create a new node that will hold the 2nd value
node *n = malloc(sizeof(node));

//Sets the number at n to 2 and next to list which points to 1
n->number = 2;
n->next = list;

//List now points to 2 which contains the link to 1 in 2's next field
list = n;
```

```
#include <stdio.h>
#include <stdlib.h>

typedef sturct node
{
	int number;
	struct node *next;
}
node;

int maind(int argc, char *argv[])
{
	node *list = NULL;

	//Start at 1 because 1st arg is the program name
	for (int i = 1; i < argc; i++)
	{
		//Convert string to number
		int number = atoi(argv[i]);

		node *n = malloc(sizeof(node));
		if (n == NULL)
		{
			return 1;
		}
		n->number = number;
		n->next = NULL;

		n->next = list;
		list = n;
	}

	//Pointer pointing at the first node of the list
	node *ptr = list;

	while (ptr != NULL)
	{
		printf("%i\n", ptr->number);
		ptr = ptr->next;
	}

	//Reset to beginning of list
	ptr = list;

	//Free up the nodes in memory
	while (ptr != NULL)
	{
		node *ptr = ptr->next;
		free(ptr);
		ptr = next;
	}
}

//Ouput:
$ ./list 1 2 3
3
2
1
```
- Using linked lists searching is O(n) while insertion is O(1) w/prepending nodes
- Using linked lists searching is O(n) while insertion is O(n) w/appending nodes
- Using linked lists with sorted order is O(n) while insertion is O(n)

## Trees
- **Binary Search Trees** - allows you to use binary search on a linked list. Modeled in 2 dimensions (x and y axis).
	- In order for it to work though the nodes to the left must be less than the parent and the nodes to the right must be larger i.e. **Balanced**
```
//Binary Search Tree
typedef struct node
{
	int number;
	struct node *left;
	struct node *right;
}
node;

//Function that traverses tree to find given number
bool search(node *tree, int number)
{
	if (tree == NULL)
	{
		return false;
	}
	else if (number < tree->number)
	{
		return search(tree->left, number);
	}
	else if (number > tree->number)
	{
		return search(tree->right, number);
	}
	else if (number == tree->number)
	{
		return true;
	}
}
```

## Dictionaries
- Combination of key/value pairs
	- **Key** - what you use to look for some info
	- **Value** - the actual info represented by the key
- With key/value pairs search is still O(1), i.e. it is constant. The time to solve the problem is not dependent on the size itself.

## Hashing
- **Hashing** - taking input of some value, and outputting something simpler
- **Hash Function** - the algorithm or code that hashes a problem
- **Hash Table** - application of both arrays and linked lists
```
typedef struct node
{
	char *name;
	char *number;
	struct node *next;
}
node;

//Hash table
node *table[26];
```

## Tries
- short for **Retrieval**
- **Tries** - a tree whose nodes are arrays
```
typedef struct node
{
	char *number;
	struct node *children[26];
}
node;

node *trie;
```