#include <stdio.h>
#include <business_card.h>

int main(int argc, char *argv[])
{
	FILE *fp1, *fp2, *fp3;
	char buffer[100][100];
	business bus[200];
	int line = 0;

	if(argc != 2)
	{
		printf("error\n");
		return -1;
	}
	
	fp1 = fopen("test1.txt", "r");

	while(fgets(buffer[line], 100, fp1) != NULL)
	{
		line++;
	}

	
	for(int i = 0; i < line; i++)
	{
		fputs(buffer[i], fp3);
	}
	return 0;
}
