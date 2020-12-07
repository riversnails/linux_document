#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void intHandler(int signo);
void quitHandler(int signo);
void tstpHandler(int signo);

int main()
{	
	signal(SIGINT, intHandler);
	signal(SIGQUIT, quitHandler);
	signal(SIGTSTP, Handler);
	
	while(1)
	{
		printf("work\n");
		sleep(1);
	}
	printf("not work");
}

void intHandler(int signo)
{
	
	printf("number : %d\n", signo);
	printf("signal : SIGINT\n");
	
}

void quitHandler(int signo)
{
	
	printf("number : %d\n", signo);
	printf("signal : SIGQUIT\n");
}

void Handler(int signo)
{
	
	printf("number %d\n", signo);
	printf("signal sigtstp\n");
	
	exit(1);
}


