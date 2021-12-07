#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void intHandler(int signo);

int main()
{	
	signal(SIGINT, intHandler);
	
	
	while(1)
	{
		printf("work\n");
		sleep(1);
	}
	printf("not work");
}

void intHandler(int signo)
{
	
	for(int i=1; i<6; i++)
	{
		sleep(1);
		printf("%d sec\n", i);
	}
	
}

