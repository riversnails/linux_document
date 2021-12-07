#include <stdio.h>
#include <wiringPi.h>
#include <softTone.h>
#include "Wrapper.h"

unsigned int melody[8] = { 262, 294, 330, 349, 392, 440, 494, 523};
int idx = 0;

int main(int argc, char *argv[])
{
	if(wiringPiSetup() == -1)
	{
		return -1;
	}
	
	init_Active_Buzzer(5);
	init_Passive_Buzzer(4);
	init_LED(1);
	init_Ultrasonic(6, 26);
	init_PushSwitch(27);
	
	while(1)
	{
		LED(1, HIGH);
		Passive_Buzzer(4, 1, melody[idx++]);
		Active_Buzzer(5, HIGH);
		
		delay(500);
		
		LED(1, LOW);
		Passive_Buzzer(4, 0, 0);
		Active_Buzzer(5, LOW);
		printf("ultra:%lf\n", Ultrasonic(6, 26));
		printf("button:%d\n\n", PushSwitch(27, 0));
		delay(500);
		
		if(idx == 7) idx = 0;
	}
	return 0;
}
