#include <stdio.h>
#include <wiringPi.h>
#include <softTone.h>

#define BUZ_PIN 21

#define NA 255
#define SET_BEAT 254

#define DO 0
#define DO_ 1
#define RE 2
#define RE_ 3
#define MI 4
#define PA 5
#define PA_ 6
#define SL 7
#define SL_ 8
#define LA 9
#define LA_ 10
#define SI 11

unsigned int melody[8] = { 262, 294, 330, 349, 392, 440, 494, 523};

int main()
{
	int idx = 0;
	
	if(wiringPiSetup() == -1)
	{
		printf("error");
		return -1;
	}
	
	pinMode(BUZ_PIN, SOFT_TONE_OUTPUT);
	softToneCreate(BUZ_PIN);
	
	while(1)
	{
		//for(idx=0; idx<8; idx++)
		//{
		//	softToneWrite(BUZ_PIN, melody[idx]);
		//	delay(1000);
		//}
		softToneWrite(BUZ_PIN, melody[4]);
		delay(1000);
		softToneWrite(BUZ_PIN, 0);
		delay(500);
		softToneWrite(BUZ_PIN, melody[4]);
		delay(1000);
		softToneWrite(BUZ_PIN, 0);
		delay(500);
		softToneWrite(BUZ_PIN, melody[5]);
		delay(1000);
		softToneWrite(BUZ_PIN, 0);
		delay(500);
		softToneWrite(BUZ_PIN, melody[5]);
		delay(1000);
		softToneWrite(BUZ_PIN, 0);
		delay(500);
	}
	
	softToneStop(BUZ_PIN);
	delay(500);
	
	return 0;
}
