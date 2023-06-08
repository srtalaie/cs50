#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  // Check to make sure user is providing only 1 argument, the file name
  if (!argv[1])
  {
    printf("Please provide an argument.\n");
    return 1;
  }
  else if (argc > 2)
  {
    printf("Please provide only 1 argument.\n");
    return 1;
  }

  // Open file in read mode
  FILE *memory_card = fopen(argv[1], "r");

  // Initialize arrays for buffer and to hold name of the file to be written to
  BYTE buffer[512];
  char filename[8];

  int jpeg_count = 0;