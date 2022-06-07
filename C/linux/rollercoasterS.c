#include <stdio.h>

int price = 0;
long long money = 0;
int count = 0;
long long solution(int price, long long money, int count);

int main(void)
{
	printf("price setting");
	scanf("%d", &price);
	printf("How much money do you have?");
	scanf("%lld", &money);
	printf("How many time you want to ride this rollercoaster?\n%d money per time", price);
	scanf("%d", &count);

	int notenough = solution(price, money, count);

	if (notenough != 0)
	{
		printf("You need %d money more to ride that much.\n", notenough);
	}
	else if (notenough == 0)
	{
		printf("You can ride it. Enjoy your trip!");
	}

	return 0;
}

long long solution(int price, long long money, int count)
{
	long long answer = 0;
	for (int i = 1; i <= count; i++)
	{
		money = money - price * i;
	}
	if (money < 0)
	{
		return answer = 0 - money;
	}

	return 0;
}