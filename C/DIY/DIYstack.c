#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 10

typedef struct data
{
  struct data *before;
  int index;
  char name[20];
  struct data *next;
} data;

data *head = NULL;
data *tail = NULL;

void push(int index, char *name);
data *pop();
data *find(int index);
void printAll();

int main(void)
{
  for (int i = 0; i < MAX; i++)
  {
    char name[20];
    sprintf(name, "test%d", i);
    push(i, name);
  }

  printAll();

  return 0;
}

void push(int index, char *name)
{
  data *node = (data *)malloc(sizeof(data));
  node->index = index;
  if (name != NULL)
  {
    strcpy(node->name, name);
  }

  if (head == NULL)
  {
    head = node;
    tail = node;
    node->next = NULL;
    return;
  }
  else
  {
    data *temp = head;

    while (temp->next)
    {
      temp = temp->next;
    }
    temp->next = node;
    tail = node;
  }

  return;
}

data *pop()
{
}

data *find(int index)
{
}

void printAll()
{
  data *temp = head;
  do
  {
    if (temp == NULL)
    {
      printf("ERROR: Unknown NULL data");
      break;
    }
    else
    {
      printf("=====================\n");
      printf(" index: %d\n", temp->index);
      printf(" name : %s\n", temp->name);
      printf("=====================\n");
    }
    temp = temp->next;
  } while (temp->next);
}
