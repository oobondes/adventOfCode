//this script solves the problem here ----> https://adventofcode.com/2021/day/1
#include<stdio.h>
int measurements[] = {199,200,208,210,200,207,240,269,260,263};

int main(){
    int loops = (sizeof measurements)/4;

    //loops through list to see how many times the measurement increases
    int count = 0;
    for (int i = 1; i < loops; i++)
    {
        if (measurements[i] > measurements[i-1]){
            count++;
        }
    }

    //loops through the list again to see how many times the group of three measurements increases
    int count2 = 0;
    loops = loops;
    for (int i = 3; i < loops; i++)
    {
        if (measurements[i] + measurements[i-1] + measurements[i-2] > measurements[i-1] + measurements[i-2] + measurements[i-3]){
            count2++;
        }
    }

    //prints answers for parts 1 and 2 of the problem
    printf("ans: %d\n", count);
    printf("ans2: %d\n",count2);
    return 0;
}