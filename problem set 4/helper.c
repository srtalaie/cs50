#include "helpers.h"
#include <math.h>

void swap_pixels(RGBTRIPLE *left_pixel, RGBTRIPLE *right_pixel);

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
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      float sepiaRed = (.393 * image[i][j].rgbtRed) + (.769 * image[i][j].rgbtGreen) + (.189 * image[i][j].rgbtBlue);
      float sepiaGreen = (.349 * image[i][j].rgbtRed) + (.686 * image[i][j].rgbtGreen) + (.168 * image[i][j].rgbtBlue);
      float sepiaBlue = (.272 * image[i][j].rgbtRed) + (.534 * image[i][j].rgbtGreen) + (.131 * image[i][j].rgbtBlue);

      if (sepiaRed > 255)
      {
        sepiaRed = 255;
      }
      if (sepiaBlue > 255)
      {
        sepiaBlue = 255;
      }
      if (sepiaGreen > 255)
      {
        sepiaGreen = 255;
      }

      image[i][j].rgbtRed = round(sepiaRed);
      image[i][j].rgbtBlue = round(sepiaBlue);
      image[i][j].rgbtGreen = round(sepiaGreen);
    }
  }

  return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
  for (int i = 0; i < height; i++)
  {
    for (int j = 0, last_pixel = (width - 1); j < width / 2; j++)
    {
      swap_pixels(&image[i][j], &image[i][last_pixel]);
      last_pixel--;
    }
  }

  return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
  return;
}

void swap_pixels(RGBTRIPLE *left_pixel, RGBTRIPLE *right_pixel)
{
  RGBTRIPLE temp = *left_pixel;
  *left_pixel = *right_pixel;
  *right_pixel = temp;
}