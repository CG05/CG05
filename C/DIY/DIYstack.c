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
  int index = 0;
  printf("What index you want to find?");
  scanf("%d", &index);
  data *found = find(index);
  if (found != NULL)
  {
    printf("*******************\n");
    printf("Found\n index : %d\n name: %s\n", found->index, found->name);
    printf("*******************\n");
  }

  for (int i = 0; i < MAX; i++)
  {
    data *node = pop();
    printf("*******************\n");
    printf("index: %d\nname: %s\n", node->index, node->name);
    printf("*******************\n");
    printAll();
  }

  return 0;
}

void push(int index, char *name)
{
  data *node = (data *)malloc(sizeof(data));
  data *temp;

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
    node->before = NULL;
    return;
  }
  else
  {
    temp = head;
    while (temp->next)
    {
      temp = temp->next;
    }
    temp->next = node;
    node->before = temp;
    node->next = NULL;
    tail = node;
  }
  return;
}

data *pop()
{
  if (tail == NULL)
  {
    printf("Stack is empty..\n");
    return NULL;
  }

  data *node = tail;
  if (node == head)
  {
    tail = NULL;
    head = NULL;

    return node;
  }

  data *temp = node->before;
  temp->next = NULL;
  tail = temp;
  return node;
}

data *find(int index)
{
  if (tail == NULL)
  {
    printf("Stack is empty..\n");
    return NULL;
  }

  data *node = tail;
  while (node->index != index)
  {
    if (node->before == NULL)
    {
      printf("Cant find data\n");
      return NULL;
    }

    node = node->before;
  }

  return node;
}

void printAll()
{
  data *temp = head;
  do
  {
    if (temp == NULL)
    {
      printf("ERROR: Unknown NULL data\n");
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
  } while (temp);
}
