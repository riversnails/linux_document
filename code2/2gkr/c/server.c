#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

#define MAXLINE 256

void intHandler(int signo);

FILE *fp;

int main(int argc, char **argv)
{
	int fd1, fd2, n;
	char msg[MAXLINE];
	char server[10] = "서버:";
	char client[20] = "클라이언트:";
	char cash[50];
	
	signal(SIGINT, intHandler);
	
	if(mkfifo("./chatfifo1", 0666) == -1)
	{
		perror("mkfifo");
		exit(1);
	}
	if (mkfifo("./chatfifo2", 0666) == -1)
	{
		perror("mkfifo");
		exit(2);
	}
	
	fd1 = open("./chatfifo1", O_WRONLY);
	fd2 = open("./chatfifo2", O_RDONLY);
	if(fd1 == -1 || fd2 == -1)
	{
		perror("open");
		exit(3);
	}
	
	fp = fopen("log.txt", "a");
	
	printf("* 서버 시작 \n");
	while(1)
	{
		 printf("[서버]:");
		 fgets(msg, MAXLINE, stdin);
		 n = write(fd1, msg, strlen(msg)+1);
		 cash[0] = '\0';
		 strcat(cash, server);
		 fputs(strcat(cash, msg), fp);
		 if(n == -1)
		 {
			 perror("write");
			 exit(1);
		 }
		 n = read(fd2, msg, MAXLINE);
		 printf("[클라이언트] -> %s\n", msg);
		 cash[0] = '\0';
		 strcat(cash, client);
		 fputs(strcat(cash, msg), fp);
		 
	 }
	return 0;
}

void intHandler(int signo)
{
	fclose(fp);
	exit(0);
}

