#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main_array(void)
{
  srand(time(NULL));
  printf("SELECT right number of medicine\n");

  int answer;
  int medicine = rand() % 4;

  int cntShowBottle = 0;
  int prevCntShowBottle = 0;

  for (int i = 1; i <= 3; i++)
  {
    int bottle[4] = {0, 0, 0, 0};
    do
    {
      cntShowBottle = rand() % 2 + 2;
    } while (cntShowBottle == prevCntShowBottle);
    prevCntShowBottle = cntShowBottle;

    int isIncluded = 0;
    printf("> Try %d:  ", i);

    for (int j = 0; j < cntShowBottle; j++)
    {
      int randBottle = rand() % 4;
      if (bottle[randBottle] == 0)
      {
        bottle[randBottle] = 1;
        if (randBottle == medicine)
        {
          isIncluded = 1;
        }
      }
      else
      {
        j--;
      }
    }

    for (int k = 0; k < 4; k++)
    {
      if (bottle[k] == 1)
      {
        printf("%d ", k + 1);
      }
    }
    printf("using chosen medicine\n\n");

    if (isIncluded == 1)
    {
      printf("Success! It works!\n");
    }
    else
    {
      printf("NOOO it doesn't work!\n");
    }

    printf("\nIf you want to continue press any button\n");
    getchar();
  }
  printf("What number is true medicine?\n");
  scanf("%d", &answer);

  if (answer == medicine + 1)
  {
    printf("Right answer!\n");
  }
  else
  {
    printf("Wrong answer! The answer was %d.\n", medicine + 1);
  }

  return 0;
}