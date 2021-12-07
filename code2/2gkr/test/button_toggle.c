#include <stdio.h>
#include <wiringPi.h>

int toggle = 0;
int pin = 0;
int p_b = 0;

int main()
{
	if(wiringPiSetup() == -1)
	{
		return -1;
	}
	
	pinMode(0, INPUT);
	pinMode(2, OUTPUT);
	
	while(1)
	{
		pin = digitalRead(0);
		printf("%d %d", pin, toggle);
		
		if(pin == 1 && p_b == 0)
		{
			if(toggle == 0)
			{
				digitalWrite(2, HIGH);
			}
			else if(toggle == 1)
			{
				toggle = -1;
				digitalWrite(2, LOW);
			}
			toggle++;
		}
		p_b = pin;
		printf("\n");
		delay(20);
	}
}
