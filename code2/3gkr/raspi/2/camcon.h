#include <stdlib.h>
#include <string.h>
#include <opencv2/opencv.hpp>

int init_cam(int id);
void picture(char *fileName, bool showWindow, int width, int height);
int recordVideo(char *fileName);
void face_streaming();
void eyes_streaming();
void save_gray(char *filename);
