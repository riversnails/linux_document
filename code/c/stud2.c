#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct student{
	int id;
	char name[20];
	struct student *next;
};

int main()
{
	struct student *ptr, *head = NULL;
	int count = 0, id;
	char name[20];
	
	printf("학번과 이름을 입력하세요\n");
	
	while(scanf("%d %s", &id, name) == 2)
	{
		ptr = (struct student *) malloc(sizeof(struct student));
		if(ptr == NULL)
		{
			perror("malloc");
			exit(2);
		}
		
		ptr->id = id;
		strcpy(ptr->name, name);
		
		ptr->next = head;
		head = ptr;
	}
	
	printf("\n* 학생 정보(역순) *\n");
	ptr = head;
	while(ptr!= NULL)
	{
		count++;
		printf("%d %s\n", ptr->id, ptr->name);
		ptr = ptr->next;
	}
	
	exit(0);

}
