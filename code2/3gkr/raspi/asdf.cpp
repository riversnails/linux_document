#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <stdlib.h>
#include <iostream>

using namespace std;
using namespace cv;

int main(){


	
	
	Mat img;
	
	VideoCapture capture(0);
	
	int count = 2;
	char savefile[200];
	
	if(!capture.isOpened()){
		std::cerr << "Could not open camera" << std::endl;
		return -1;
	}
	
	namedWindow("webcame", 1);
	
	capture >> img;
		
	resize(img, img, Size(100, 100),0,0,INTER_CUBIC);
		
	sprintf(savefile, "image%d.jpg", count++);
	imwrite(savefile, img);
			
	
	return 0;
}
