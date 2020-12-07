#include<stdio.h>
#include"student.h"

int main(int argc, char* argv[])
{
	struct student rec;
	int id;
	char c;
	FILE *fp;

	if(argc != 2){
		fprintf("잘못된 사용법");
		return 1;
	}

	if((fp = fopen(argv[1], "rb+")) == NULL){
		fprintf(stderr, "File Open Error\n");
		return 2;
	}

	do{
		printf("Modify Grade : ");
		if(scanf("%d", &id) == 1){
			fseek(fp, (id - START_ID)*sizeof(rec), SEEK_SET);
			if((fread(&rec, sizeof(rec), 1, fp) > 0) && (rec.id != 0)){
				printf("ID : %8d NAME : %4s SCORE : %4d GRADE : %4d\n", rec.id, rec.name, rec.score, rec.grade);
				printf("New Grade : ");
				scanf("%d", &rec.grade);
				fseek(fp, -sizeof(rec), SEEK_CUR);
				fwrite(&rec, sizeof(rec), 1, fp);
			}
			else printf("No Record %d\n", id);
		}
		else printf("Input Error\n");

		printf("Continue? (Y/N)");
		scanf(" %c", &c);
	}while(c == 'Y');

	fclose(fp);
	return 0;
}
