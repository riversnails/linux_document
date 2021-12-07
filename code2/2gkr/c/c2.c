#include <stdio.h>

int main(int argc, char *argv[])
{
	FILE *fp1, *fp2, *fp3;
	char buffer[100][100];
	int line = 0;

	
	fp1 = fopen("test1.txt", "w+");
	fp2 = fopen("test2.txt", "w+");
	fp3 = fopen("test.txt", "w+");

	fputs("qweiourweqiouwet \n", fp1);

	fputs("sdfjkjnfsdkj", fp2);
	
	fclose(fp1);
	fclose(fp2);
	fp1 = fopen("test1.txt", "r");
	fp2 = fopen("test2.txt", "r");

	while(fgets(buffer[line], 100, fp1) != NULL)
	{
		line++;
	}

	while(fgets(buffer[line], 100, fp2) != NULL)
	{
		line++;
	}
	

	for(int i = 0; i < line; i++)
	{
		fputs(buffer[i], fp3);
	}
	return 0;
}
