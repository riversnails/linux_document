#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

#define MAXLINE 1000

int readLine(int fd, char *str);

int main(int argc, char **argv)
{
	FILE *fd;
	int fd1, fd2, n, cnt = 0;
	char inmsg[MAXLINE], outmsg[MAXLINE], name[MAXLINE], buffer[MAXLINE];
	
	
	if(access("pipefifo1", F_OK) == -1)
	{
		if(mkfifo("./pipefifo1", 0666) == -1)
		{
			perror("mkfifo");
			exit(1);
		}
	}
	if(access("pipefifo2", F_OK) == -1)
	{
		if(mkfifo("./pipefifo2", 0666) == -1)
		{
			perror("mkfifo");
			exit(2);
		}
	}
	
	
	fd1 = open("./pipefifo1", O_WRONLY);
	fd2 = open("./pipefifo2", O_RDONLY);
	if(fd1 == -1 || fd2 == -1)
	{
		perror("open");
		exit(3);
	}
	
	printf("* 서버 시작 \n");
	while(1)
	{
		readLine(fd2, inmsg);
		
		int as = strcmp(inmsg, "e%n%d");
		if(as == 0) 
		{
			cnt = 0;
			continue;
		}
		
		printf("%s", inmsg);
		
		if(cnt == 0)
		{
			cnt++;
			int i = 0;
			for(i = 0; i < MAXLINE - 1; i++) name[i] = '\0';
			strcat(name, "upload/");
			strcat(name, inmsg);
			printf("	%s\n", name);
			inmsg[0] = '\0';
		}
		else
		{
			fd = fopen(name, "a");
			fputs(inmsg, fd);
			fclose(fd);
		}
		
	 }
	
	return 0;
}

int readLine(int fd, char *str)
{
	int n;
	do{
		n = read(fd, str, 1);
	} while(n > 0 && *str++ != NULL);
	return (n>0);
}
