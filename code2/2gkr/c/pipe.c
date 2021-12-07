#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <signal.h>

#define MAXLINE 100

#if 1
void intHandler(int signo);

FILE *fp;
	
int main(int argc, char **argv)
{
	int n, length, fd[2];
	int pid;
	char message[MAXLINE], line[MAXLINE];
	pipe(fd);
	
	if((pid = fork()) == 0)
	{
		close(fd[0]);
		while(1)//message[0] != 0)
		{
			fgets(message, MAXLINE, stdin);
			length = strlen(message)+1;
			write(fd[1], message, length);
		}
	}
	else
	{
		close(fd[1]);
			
		while(1)//line[0] != 0)
		{
			n = read(fd[0], line, MAXLINE);
			printf("%s\n", line);
			
		}
		
	}
	
	exit(0);
}

#else

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

#endif
