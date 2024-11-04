## Linear Search
- Search starting from left to right until search term is found
```
For i from 0 to n-1
	If 50 is behind the doors[i]
	return true
return false
```

## Binary Search
- Array is sorted in advance, and first the very middle is checked. Based on if the value is larger or smaller the search moves to the left or right and the moves to a linear search moving left to right but with only half of the array.
```
If no doors left
	return false
If 50 is behind doors[middle]
	return true
Else if 50 < doors[middle]
	search doors[0] through doors[middle - 1]
Else if 50 > doors[middle]
	search doors[middle + 1] through doors[n - 1]
```

## Running Time
- How long it takes for an algorithm to complete its task
- **Big O Notation** used to denote how many steps algorithm takes, order/magnitude of it. Used to describe the upper bound, the longest the algorithm will take.
	- O =  Order, O(n) = Order of n
	- Common Big O formulas (slowest to fastests)
		- O(n<sup>2</sup>)
		- O(n log n)
		- O(n) - linear search
		- O(log n) - binary search
		- O(1) - amount of steps do not change, fixed amount of steps
	- Ω is the symbol used for the lower bound of an algorithm, how few steps an algorithm can take
		- Best case for linear search/binary search is Ω(1), you may get lucky and the  term you are looking for is the first thing you check
	- If an algorithm has the same upper/lower bound it is denoted with Θ

## search.c
- Linear Search w/ strings & ints
```
#include <cs50.h>
#include <stdio.h>

int main(void)
{
	int numbers[] = {20, 500, 10, 5, 100, 1, 50};

	int n = get_int("Number: ");
	for(int i = 0; i < 7; i++)
	{
		if (numbers[i] == n)
		{
			printf("Found \n");
			return 0;
		}
	}
	printf("Not Found \n");
	return 1;
}
```

```
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
	string strings[] = {"battleship", "boot", "cannon", "iron", "thimble", "top hat"};

	string s = get_string("String: ");
	for(int i = 0; i < 6; i++)
	{
		if (strcmp(strings[i], s) == 0)
		{
			printf("Found \n");
			return 0;
		}
	}
	printf("Not Found \n");
	return 1;
}
```

```
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
	string names[] = {"Carter", "David"};
	string numbers[] = {"+1-617-495-1000", "+1-949-468-2750"};

	string name = get_string("Name: ");
	
	for(int i = 0; i < 2; i++)
	{
		if (strcmp(names[i], name) == 0)
		{
			printf("Found %s\n", numbers[i]);
			return 0;
		}
	}
	printf("Not Found \n");
	return 1;
}
```


## Data Structures
- Create your own datatypes out of the primatives that come with C
ex/
```
typedef struct
{
	string name;
	string number;
}
person;
```

```
#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
	string name;
	string number;
}
person;

int main(void)
{
	person people[2];

	people[0].name = "Carter";
	people[0].number = "+1-617-495-1000";
	
	people[1].name = "David";
	people[1].number = "+1-949-468-2750";
	
	string name = get_string("Name: ");
	
	for(int i = 0; i < 2; i++)
	{
		if (strcmp(people[i].name, name) == 0)
		{
			printf("Found %s\n", people.number[i]);
			return 0;
		}
	}
	printf("Not Found \n");
	return 1;
}
```

## Sorting
- **Selection Sort** selecting the smallest element again and again until they are all in place. Start with the smallest and then swap the first element with where the smallest used to be until array is sorted.
```
for i from 0 to n - 1
	Find the smallest number between numbers[i] to numbers[n - 1]
	Swap smallest number with numbers[i]
```
- **Bubble Sort** take two elements and compare and sort based on just those two elements moving left to right and iterating back over the loop until the smallest element is on the left and largest on the right. Named because the largest elements bubble to the top of the array. Know when it is sorted when you move through the whole array without swapping.
```
Repeat n - 1 times
	For i from 0 to n - 2
		If numbers[i] and numbers[n + 1] out of order
			Swap them
	If no swaps
		Quit
```
- When analyzing algorithms generally you look at how many comparisons the algorithm went through
	- For selection sort it takes **n - 1** comparisons for the smallest number, then **n - 2** comparisons for the next smallest, then so on
		- **n<sup>2</sup>/2 - n/2** or just **O(n<sup>2</sup>)** because n<sup>2</sup> is what only matters as n gets larger. This is the upper bound for selection sort, for the lower bound it is  **Ω(n<sup>2</sup>)** because you still go through each compariosn. Slection sort takes **Θ(n<sup>2</sup>)** (upper/lower bounds take the same amount of steps)
	- For bubble sort it takes **n - 1** comparisons because through each pass you were still solving at least 1 problem
		- **(n -1) (n - 1)** - you are doing **n - 1** things, **n - 1** times. Or **n<sup>2</sup> - 2n + 1** or just **O(n<sup>2</sup>)** because n<sup>2</sup> is what only matters as n gets larger. The upper bound for bubble sort is **O(n<sup>2</sup>)** but the lower bound is **Ω(n)** because if the array is already sorted it passes through only the one time because if there are no swaps it quits.
- [Comparing Sorting Algorithms Visualizer](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)

## Recursion
- Ability of a function to call itself
```
#include <cs50.h>
#include <stdio.h>

void draw(int n);

int main(void)
{
	int height = get_int("Height: ");
	draw(height);
}

void draw(int n)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < i + 1; j++)
		{
			printf("#");
		}
		printf("\n");
	}
}
```
- Implemented with recursion:
```
#include <cs50.h>
#include <stdio.h>

void draw(int n);

int main(void)
{
	int height = get_int("Height: ");
	draw(height);
}

void draw(int n)
{
	if (n <= 0)
	{
		return;
	}
	
	draw(n - 1);

	for (int i = 0; i < n; i++)
	{
		printf("#");
	}
	printf("\n");
}
```

## Merge Sort
- Sorting using recursion 
```
If only on number
	Quit
Else
	Sort left half of numbers
	Sort right half of numbers
	Merge sorted halves
```
- **O(n log n)** upper bound, lower boudn **Ω(n log n)**. Therefore **Θ(n log n)**.
- If you want to save time you must sacrifice space, in the case of merge sort because you need another array to hold the other half