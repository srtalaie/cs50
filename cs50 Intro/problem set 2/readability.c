#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
void calculate_reading_level(int letters, int words, int sentences);

int main(void)
{
  string text = get_string("Text: ");

  int letters = count_letters(text);
  int words = count_words(text);
  int sentences = count_sentences(text);

  calculate_reading_level(letters, words, sentences);
}

int count_letters(string text)
{
  int letter_count = 0;
  for (int i = 0, len = strlen(text); i < len; i++)
  {
    if (isalpha(text[i]))
    {
      letter_count++;
    }
  }
  return letter_count;
}

int count_words(string text)
{
  int word_count = 1;
  for (int i = 0, len = strlen(text); i < len; i++)
  {
    if (isblank(text[i]))
    {
      word_count++;
    }
  }
  return word_count;
}

int count_sentences(string text)
{
  int sentence_count = 0;
  for (int i = 0, len = strlen(text); i < len; i++)
  {
    if (ispunct(text[i]) && (text[i] == '.' || text[i] == '!' || text[i] == '?'))
    {
      sentence_count++;
    }
  }
  return sentence_count;
}

void calculate_reading_level(int letters, int words, int sentences)
{
  const float L = ((float)letters / (float)words) * 100;
  const float S = ((float)sentences / (float)words) * 100;
  int index = round((0.0588 * L) - (0.296 * S) - 15.8);

  if (index > 16)
  {
    printf("Grade 16+\n");
  }
  else if (index < 1)
  {
    printf("Before Grade 1\n");
  }
  else
  {
    printf("Grade %i\n", index);
  }
}