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
  RGBTRIPLE copy[height][width];
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      copy[i][j] = image[i][j];
    }
  }

  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      int red_total = 0;
      int green_total = 0;
      int blue_total = 0;
      float total_pixels = 0;

      for (int neighbor_column = -1; neighbor_column < 2; neighbor_column++)
      {
        for (int neighbor_row = -1; neighbor_row < 2; neighbor_row++)
        {
          if (i + neighbor_column < 0 || i + neighbor_column > (height - 1))
          {
            continue;
          }

          if (j + neighbor_row < 0 || j + neighbor_row > (width - 1))
          {
            continue;
          }

          red_total += copy[i + neighbor_column][j + neighbor_row].rgbtRed;
          green_total += copy[i + neighbor_column][j + neighbor_row].rgbtGreen;
          blue_total += copy[i + neighbor_column][j + neighbor_row].rgbtBlue;
          total_pixels++;
        }
      }

      image[i][j].rgbtRed = round(red_total / total_pixels);
      image[i][j].rgbtGreen = round(green_total / total_pixels);
      image[i][j].rgbtBlue = round(blue_total / total_pixels);
    }
  }

  return;
}

void swap_pixels(RGBTRIPLE *left_pixel, RGBTRIPLE *right_pixel)
{
  RGBTRIPLE temp = *left_pixel;
  *left_pixel = *right_pixel;
  *right_pixel = temp;
}