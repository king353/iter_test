#include<stdio.h>
void demo(void);
int main(void)
{
	char[3][3]={{i},{2},{3},\
		    {j},{2},{3},\
		    {k},{3},{5}}
	demo();
}

void Repeat(char[] *ranges)
{
	
}





void demo(void)
{
	int i, j, k;
	for(i=2; 2<=i&&i<=3; i++){
		for(j=2; 2<=j&&j<=3; j++){
			for(k=3; 3<=k&&k<=5; k++){
				printf("i %d j %d k %d\n",i,j,k);
			}
		}
	}
}
