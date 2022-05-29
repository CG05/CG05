#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int randF(int stage);
int randS(int stage);
char *stage_name(int stage);
int get_respond(char stageName[256], int num1, int num2);
int check_answer(int respond, int answer);
void report(int result);

int main(void)
{
  int result;

  for (int stage = 1; stage <= 5; stage++)
  {
    int num1 = randF(stage);
    int num2 = randS(stage);
    int answer = num1 * num2;
    char *stageName = stage_name(stage);

    int respond = get_respond(stageName, num1, num2);
    result = check_answer(respond, answer);
    if (result == 0)
    {
      break;
    }
    else if (result == 1)
    {
      printf("Correct! Go to the next stage\n\n");
    }
  }
  report(result);
  return 0;
}

int randF(int stage)
{
  srand(time(NULL));
  int num1 = rand() % 4 + 1 * stage * stage;
  return num1;
}
int randS(int stage)
{
  srand(time(NULL));
  int num2 = rand() % 5 + 1 * stage * stage;
  return num2;
}
char *stage_name(int stage)
{
  char *stageName = NULL;
  switch (stage)
  {
  case 1:
    stageName = "First stage";
    break;
  case 2:
    stageName = "Second stage";
    break;
  case 3:
    stageName = "Third stage";
    break;
  case 4:
    stageName = "Fourth stage";
    break;
  case 5:
    stageName = "Fifth stage";
    break;

  default:
    break;
  }
  return stageName;
}

int get_respond(char stageName[256], int num1, int num2)
{
  int respond;
  printf("%s\n", stageName);
  printf("%d * %d = ?\n", num1, num2);
  scanf("%d", &respond);

  return respond;
}
int check_answer(int respond, int answer)
{
  if (respond == answer)
  {
    return 1;
  }
  else
  {
    return 0;
  }
}
void report(int result)
{
  if (result == 0)
  {
    printf("You lose. Try Again\n");
  }
  else
  {
    printf("You won! Great Job\n");
  }
}
