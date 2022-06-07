#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct data
{
  struct data *before;
  int index;
  char name[20];
  struct data *next;
} data;

data *head = NULL;
data *tail = NULL;