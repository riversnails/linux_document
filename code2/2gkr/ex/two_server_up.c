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
		printf("%s", inmsg);
		
		
		int as = strcmp(inmsg, "e%n%d");
		if(as == 0) 
		{
			printf("end");
			cnt = 0;
			continue;
		}
		
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
