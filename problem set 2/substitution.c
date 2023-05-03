#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int check_input(string input);
string convert_text_to_upper(string input);
string convert_text(string plaintext, string key);

int main(int argc, string argv[])
{
  if (!argv[1])
  {
    printf("Please provide a key containing 26 characters");
    return 1;
  }
  else if (argc > 2)
  {
    printf("Please provide 1 key containing 26 characters");
    return 1;
  }

  check_input(argv[1]);

  string plaintext = get_string("plaintext: ");
  string upper_plaintext = convert_text_to_upper(plaintext);
  string upper_key = convert_text_to_upper(argv[1]);

  string ciphertext = convert_text(upper_plaintext, upper_key);
  printf("ciphertext: %s\n", ciphertext);
}

int check_input(string input)
{
  int input_len = strlen(input);

  if (input_len > 26)
  {
    printf("Key must contain 26 characters");
    return 1;
  }

  for (int i = 0; i < input_len; i++)
  {
    if (!isalpha(input[i]))
    {
      printf("All characters in the key must be alpha characters.");
      return 1;
    }
  }
  return 1;
}

string convert_text(string plaintext, string key)
{
  const string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  char ciphertext[strlen(plaintext)];

  for (int i = 0, len = strlen(plaintext); i < len; i++)
  {
    for (int j = 0, alpha_len = strlen(alphabet); j < alpha_len; j++)
    {
      if (plaintext[i] == alphabet[j])
      {
        ciphertext[i] = key[j];
      }
      else if (ispunct(plaintext[i]) || isspace(plaintext[i]))
      {
        ciphertext[i] = plaintext[i];
      }
    }
  }
  string message = strncpy(plaintext, ciphertext, strlen(ciphertext));
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