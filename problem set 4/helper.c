#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
  float average_rgbt;

  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      average_rgbt = ((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0);

      image[i][j].rgbtRed = round(average_rgbt);
      image[i][j].rgbtBlue = round(average_rgbt);
      image[i][j].rgbtGreen = round(average_rgbt);
    }
  }

  return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
  return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
  return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
  return;
}
