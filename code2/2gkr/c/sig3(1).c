#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

void handler(int signo);

int pid;
int status = 0;
int main() {
	pid = fork();
	signal(SIGTSTP, handler);
	signal(SIGINT, handler);
	if(pid == 0) {
		printf("child start\n");
		while(1);
	}
	else{
		printf("parent start\n");
		sleep(10);
		if(!status) {
			printf("kill child\n");
			kill(pid, SIGTSTP);
			exit(0);
		}
		printf("parent dead\n");
		while(1);
	}
}
                                                                                
void handler(int signo) {
	if(signo == SIGTSTP) {
		if(pid == 0) {
			printf("child dead\n");
		}else {
			printf("parent dead\n");
		}
		exit(0);
	}
	if(SIGINT == signo) 
{
		if(pid == 0) 
{
		}
		else {
			kill(pid, SIGTSTP);
			status = 1;
		}
	}
}
