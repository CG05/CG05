#include <stdio.h>

int main_loop(void)
{
  int floor;
  printf("how many floor?: ");
  scanf("%d", &floor);

  int i = 0;
  while (i < floor - 1)
  {
    for (int k = 0; k < floor - i - 1; k++)
    {
      printf(" ");
    }
    int j = 0;
    do
    {
      printf("*");
      j++;
    } while (j < i * 2 + 1);
    printf("\n");
    i++;
  }

  return 0;
}