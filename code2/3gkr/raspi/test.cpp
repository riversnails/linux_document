#include <opencv2/opencv.hpp>
#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <iostream>
#include "camcon.h"

using namespace cv;
using namespace std;

/*
VideoCapture capture;

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
			destroyWindow("face");
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
			destroyWindow("eyes");
			break;
		}
	}
}
*/

int main(int argc, char** argv)
{
	int idx = init_cam(0);
	if(idx == -1) return -1;
	
	if(recordVideo("video.h264")) printf("in");
	face_streaming();
	while(1);
	/*
	if(!inputVideo.isOpened()){
		std::cerr << "Could not open camera" << std::endl;
	}
	
	Mat videoFrame;
	
	Size size = Size((int)inputVideo.get(CAP_PROP_FRAME_WIDTH), (int)inputVideo.get(CAP_PROP_FRAME_HEIGHT));
	
	int fourcc = VideoWriter::fourcc('X', '2', '6', '4');
	
	float fps = inputVideo.get(CAP_PROP_FPS);
	
	bool isColor = true;
		
	outputVideo.open("test.h264", fourcc, fps, size, isColor);

	if(!outputVideo.isOpened())
	{
		cout << "Can't write vide !!!" << std::endl;
	}
	
	
	while(1) {
		inputVideo >> videoFrame;
		
		if(videoFrame.empty()) break;
		
		outputVideo << videoFrame;
		
		imshow("frame", videoFrame);
		
		if(waitKey(1000 / fps) == 27) break;
	}
	
	destroyWindow("frame");
	
	while(1);
	*/
	/*
	Mat image;
	image = imread("lake_gray.jpg", 1);
	namedWindow("lake_gray.jpg", WINDOW_AUTOSIZE);
	imshow("lake_gray.jpg", image);
	waitKey(0);
	printf("hello");
	*/
	
	/*
	Mat frame;
	VideoCapture capture;
	capture.release();
	capture.open(0);
	
	CascadeClassifier face_cascade;
	face_cascade.load("/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml");
	
	
	namedWindow("webCame", WINDOW_AUTOSIZE);
		
		while(1)
		{
			capture >> frame;
			if(frame.empty())break;
			
			
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
			//-- Show what you got
			imshow("webCame", frame );
			
			waitKey(10);
		}
		*/
	
	/*
	while(cap.isOpened())
	{
		cap >> frame;
		if(frame.empty())
		{
			break;
		}
		imshow("Live", frame);
		if(waitKey(5) >= 0) break;
	}*/
	
	/*
	Mat img = imread("people.jpeg");
    String st = "/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml";
    CascadeClassifier face_cascade = CascadeClassifier(st);
    Mat gray_img;
    cvtColor(img, gray_img, COLOR_BGR2GRAY, 0);
    
    namedWindow("lake_gray.jpg", WINDOW_AUTOSIZE);
	imshow("lake_gray.jpg", gray_img);
	waitKey(0);
	*/
	
    /*
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5);
    
    for (x,y,w,h) in faces
    {
        rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2);
	}
        
    imshow('img', img);
    waitKey(0);
    destroyAllWindows();*/
	return 0;
}
