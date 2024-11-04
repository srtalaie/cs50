#include <cs50.h>
#include <stdio.h>

int get_size(void);
void print_grid(int size);

int main(void)
{
  // Get size of grid
  int n = get_size();

  // Print grid of bricks
  print_grid(n);
}

int get_size(void)
{
  int height;
  do
  {
    height = get_int("Size (between 1 and 8): ");
  } while (height < 1 || height > 8);
  return height;
}

void print_grid(int size)
{
  // Print each row up to the size
  for (int row = 0; row < size; row++)
  {
    // Print spaces starting from the size - 1 and working down
    for (int spaces = size - 1; spaces > row; spaces--)
    {
      printf(" ");
    }
    // Print blocks from 1 going up to the size
    for (int hashes = 0; hashes <= row; hashes++)
    {
      printf("#");
    }
    printf("\n");
  }
}