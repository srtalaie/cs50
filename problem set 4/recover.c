#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

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
  char *old_filename = argv[1];
  FILE *lost_jpeg = fopen(old_filename, "r");

  BYTE buffer[512];

  char new_filename[8];
  FILE *recovered_jpeg = NULL;

  int jpeg_count = 0;

  while (fread(&buffer, 512, 1, lost_jpeg) == 1)
  {
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
      if (!(jpeg_count == 0))
      {
        fclose(recovered_jpeg);
      }

      sprintf(new_filename, "%03i.jpg", jpeg_count);
      recovered_jpeg = fopen(new_filename, "w");
      jpeg_count++;
    }

    if (!(jpeg_count == 0))
    {
      fwrite(&buffer, 512, 1, recovered_jpeg);
    }
  }
  fclose(lost_jpeg);
  fclose(recovered_jpeg);

  return 0;
}