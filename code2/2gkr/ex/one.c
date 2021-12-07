#include <stdio.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <string.h>

int main(int argc, char **argv)
{
	char dir[100];
	char input[100];
	char buf[100];
	printf("start\n");
	dir[0] = '/';
	dir[1] = '\0';
	
	while(1)
	{
		//printf("\n\n:%s	:%s \n", input, dir);
		printf(": ");
		scanf(" %[^\n]", input);
		strcat(input, "/");
		printf("\n");
		
		if(input[0] == '/' )//&& input[1] == '\n') 
		{
			for(int i = 0; i < 99; i++) dir[i] = '\0';
		}
		if(input[0] == 'l' && input[1] == 's')
		{
			system("ls");
			continue;
		}
		for(int l = 0; l < 99; l++) buf[l] = '\0';
		buf[0] = 'l';
		buf[1] = 's';
		buf[2] = ' ';
		strcat(buf, dir);
		strcat(buf, input);
		if(system(buf) == 0)
		{
			strcat(dir, input);
		}
		else
		{
			printf("fail\n");
		}
		
	}
	return 0;
}

