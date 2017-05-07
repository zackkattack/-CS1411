#include <stdio.h>

void main(){

	int grade, sum;
	float average;

	for(int i = 0; i < 10; i++){
		printf("Enter a students grade:");
		scanf("%d", &grade);
		
		sum += grade;

	}
	
	average = sum/10;
	printf("The class average is: %f\n", average);

}
