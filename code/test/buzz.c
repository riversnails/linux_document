#include <stdio.h>
#include <wiringPi.h>
#include <softTone.h>

#define ULTRASONIC_TRIG 0
#define ULTRASONIC_ECHO 2
#define BUZ_PIN 21

int start_time = 0, end_time = 0;
float distance = 0, duration = 0;
int duty = 200, toggle = 0;
long c = 0, p = 0;

unsigned int melody[8] = { 262, 294, 330, 349, 392, 440, 494, 523};

int main()
{
	
	if(wiringPiSetup() == -1)
	{
		return -1;
	}
	
	pinMode(ULTRASONIC_TRIG, OUTPUT);
	pinMode(3, OUTPUT);
	pinMode(ULTRASONIC_ECHO, INPUT);
	pinMode(BUZ_PIN, SOFT_TONE_OUTPUT);
	softToneCreate(BUZ_PIN);
	
	while(1)
	{
		c = millis();
		if(c-p > duty)
		{
			p = c;
			if(toggle == 0)
			{
				toggle = 1;
				digitalWrite(3, HIGH);
			}
			else if(toggle	== 1)
			{
				toggle = 0;
				digitalWrite(3, LOW);
			}
			
		}
		
		digitalWrite(ULTRASONIC_TRIG, LOW);
		delay(500);
		digitalWrite(ULTRASONIC_TRIG, HIGH);
		delayMicroseconds(10);
		digitalWrite(ULTRASONIC_TRIG, LOW);
		


		while(digitalRead(ULTRASONIC_ECHO) == LOW)
		{ 
			start_time = micros();
			//printf("start_time => %d\n", start_time);
		}
		
		while(digitalRead(ULTRASONIC_ECHO) == HIGH) 
		{
			end_time = micros();
			//printf("end_time => %d\n", end_time);
		}
		
		duration = (float)(end_time - start_time);
		distance = duration / 58;
		//printf("%f %f\n", end_time, start_time);
		printf("%f\n", distance);
		if(distance > 0 && distance <= 10) duty = 100;
		else if(distance > 10 && distance <= 30) duty = 500;
		else if(distance > 40 && distance <= 50) duty = 1000;
		delay(10);
		
	}
}
