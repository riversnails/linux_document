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

	if((fp = fopen(argv[1], "rb")) == NULL){
		fprintf(stderr, "File Open Error\n");
		return 2;
	}

	printf("%10s %6s %6s %6s\n", "학년", "이름", "점수", "석차");

	while(fread(&rec, sizeof(rec), 1, fp) > 0)
		if(rec.id != 0) printf("%10d %6s %6d %6d\n", rec.id, rec.name, rec.score, rec.grade);

	fclose(fp);
	return 0;
}
