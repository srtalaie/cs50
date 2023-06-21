
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

## Linked Lists
- 