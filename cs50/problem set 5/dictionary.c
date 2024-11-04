// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
  char word[LENGTH + 1];
  struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 1000;

// Hash table
node *table[N];

int dictionary_size = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
  int input_word_hash = hash(word);
  node *n = table[input_word_hash];

  while (n != NULL)
  {
    if (strcasecmp(word, n->word) == 0)
    {
      return true;
    }
    n = n->next;
  }
  return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
  long hash_value = 0;

  for (int i = 0, length = strlen(word); i < length; i++)
  {
    hash_value += tolower(word[i]);
  }

  return hash_value % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
  FILE *dictionary_file = fopen(dictionary, "r");
  if (dictionary_file == NULL)
  {
    printf("Unable to open the dictionary");
    return false;
  }

  char dictionary_word[LENGTH + 1];

  while (fscanf(dictionary_file, "%s", dictionary_word) != EOF)
  {
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
      printf("Unable to initialize node");
      return false;
    }

    strcpy(n->word, dictionary_word);
    int word_hash = hash(dictionary_word);

    n->next = table[word_hash];
    table[word_hash] = n;
    dictionary_size++;
  }

  fclose(dictionary_file);
  return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
  return dictionary_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
  for (int i = 0; i < N; i++)
  {
    node *n = table[i];

    while (n != NULL)
    {
      node *temp = n;
      n = n->next;
      free(temp);
    }

    if (n == NULL && i == N - 1)
    {
      return true;
    }
  }
  return false;
}
