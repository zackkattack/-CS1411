#include <stdio.h>

void main()
{

	int month, year;

	printf("Enter the month:");
	scanf("%d", &month);

	printf("Enter the year");
	scanf("%d", &year);

	switch(month){
		case 4:
		case 6:
		case 9:
			printf("31 days\n");
			break;

		case 2:
			if(year%4 == 0){ printf("29 days\n");}
			if(year%4 != 0){ printf("28 days\n");}
			break;
		default:
			printf("31 days\n");
			break;
	}
}
