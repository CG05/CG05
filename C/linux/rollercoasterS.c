#include <stdio.h>

int money = 0;
int count = 0;
int time = 0;
int solution(int money, int num, int *ptime);

int main(void){
	printf("How much money do you have?");
	scanf("%d", &money);
	printf("How many time you want to ride this rollercoaster?\n100 money per time");
	scanf("%d", &count);	

	int notenough = solution(money, count, &time);

	if(notenough != 0){
		printf("You don't have that much money. Sorry.\nYou can ride only %d times.\n", time);
		printf("You need %d money more to ride that much.\n", notenough);
	}else if(notenough == 0){
		printf("You can ride it. Enjoy your trip!");
	}

	return 0;
	
}


int solution(int money, int count, int *ptime){
	int notenough = 0;
	for(int i = 1; i <= count; i++){
		money = money - 100*i;
		if(money < 0){
			notenough = 0 - money;
			*ptime = i - 1;
		}
	}
	if(money < 0){
		notenough = 0 - money;
	}

	return notenough;
}