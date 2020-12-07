#include <stdio.h>
#include <wiringPi.h>

int arr[10];
int idx = 0;
int toggle = 0;
int pin = 0;

int main()
{
	for(int i  = 0; i < 10; i++)
	{
		arr[i] = 0;
	}
			
	if(wiringPiSetup() == -1)
	{
		return -1;
	}
	
	pinMode(0, INPUT);
	
	while(1)
	{
		pin = digitalRead(0);
		// printf("now %d %d %d	", pin, toggle, idx);
		
		if(pin == 1)
		{
			toggle = 1;
			arr[idx++] = 1;
			if(idx == 9)
			{
				idx = 0;
				printf("long");
				for(int i  = 0; i < 10; i++)
				{
					arr[i] = 0;
				}
			}	
		}
		else if(pin == 0 && toggle == 1)
		{
			toggle = 0;
			idx = 0;
			
			int count = 0;
			for(int i = 0; i < 10; i++)
			{
				if(arr[i] == 1) count++;
				else continue;
			}
			
			if(count > 0 && count < 4)
			{
				printf("short");
			}
			else if (count >= 4 && count < 8)
			{
				printf("long");
			}
			
			for(int i  = 0; i < 10; i++)
			{
				arr[i] = 0;
			}
		}
		
	
		printf("\n");
		delay(50);
	}
}
