#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 10마리의 서로 다른 동물 (각 카드 2장 씩)
//사용자로부터 2개의 입력값을 받아서
//->같은 동물 찾으면 카드 뒤집기
//->다른 동물 찾으면 원상복구
//모든 동물 쌍을 찾으면 게임 종료
//총 실패 횟수 알려주기

int arrayAnimal[4][5]; // 카드 지도 (20장의 카드)
int checkAnimal[4][5]; //뒤집혔는지 여부 확인
char *strAnimal[10];

void initAnimalArray();
void initAnimalName();
void shuffleAnimal();
void printAnimals();
void printQuestions();
int foundAllAnimals();

int getEmptyPosition();
int conv_pos_x(int x);
int conv_pos_y(int y);

int main_m_array(void)
{

  srand((unsigned)time(NULL));
  initAnimalName();
  initAnimalArray();
  shuffleAnimal();

  int failCount = 0;

  while (1)
  {
    int select1 = 0;
    int select2 = 0;

    printAnimals();
    printQuestions();

    printf("0부터 19까지, 뒤집을 카드를 2개 고르세요 : ");
    scanf("%d %d", &select1, &select2);

    if (select1 == select2)
      continue;
    //같은 카드 선택 시 무효

    // 좌표에 해당하는 카드를 뒤집어보고 같은지 안같은지 확인
    int firstSelect_x = conv_pos_x(select1);
    int firstSelect_y = conv_pos_y(select1);

    int secondSelect_x = conv_pos_x(select2);
    int secondSelect_y = conv_pos_y(select2);
    //입력받은 정수를 좌표로 변환
    //뒤집히지 않은 카드 && 같은 동물
    if (checkAnimal[firstSelect_x][firstSelect_y] == 0 && checkAnimal[secondSelect_x][secondSelect_y] == 0)
    {
      if (arrayAnimal[firstSelect_x][firstSelect_y] == arrayAnimal[secondSelect_x][secondSelect_y])
      {
        printf("\n\n 빙고! : %s 발견 \n\n", strAnimal[arrayAnimal[firstSelect_x][firstSelect_y]]);
        checkAnimal[firstSelect_x][firstSelect_y] = 1;
        checkAnimal[secondSelect_x][secondSelect_y] = 1;
      }
      else
      {
        printf("\n\n 땡! 틀렸습니다)\n");
        printf("%d : %s", select1, strAnimal[arrayAnimal[firstSelect_x][firstSelect_y]]);
        printf("%d : %s", select2, strAnimal[arrayAnimal[secondSelect_x][secondSelect_y]]);
        printf("\n\n");

        failCount++;
      }
    }

    else
    {
      printf("\n\n 이미 뒤집힌 카드입니다)\n");
      printf("%d : %s", select1, strAnimal[arrayAnimal[firstSelect_x][firstSelect_y]]);
      printf("%d : %s", select2, strAnimal[arrayAnimal[secondSelect_x][secondSelect_y]]);
      printf("\n\n");

      failCount++;
    }

    if (foundAllAnimals() == 1)
    {
      printf("\n\n축하합니다! 모든 동물을 다 찾았네요 \n");
      printf("지금까지 %d번 실수하셨습니다.", failCount);
      break;
    }
  }

  return 0;
}

void initAnimalArray()
{
  for (int i = 0; i < 4; i++)
  {
    for (int j = 0; j < 5; j++)
    {
      arrayAnimal[i][j] = -1; //빈공간 = -1
    }
  }
}

void initAnimalName()
{
  strAnimal[0] = "원숭이";
  strAnimal[1] = "하마";
  strAnimal[2] = "강아지";
  strAnimal[3] = "고양이";
  strAnimal[4] = "돼지";
  strAnimal[5] = "코끼리";
  strAnimal[6] = "기린";
  strAnimal[7] = "낙타";
  strAnimal[8] = "타조";
  strAnimal[9] = "호랑이";
}

void shuffleAnimal()
{
  for (int i = 0; i < 10; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      int pos = getEmptyPosition();
      int x = conv_pos_x(pos);
      int y = conv_pos_y(pos);

      arrayAnimal[x][y] = i;
    }
  }
}

void printAnimals()
{
  for (int i = 0; i < 4; i++)
  {
    for (int j = 0; j < 5; j++)
    {
      printf("%8s", strAnimal[arrayAnimal[i][j]]);
    }
    printf("\n");
  }
  printf("\n======================================\n");
}
void printQuestions()
{
  printf("\n\n(문제)\n");
  int seq = 0;
  for (int i = 0; i < 4; i++)
  {
    for (int j = 0; j < 5; j++)
    {
      //카드를 뒤집어서 정답을 맞추면 동물 이름
      if (checkAnimal[i][j] != 0)
      {
        printf("%s", strAnimal[arrayAnimal[i][j]]);
      }
      //맞추지 못했으면 뒷면
      else
      {
        printf("%d", seq);
      }
    }
    printf("\n");
  }
  printf("\n");
}

int foundAllAnimals()
{
  for (int i = 0; i < 4; i++)
  {
    for (int j = 0; j < 5; j++)
    {
      if (checkAnimal[i][j] == 0)
      {
        return 0;
      }
    }
  }
  return 1; //모두 다 찾음
}

int getEmptyPosition()
{
  while (1)
  {
    int randPos = rand() % 20;
    // 19 -> (3,4) 변환 필요.
    int x = conv_pos_x(randPos);
    int y = conv_pos_y(randPos);

    if (arrayAnimal[x][y] == -1)
    {
      return randPos;
    }
  }
  return 0;
}

int conv_pos_x(int x)
{

  return x / 5; // int x/5 : 5로 나눈 몫이 나옴.
}
int conv_pos_y(int y)
{

  return y % 5; // %: 나누고 몫이 나온 나머지가 나옴.
}
