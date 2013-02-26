/*
 * quickSort.c
 *
 *  Created on: 2013-2-25
 *      Author: chuzui
 */
#include <stdlib.h>
#include "quickSort.h"
#include "..\tool\rand.h"

#ifdef DEBUG
static int count = 0;
#endif

int partition(int*a, int l, int r);

#ifdef DEBUG
int GetCount()
{
	return count;
}
#endif

void QuickSort(int* a, int l, int r)
{

	if(l < r)
	{
		int middle = partition(a,l,r);
		QuickSort(a, l, middle - 1);
		QuickSort(a,middle+1, r);
	}
}
int partition(int*a, int l, int r)
{


	int i,j;
	i = l-1;

#ifdef RAND
	int randIndex = randAtoB(l, r+1);
	ex(a[r], a[randIndex]);
#endif

	int x = a[r];
	for(j = l; j < r; j++)
	{
#ifdef DEBUG
		++count;
#endif
		if(a[j] < x)
		{
			++i;
			ex(a[i],a[j]);
		}
	}
	ex(a[i+1], a[r]);
	return i+1;
}

void smallInsertSort(int* array, int n)
{
	 int i;
	 for(i = 1; i < n; i++)
	 {

	 }
}


