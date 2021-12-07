#include<stdio.h>
#include"student.h"

int main(int argc, char* argv[])
{
	struct student rec;
	FILE *fp;

	if(argc != 2){
		fprintf("잘못된 사용법");
		return 1;
	}

	fp = fopen(argv[1], "wb");
	printf("%-9s %-7s %-4s %-4s\n", "ID", "NAME", "SCORE", "GRADE");
	while (scanf("%d %s %d %d",&rec.id, rec.name, &rec.score, &rec.grade)==4){
		fseek(fp, (rec.id - START_ID)*sizeof(rec), SEEK_SET);
		fwrite(&rec, sizeof(rec), 1, fp);
	}

	fclose(fp);
	return 0;
}
