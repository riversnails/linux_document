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
	
	printf("* 클라이언트 시작 \n");
	
	printf("파일 이름:\n");
	scanf(" %[^\n]", inmsg);
	write(fd2, inmsg, strlen(inmsg)+1);
	
	name[0] = '\0';
	strcat(name, "download/");
	strcat(name, inmsg);
	printf("%s\n", name);
	
	readLine(fd1, outmsg);
	int as = strcmp(outmsg, "X");
	if(as == 0) 
	{
		printf("out");
		write(fd2, "e%n%d", strlen("e%n%d")+1);
		return 0;
	}
		
	while(1)
	{
		int i = 0;
		//outmsg[0] = '\0';
		//n = read(fd1, outmsg, MAXLINE);
		readLine(fd1, outmsg);
		printf("%s", outmsg);
		int as = strcmp(outmsg, "e%n%d");
		if(as == 0) break;
		fd = fopen(name, "a");
		fputs(outmsg, fd);
		fclose(fd);
	}
	write(fd2, "e%n%d", strlen("e%n%d")+1);
	
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
