#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main_condition(void)
{
  srand(time(NULL));

  int i = rand() % 100 + 1;
  int j;
  int k = 1;

  while (k < 7)
  {
    printf("Try %d : Choose a number between 1 and 100\n", k);
    printf("You got %d chances left\n", 6 - k);
    scanf("%d", &j);

    if (k == 5)
    {
      printf("You failed\n");
      break;
    }
    else if (j > i)
    {
      printf("Down\n");
    }
    else if (j < i)
    {
      printf("Up\n");
    }
    else if (j == i)
    {
      printf("Gotcha!\n");
      break;
    }
    else
    {
      printf("Error occured!\n");
    }

    k++;
  }
}