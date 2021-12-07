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
	int fd1, fd2, n;
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
		for(int i = 0; i < MAXLINE - 1; i++) name[i] = '\0';
		//n = read(fd2, outmsg, MAXLINE);
		readLine(fd2, outmsg);
		int as = strcmp(outmsg, "e%n%d");
		if(as == 0) continue;
		printf("%s\n", outmsg);
		buffer[0] = '\0';
		if (access(outmsg, F_OK) == -1) 
		{
			write(fd1, "X", strlen("X")+1);
			continue;
		}
		else write(fd1, "O", strlen("O")+1);
		
		
		fd = fopen(outmsg, "r");
		while(fgets(buffer, MAXLINE, fd) != NULL)
		{
			printf("%s", buffer);
			write(fd1, buffer, strlen(buffer)+1);
			sleep(0.1);
		}
		write(fd1, "e%n%d", strlen("e%n%d")+1);
		fclose(fd);
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
