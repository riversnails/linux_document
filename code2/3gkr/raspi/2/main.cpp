#include "camcon.h"
#include <stdio.h>

int main()
{
	int idx = init_cam(0);
	if(idx == -1) return -1;
	
	picture("hello.jpg", false, 400, 400);
	recordVideo("video.h264");
	face_streaming();
	eyes_streaming();
	printf("end\n");
	save_gray("hello.jpg");
	return 0;
}
