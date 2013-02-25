/*
 * main.c
 *
 *  Created on: 2013-2-25
 *      Author: chuzui
 */

#include "sort/quickSort.h"
#include "tool/rand.h"
#include <stdio.h>
#include <stdlib.h>
void printArray(int* a, size_t n)
{
	int i;
	for(i = 0; i < n; i++)
		printf("%d, ", a[i]);
	printf("\n");
}

int main()
{
	int a[12] = {13,12,11,10,9,8,7,6,5,4,3,2};
	//printf("%d\n", GetCount());
	QuickSort(a, 0, 11);
	printArray(a, 12);
	printf("%d", GetCount());
	exit(0);
}

void testRand()
{
	int i;
	for(i = 0; i < 100; i++)
	{
		printf("%d ", randAtoB(3, 9));
	}
}


