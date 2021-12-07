#include "camcon.h"

void init_cam()
{
	system("sudo raspi-config");
}

void picture(char *name)
{
	char val[100] = "raspistill -o ";
	strcat(val, name);
	system(val);
}

void adv_picture(char *name)
{
	char val[100] = "raspistill ";
	strcat(val, name);
	system(val);
}

void video(char *name)
{
	char val[100] = "raspivid -o ";
	strcat(val, name);
	system(val);
}

void adv_video(char *name)
{
	char val[100] = "raspivid ";
	strcat(val, name);
	system(val);
}
