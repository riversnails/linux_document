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

void toUpper(char* in, char* out);
int readLine(int fd, char* str);

int main(int argc, char **argv)
{
	FILE* fd;
	int sfd, cfd, clientlen, cnt;
	int type = -1;
	char inmsg[MAXLINE], outmsg[MAXLINE], buffer[MAXLINE], name[MAXLINE];
	struct sockaddr_un serverAddr, clientAddr;
	
	if(access("upload", F_OK) == -1) // 디렉터리 생성
	{
		system("mkdir upload");
	}
	if(access("download", F_OK) == -1) // 디렉터리 생성
	{
		system("mkdir download");
	}
	
	signal(SIGCHLD, SIG_IGN);
	clientlen = sizeof(clientAddr);
	
	sfd = socket(AF_UNIX, SOCK_STREAM, DEFAULT_PROTOCOL);
	serverAddr.sun_family = AF_UNIX;
	strcpy(serverAddr.sun_path, "up_down");
	unlink("up_down");
	bind(sfd, (struct sockaddr *) &serverAddr, sizeof(serverAddr));
	listen(sfd, 5);
	
	
	
	while(1)
	{
		cfd = accept(sfd, (struct sockaddr *) &clientAddr, &clientlen);
		
		readLine(cfd, inmsg);
		printf("%d %s", type, inmsg);
		
		if (access(inmsg, F_OK) == -1) 
		{
			write(cfd, "X", strlen("X")+1);
			continue;
		}
		else write(cfd, "O", strlen("O")+1);
		
		int i = 0;
		for(i = 0; i < MAXLINE - 1; i++) name[i] = '\0';
		strcat(name, inmsg);
		printf("	%s\n", name);
		inmsg[0] = '\0';
		
		fd = fopen(name, "r");
		while(fgets(buffer, MAXLINE, fd) != NULL)
		{
			printf("%s", buffer);
			cfd = accept(sfd, (struct sockaddr *) &clientAddr, &clientlen);
			write(cfd, buffer, strlen(buffer)+1);
		}
		cfd = accept(sfd, (struct sockaddr *) &clientAddr, &clientlen);
		write(cfd, "e%n%d", strlen("e%n%d")+1);
		fclose(fd);
		type = -1;
		
		
		close(cfd);
	}
	
}

int readLine(int fd, char* str)
{
	int n;
	do{
		n = read(fd, str, 1);
	} while(n > 0 && *str++ != NULL);
	return(n > 0);
}
