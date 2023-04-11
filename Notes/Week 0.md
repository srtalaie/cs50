
## Binary
- Unary - system using a single symbol to solve a problem
	- base -1 - 1, 2, 3, 4, 5...
- Decimal - 10, 0-9. What humans use
	-  base -10 - ex/ 123 = (100 x **1**) + (10 x **2**) + (1 x **3**) = 123
		- 10 is the base. The 1 in the hundreds column is 10<sup>2</sup> (10<sup>2</sup> = 100. The 2 in the tens column is 10<sup>1</sup>(10<sup>1</sup> = 10). The 3 in the hundreds column is 10<sup>0</sup> (10<sup>0</sup> = 1).
- Binary - what compuetrs use, 2 digits (0 or 1)
	- base -2 - 0 or 1
		- 2 is the base. For a 3 digit number ### = 2<sup>2</sup> 2<sup>1</sup> 2<sup>0</sup> = 4 2 1
			- 000 or 0 is this because (4 x 0) + (2 x 0) + (1 x 0) = 0
			- 001 or 1 is this because (4 x 0) + (2 x 0) + (1 x 1) = 1
			- 010 or 2 is this because (4 x 0) + (2 x 1) + (1 x 0) = 2
			- 011 or 3 is this because (4 x 0) + (2 x 1) + (1 x 1) = 3
			- A 4th bit is needed for 8 so 1000 or 8 is this because #### = 2<sup>3</sup> 2<sup>2</sup> 2<sup>1</sup> 2<sup>0</sup> = 8 4 2 1. So 1000 or 8 is this because (8 x 1) + (4 x 0) + (2 x 0) + (1 x 0) = 8
	- Binary Digit - where the term bit comes from **bi**gi**t**. A bit is 0 or 1
	- Computers represent a bit as for exmple a light bulb. Number 0 would be the bulb off, Number 1 would be the bulb on.
		- In computers there are switches (transistors) that are wither switched on or off.
		- Computers utilize paterns to represent higher numbers than 0 or 1
	- A Byte is 8 bits (########)
		- ex/ 00000000 = 0, 11111111 = 255


## Representation
- Computers can represent characters such as 'A' as 65 or in binary as 01000001
- ASCII is a mapping between characters and numbers
	- ex/ 01001000 01001001 00100001 = 72 73 33 = 'HI!'
	- Numbers have their own numbers to reprsent them as well. ex/ 1 is 49
- In the end it is about context. The same patterns of numbers that represent text can represent colors in another program.
- Using only 8 bits (1 byte) ASCII could have 256 possibilities of representing characters with numbers
	- Solution to represent the other characters missing is to add another digit, use 2 bytes instead of 1 and so on
	- The soltuion is called **Unicode**
		- **Unicode** is just a mapping of numbers to characters but on a larger scale to rperesent different languages and characters that ASCII does not cover
		- Using as many 23 bits to represent characters leads to 4 billion possible number representations. This lead to adding Emojis.
			- ex/ 11110000 10011111 10011000 10000010 = 4036991106 = 😂 (looks different on iOS and Android because they are essentially just fonts and are rendered differently)
			- For emojis where you can change skin tone  they have re-usable patterns that represent the skin tones themselves and  if the emoji code is followed by that pattern the skin color changes
			- This has expanded to emojis that have multiple emojis within them. ex/ 💑 each person and the heart are represented by their own pattern, now you can switch out the left or right person with a different gender and then you assemble the 3 different patterns to create a more complicated emoji.
- RGB - Red, Green, Blue. Used to create all of the colors as an assembly as an amount of red, green and blue. Each one is 1 byte so  (0 - 255 of red), (0 - 255 of green), (0 - 255 of blue).
	- 72 73 33 = 72 (🟥) 73 (🟩) 33 (🟦) = 🟫
	- Pixel - dot on the screen, each pixel is 3 bytes (RGB)
	- A video then is pixels that are changing values over time
		- FPS = Frames Per Second = Each frame is an individual image, a video is just a sequence of images
- Digitizing sound is done by giving each note or frequency its own value over time

## Algorithm
- Step by step instructions on how to solve a problem
- **Psuedocode**
	- Step by step instructions written in human language rather than in code
		- Verbs = functions
		- Ifs, Elses = conditionals
			- Conditons for the conditionals = boolean expressions
		- Cycles of repeating tasks = loops

## Abstraction
- The simplification of something so you don't have to focus on the lower level details, but the overall goal itself
	- ex/ a car is an abstraction, you don't care or know how it works exactly you just know it is a way to get you somewhere