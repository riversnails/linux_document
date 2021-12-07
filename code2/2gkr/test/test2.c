#include <stdio.h>
#include <wiringPi.h>

int toggle = 0, toggle2 = 0;

int main()
{
	if(wiringPiSetup() == -1)
	{
		return -1;
	}
	
	pinMode(0, OUTPUT);
	pinMode(2, INPUT);
	pinMode(3, INPUT);
	
	while(1)
	{
		printf("%d %d\n", toggle, toggle2);
		if(digitalRead(3) == 1)
		{
			if(toggle == 0)
			{
				toggle = 1;
			}
			else if(toggle == 1)
			{
				toggle = 0;
			}
		}
		
		if(toggle = 0)
		{
			if(digitalRead(2) == 1)
			{
				digitalWrite(0, HIGH);
			}
			else if(digitalRead(2) == 0)
			{
				digitalWrite(0, LOW);
			}
		}
		delay(50);
	}
}
