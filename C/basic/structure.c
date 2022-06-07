#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 5마리의 고양이
// 아무키를 눌러서 랜덤으로 고양이를 뽑되
// 5마리 모두 다 수집하면 열심히 키우면 됨
// 중복발생가능

//고양이
//이름, 나이, 성격, 키우기 난이도(레벨)
typedef struct
{
  char *name;
  int age;
  char *character;
  int level;
} CAT;

//현재까지 보유한 고양이
int collection[5] = {0, 0, 0, 0, 0};

CAT cats[5];

void initCats();
void printCat(int selected);
int checkCollection();

int main(void)
{
  srand(time(NULL));

  initCats();
  while (1)
  {
    printf("어느 고양이가 나올까요..?\n아무 키나 눌러서 확인하세요!\n");
    getchar();

    int selected = rand() % 5; //고양이 뽑기
    printCat(selected);        //고양이 뽑기 결과 출력
    //고양이 뽑기 처리
    collection[selected] = 1;
    int collectAll = checkCollection();
    if (collectAll == 1)
    {
      break;
    }
  }

  return 0;
}
void initCats()
{
  cats[0].name = "깜냥이";
  cats[0].age = 5;
  cats[0].character = "온순";
  cats[0].level = 1;

  cats[1].name = "귀요미";
  cats[1].age = 1;
  cats[1].character = "애교";
  cats[1].level = 2;

  cats[2].name = "까칠이";
  cats[2].age = 2;
  cats[2].character = "까칠";
  cats[2].level = 3;

  cats[3].name = "순둥이";
  cats[3].age = 3;
  cats[3].character = "온순";
  cats[3].level = 4;

  cats[4].name = "하양이";
  cats[4].age = 2;
  cats[4].character = "까칠";
  cats[4].level = 5;
}

void printCat(int selected)
{
  printf("\n== 당신은 이 고양이의 집사가 되었어요! ==\n");
  printf(" 이름      : %s\n", cats[selected].name);
  printf(" 나이      : %d\n", cats[selected].age);
  printf(" 성격      : %s\n", cats[selected].character);
  printf(" 레벨      : ");
  for (int i = 0; i < cats[selected].level; i++)
  {
    printf("%s", "★");
  }
  printf("\n");
}

int checkCollection()
{
  //현재 보유한 고양이 목록 출력
  //다 모았는지 여부 반환
  int collectAll = 1;

  printf("\n\n=== 보유한 고양이 목록입니다 ===\n\n");
  for (int i = 0; i < 5; i++)
  {
    if (collection[i] == 0)
    {
      printf("%10s", "(빈 박스)");
      collectAll = 0;
    }
    else
    {
      printf("%10s", cats[i].name);
    }
  }
  printf("\n===================================\n");

  if (collectAll == 1)
  {
    printf("\n\n축하합니다! 모든 고양이를 다 모으셨어요!\n");
  }

  return collectAll;
}