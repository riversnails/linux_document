#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main()
{
	int child;
        char command[2];
        char option[2];
	scanf("%s %s", command, option);

        if(fork() == 0)
        {
                execl("/bin/ls", command, option, NULL);
                exit(1);
        }
}
