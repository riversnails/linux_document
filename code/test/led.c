#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

int num = 0;
int cnt = 0;

int main(int argc, char *argv[])
{
	if(wiringPiSetup() == -1)
	{
		return -1;
	}
	
	pinMode(2, OUTPUT);
	num = atoi(argv[1]);
	printf("%d \n", num);
	
	while(cnt++ != num)
	{
		delay(500);
		digitalWrite(2, HIGH);
		delay(500);
		digitalWrite(2, LOW);
	}
}
