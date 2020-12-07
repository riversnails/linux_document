#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#define MAXLINE 1000

int readLine(int fd, char *str);

int main(int argc, char **argv)
{
	FILE* fd;
	int fd1, fd2, n;
	char inmsg[MAXLINE], outmsg[MAXLINE], name[MAXLINE], buffer[MAXLINE];
	
	fd1 = open("./pipefifo1", O_RDONLY);
	fd2 = open("./pipefifo2", O_WRONLY);
	if(fd1 == -1 || fd2 == -1)
	{
		perror("open");
		exit(1);
	}
	
	printf("파일 이름:\n");
	scanf(" %[^\n]", inmsg);
	if (access(inmsg, F_OK) == -1) 
	{
		printf("no\n");
		return 0;
	}
		
	write(fd2, inmsg, strlen(inmsg)+1);
	
		
	fd = fopen(inmsg, "r");
	int i = 0;
	while(fgets(buffer, MAXLINE, fd) != NULL)
	{
		printf("%d %s",i++, buffer);
		write(fd2, buffer, strlen(buffer)+1);
	}
	
	write(fd2, "e%n%d", strlen("e%n%d")+1);
	
	exit(0);
}

int readLine(int fd, char *str)
{
	int n;
	do{
		n = read(fd, str, 1);
	} while(n > 0 && *str++ != NULL);
	return (n>0);
}
