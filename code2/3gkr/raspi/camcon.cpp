#include "camcon.h"

using namespace std;
using namespace cv;
VideoCapture capture;

int init_cam(int id)
{
	capture.release();
	capture.open(id);
	
	if(!capture.isOpened()){
		return -1;
	}
	return 0;
}

void picture(char *fileName, bool showWindow, int width, int height)
{
	Mat img;
	
	capture >> img;
	
	if(showWindow) 
	{
		namedWindow("picturewebCam", WINDOW_AUTOSIZE);
		imshow("picturewebCam", img);
	}
	
	resize(img, img, Size(width, height),0,0,INTER_CUBIC);
		
	
	imwrite(fileName, img);
}

int recordVideo(char *fileName)
{
	Mat frame, reframe;
	VideoWriter videoWriter;
	
	float videoFPS = capture.get(cv::CAP_PROP_FPS);
	int videoWidth = capture.get(cv::CAP_PROP_FRAME_WIDTH);
	int videoHeight = capture.get(cv::CAP_PROP_FRAME_HEIGHT);
	
	videoWriter.open(fileName, cv::VideoWriter::fourcc('X', '2', '6', '4'), 
	videoFPS , cv::Size(videoWidth, videoHeight), true);
	
	if(!videoWriter.isOpened())
	{
		return -1;
	}
	
	namedWindow("videowebCam", WINDOW_AUTOSIZE);
	
	while(1)
	{
		capture >> frame;
		if(frame.empty()) break;
		
		videoWriter << frame;
		imshow("videowebCam", frame);
		char c = waitKey(1000 / videoFPS);
		if(c == 27) 
		{
			capture.release();
			destroyWindow("videowebCam");
			return 1;
		}
	}
	return 0;
}

void face_streaming()
{
	Mat frame;
	CascadeClassifier face_cascade;
	face_cascade.load("/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml");
	
	namedWindow("face", WINDOW_AUTOSIZE);
		
	while(1)
	{
		capture >> frame;
		if(frame.empty()) break;
		
		Mat frame_gray;
		cvtColor( frame, frame_gray, COLOR_BGR2GRAY );
		equalizeHist( frame_gray, frame_gray );
		//-- Detect faces
		std::vector<Rect> faces;
		face_cascade.detectMultiScale( frame_gray, faces );
		for ( size_t i = 0; i < faces.size(); i++ )
		{
			Point center( faces[i].x + faces[i].width/2, faces[i].y + faces[i].height/2 );
			ellipse( frame, center, Size( faces[i].width/2, faces[i].height/2 ), 0, 0, 360, Scalar( 255, 0, 255 ), 4 );
			Mat faceROI = frame_gray( faces[i] );
		}
		imshow("face", frame);
		char c = waitKey(10);
		if(c == 27)
		{
			capture.release();
			destroyWindow("videowebCam");
			 break;
		}
	}
}

void eyes_streaming()
{
	Mat frame;
	CascadeClassifier face_cascade;
	face_cascade.load("/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml");
	CascadeClassifier eyes_cascade;
	eyes_cascade.load("/usr/local/share/opencv4/haarcascades/haarcascade_eye.xml");

	namedWindow("eyes", WINDOW_AUTOSIZE);
		
	while(1)
	{
		capture >> frame;
		if(frame.empty()) break;
		
		Mat frame_gray;
		cvtColor( frame, frame_gray, COLOR_BGR2GRAY );
		equalizeHist( frame_gray, frame_gray );
		//-- Detect faces
		std::vector<Rect> faces;
		face_cascade.detectMultiScale( frame_gray, faces );
		for ( size_t i = 0; i < faces.size(); i++ )
		{
			//Point center( faces[i].x + faces[i].width/2, faces[i].y + faces[i].height/2 );
			//ellipse( frame, center, Size( faces[i].width/2, faces[i].height/2 ), 0, 0, 360, Scalar( 255, 0, 255 ), 4 );
			Mat faceROI = frame_gray( faces[i] );
			
			//-- In each face, detect eyes
			std::vector<Rect> eyes;
			eyes_cascade.detectMultiScale( faceROI, eyes );
			for ( size_t j = 0; j < eyes.size(); j++ )
			{
				Point eye_center( faces[i].x + eyes[j].x + eyes[j].width/2, faces[i].y + eyes[j].y + eyes[j].height/2 );
				int radius = cvRound( (eyes[j].width + eyes[j].height)*0.25 );
				circle( frame, eye_center, radius, Scalar( 255, 0, 0 ), 4 );
			}
		}
		
		imshow("eyes", frame);
		char c = waitKey(10);
		if(c == 27) 
		{
			capture.release();
			destroyWindow("videowebCam");
			break;
		}
	}
}

void save_gray(char *filename)
{
	char name[100];
	Mat frame_gray, file = imread(filename);
	cvtColor( file, frame_gray, COLOR_BGR2GRAY );
	equalizeHist( frame_gray, frame_gray );
	
	strcat(name, "gray_");
	strcat(name, filename);
	imwrite(name, frame_gray);
}
