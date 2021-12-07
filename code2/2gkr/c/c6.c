#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	int child, status;

	if(fork() == 0)
	{
		int a = atoi(argv[1]);
		for(int i = 1; i <= 9; i++) 
		{
			printf("%d * %d = %d\n", a, i, a*i);
		}
		printf("1\n\n");
		exit(1);
	}

	if(fork() == 0)
	{
		int big = atoi(argv[1]);
		int cal = 0;

		if(big < atoi(argv[2]))
		{
			big = atoi(argv[2]);
		}
		
		for(int i = 0; i <= big; i++)
		{ 
			cal += i;
		}

		printf("%d\n", cal);
		printf("2\n\n");
		exit(2);
	}
	
	
	child = wait(&status);
	printf("%dmain\n\n", child);
	return 0;
}
