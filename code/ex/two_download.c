#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#define DEFAULT_PROTOCOL 0
#define MAXLINE 1000

int reload(int* sfd, struct sockaddr_un serverAddr);
int readLine(int fd, char* str);

int main(int argc, char **argv)
{
	FILE* fd;
	int sfd, result;
	char inmsg[MAXLINE], outmsg[MAXLINE], name[MAXLINE];
	struct sockaddr_un serverAddr;
	
	sfd = socket(AF_UNIX, SOCK_STREAM, DEFAULT_PROTOCOL);
	serverAddr.sun_family = AF_UNIX;
	strcpy(serverAddr.sun_path, "up_down");
	
	do{
		result = connect(sfd, (struct sockaddr *) &serverAddr, sizeof(serverAddr));
		if(result == -1) sleep(1);
	}while(result == -1);
	
	
	
	name[0] = '\0';
	printf("1파일 이름:\n");
	scanf(" %[^\n]", inmsg);
	write(sfd, inmsg, strlen(inmsg)+1);
	
	readLine(sfd, outmsg);
	int as = strcmp(outmsg, "X");
	if(as == 0) return 0;
		
	strcat(name, "download/");
	strcat(name, inmsg);
	printf("%s\n", name);
	
	while(1)
	{
		reload(sfd, serverAddr);
		fd = fopen(name, "a");
		readLine(sfd, outmsg);
		printf("%s", outmsg);
		int as = strcmp(outmsg, "e%n%d");
		if(as == 0) break;
		fputs(outmsg, fd);
		fclose(fd);
	}
	
	
	close(sfd);
	exit(0);
}

int reload(int* sfd, struct sockaddr_un serverAddr)
{	
	int result;
	close(sfd);
	sfd = socket(AF_UNIX, SOCK_STREAM, DEFAULT_PROTOCOL);
	serverAddr.sun_family = AF_UNIX;
	strcpy(serverAddr.sun_path, "up_down");
	
	do{
		result = connect(sfd, (struct sockaddr *) &serverAddr, sizeof(serverAddr));
		if(result == -1) sleep(1);
	}while(result == -1);
	sleep(0.1);
}

int readLine(int fd, char* str)
{
	int n;
	do{
		n = read(fd, str, 1);
	} while(n > 0 && *str++ != NULL);
	return(n > 0);
}
