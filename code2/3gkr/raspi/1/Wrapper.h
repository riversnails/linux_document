#include <wiringPi.h>
#include <softTone.h>

void init_Active_Buzzer(int pin);
void Active_Buzzer(int pin, int type);
void init_Passive_Buzzer(int pin);
void Passive_Buzzer(int pin, int type, int hz);
void off_Passive_Buzzer(int pin);
void init_LED(int pin);
void LED(int pin, int type);
void init_Ultrasonic(int trig, int echo);
double Ultrasonic(int trig, int echo);
void init_PushSwitch(int pin);
int PushSwitch(int pin, int type);
