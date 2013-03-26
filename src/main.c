/*
 * main.c
 *
 *  Created on: 2013-2-25
 *      Author: chuzui
 */

#include "sort/quickSort.h"
#include "tool/rand.h"
#include "struct/priorityQueue.h"
#include "struct/bst.h"
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
	testBST();
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

void print(Item i)
{
	printf("%d ", i);
}

void testBST()
{
	Item a[10] = {23,17,14,6,13,10,1,5,7,12};
	BST b = initBST();
	int i;
	for(i = 0; i < 10; i++)
	{
		insertBST(b, a[i]);
	}
	walkBST(b, print);
}




