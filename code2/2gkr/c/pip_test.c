/*
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#define MAXLINE 100

int main(int argc, char **argv)
{
	int n, length, fd[2];
	int pid;
	char message[MAXLINE], line[MAXLINE];
	pipe(fd);
	
	if((pid = fork()) == 0)
	{
		close(fd[0]);
		scanf("%s", &message);
		length = strlen(message)+1;
		write(fd[1], message, length);
	}
	else
	{
		close(fd[1]);
		n = read(fd[0], line, MAXLINE);
		printf("[%d] %s\n", getpid(), line);
	}
	
	exit(0);
}
*/

/*
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#define MAXLINE 100

int main(int argc, char **argv)
{
	int n, length, fd[2];
	int pid;
	char message[MAXLINE], line[MAXLINE];
	pipe(fd);
	
	if((pid = fork()) == 0)
	{
		close(fd[0]);
		dup2(fd[1], 1);
		close(fd[1]);
		printf("sdf");
	}
	else
	{
		close(fd[1]);
		while((n = read(fd[0], line, MAXLINE)) > 0)
		write(STDOUT_FILENO, line, n);
	}
	
	exit(0);
}*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <signal.h>

#define MAXLINE 100
	
void intHandler(int signo);

FILE *fp;
	
int main(int argc, char **argv)
{
	signal(SIGINT, intHandler);
	int n, length, fd[2];
	int pid;
	char message[MAXLINE], line[MAXLINE];
	pipe(fd);
	
	if((pid = fork()) == 0)
	{
		close(fd[0]);
		while(1)//message[0] != 0)
		{
			scanf("%s", &message);
			length = strlen(message)+1;
			write(fd[1], message, length);
		}
	}
	else
	{
		close(fd[1]);
		fp = fopen("test.txt", "a");
			
		while(1)//line[0] != 0)
		{
			n = read(fd[0], line, MAXLINE);
			printf("[%d] %s\n", getpid(), line);
			
			fputs(line, fp);
		}
		
	}
	
	exit(0);
}

void intHandler(int signo)
{
	fclose(fp);
	exit(0);
}

