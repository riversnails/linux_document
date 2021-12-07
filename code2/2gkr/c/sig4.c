#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void handler(int sig)
{
	printf("signal no(%d), Receuved\n", sig);
}

int main()
{
	if(signal(SIGUSR1, handler) == SIG_ERR)
	{
		fprintf(stderr, "can not set USER1\n");
		exit(1);
	}
	
	if(signal(SIGUSR2, handler) == SIG_ERR)
	{
		fprintf(stderr, "can not set USER2\n");
		exit(1);
	}
	
	for(;;)
		pause(); 
}
