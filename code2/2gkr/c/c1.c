#include <stdio.h>

int main(int argc, char *argv[])
{
	FILE *fp;
	char buffer[15][100];
	int line =0;

	if(argc != 2)
	{
		printf("error\n");
		return -1;
	}
	
	fp = fopen(argv[1], "r");

	while(fgets(buffer[line], 100, fp) != NULL)
	{
		line++;
	}

	for(int i = line - 1; i >= 0; i--)
	{
		printf("%s", buffer[i]);
	}
	return 0;
}
