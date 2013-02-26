/*
 * main.c
 *
 *  Created on: 2013-2-25
 *      Author: chuzui
 */

#include "sort/quickSort.h"
#include "tool/rand.h"
#include "struct/priortyQueue.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 10000

void printArray(int* a, size_t n)
{
	int i;
	for(i = 0; i < n; i++)
		printf("%d, ", a[i]);
	printf("\n");
}

int main()
{
//	int a[N], i;
//	for(i = N; i > 0; --i)
//	{
//		a[N-i] = i;
//	}
	//srand(time(0));
	//QuickSort(a, 0, N-1);

	Item a[10] = {23,17,14,6,13,10,1,5,7,12};
	Queue q = initQueue(a, 10);
	printArray(q->itemArray, 10);

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


