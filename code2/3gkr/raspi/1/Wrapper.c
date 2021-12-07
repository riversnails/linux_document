#include "Wrapper.h"

void init_Active_Buzzer(int pin)
{
	pinMode(pin, OUTPUT);
}
void Active_Buzzer(int pin, int type)
{
	digitalWrite(pin, type);
}
void init_Passive_Buzzer(int pin)
{
	pinMode(pin, SOFT_TONE_OUTPUT);
	softToneCreate(pin);
}
void Passive_Buzzer(int pin, int type, int hz)
{
	if(type == 0) softToneWrite(pin, 0);
	else if(type == 1) softToneWrite(pin, hz);
}
void off_Passive_Buzzer(int pin)
{
	softToneStop(pin);
}
void init_LED(int pin)
{
	pinMode(pin, OUTPUT);
}
void toggle_LED(int pin, int time)
{
	for(int i = 0; i < time; i++)
	{
		digitalWrite(pin, HIGH);
		delay(500);
		digitalWrite(pin, LOW);	
		delay(500);
	}
}
void LED(int pin, int type)
{
	digitalWrite(pin, type);
}
void init_Ultrasonic(int trig, int echo)
{
	pinMode(trig, OUTPUT);
	pinMode(echo, INPUT);
}
double Ultrasonic(int trig, int echo)
{
	unsigned long start_time, end_time;
	long duration;
	
	digitalWrite(trig, LOW);
	delay(1);
	digitalWrite(trig, HIGH);
	delayMicroseconds(10);
	digitalWrite(trig, LOW);
	
	while(digitalRead(echo) == LOW)
	{ 
		start_time = micros();
	}
	
	while(digitalRead(echo) == HIGH) 
	{
		end_time = micros();
	}
	
	duration = (float)(end_time - start_time);
	return duration / 58;
}
void init_PushSwitch(int pin)
{
	pinMode(pin, INPUT);
}
int PushSwitch(int pin, int type) // 0 = down, 1 = up
{
	int read;
	read = digitalRead(pin);
	read - type;
	if(read == -1) read = 1;
	return read; 
} // push == 1, nonpush == 0

