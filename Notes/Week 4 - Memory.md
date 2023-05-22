
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

## Strings
- 