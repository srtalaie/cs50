#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

string convert_text_to_upper(string input);
int check_key_length(string input);
int check_key_alpha_char(string input);
int check_key_duplicates(string input);
string convert_text(string plaintext, string key);

int main(int argc, string argv[])
{
  if (!argv[1])
  {
    printf("Please provide a key containing 26 characters.\n");
    return 1;
  }
  else if (argc > 2)
  {
    printf("Please provide 1 key containing 26 characters.\n");
    return 1;
  }
  else if (check_key_length(argv[1]) == 1)
  {
    printf("Key must contain 26 characters.\n");
    return 1;
  }
  else if (check_key_alpha_char(argv[1]) == 1)
  {
    printf("All characters in the key must be alpha characters.\n");
    return 1;
  }
  else if (check_key_duplicates(argv[1]) == 1)
  {
    printf("All characters in the key must be unique.\n");
    return 1;
  }

  string plaintext = get_string("plaintext: ");
  string upper_key = convert_text_to_upper(argv[1]);
  string ciphertext = convert_text(plaintext, upper_key);
  printf("ciphertext: %s\n", ciphertext);
}

string convert_text(string plaintext, string key)
{
  const string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  char ciphertext[strlen(plaintext)];

  for (int i = 0, len = strlen(plaintext); i < len; i++)
  {
    for (int j = 0, alpha_len = strlen(alphabet); j < alpha_len; j++)
    {
      if (toupper(plaintext[i]) == alphabet[j])
      {
        if (islower(plaintext[i]))
        {
          ciphertext[i] = tolower(key[j]);
        }
        else
        {
          ciphertext[i] = key[j];
        }
      }
      else if (ispunct(plaintext[i]) || isspace(plaintext[i]))
      {
        ciphertext[i] = plaintext[i];
      }
      else if (isdigit(plaintext[i]))
      {
        ciphertext[i] = plaintext[i];
      }
      else if (plaintext[i] == '\0')
      {
        ciphertext[i] = '\0';
      }
    }
  }
  string message = strncpy(plaintext, ciphertext, strlen(plaintext));
  return message;
}

string convert_text_to_upper(string text)
{
  char upper_string[strlen(text)];

  for (int i = 0, len = strlen(text); i < len; i++)
  {
    if (islower(text[i]))
    {
      upper_string[i] = toupper(text[i]);
    }
    else
    {
      upper_string[i] = text[i];
    }
  }
  return strncpy(text, upper_string, strlen(text));
}

int check_key_length(string input)
{
  int return_value = 0;
  int input_len = strlen(input);

  if (input_len > 26 || input_len < 26)
  {
    return_value = 1;
  }
  return return_value;
}

int check_key_alpha_char(string input)
{
  int return_value = 0;
  int input_len = strlen(input);

  for (int i = 0; i < input_len; i++)
  {
    if (!isalpha(input[i]))
    {
      return_value = 1;
    }
  }
  return return_value;
}

int check_key_duplicates(string input)
{
  int key_length = strlen(input);
  string upper_key = convert_text_to_upper(input);
  int return_value = 0;

  for (int i = 0; i < key_length - 1; i++)
  {
    for (int j = i + 1; j < key_length; j++)
    {
      if (input[i] == input[j])
      {
        return_value = 1;
      }
    }
  }
  return return_value;
}