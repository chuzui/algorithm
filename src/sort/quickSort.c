/*
 * quickSort.c
 *
 *  Created on: 2013-2-25
 *      Author: chuzui
 */
#include <stdlib.h>
#include "quickSort.h"
#include "..\\tool\\rand.h"

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
	#ifdef DEBUG
	++count;
	#endif
	if(l < r)
	{
		int middle = partition(a,l,r);
		QuickSort(a, l, middle - 1);
		QuickSort(a,middle+1, r);
	}
}
int partition(int*a, int l, int r)
{

	int x = a[r];
	int i,j, tmp;
	i = l-1;

	int randIndex = randAtoB(l, r+1);
		tmp = a[r];
		a[r] = a[randIndex];
		a[randIndex] = tmp;

	for(j = l; j < r; j++)
	{
		if(a[j] < x)
		{
			++i;
			tmp = a[i];
			a[i] = a[j];
			a[j] = tmp;
		}
	}
	tmp = a[i+1];
	a[i+1] = a[r];
	a[r] = tmp;
	return i+1;
}

void smallInsertSort(int* array, int n)
{
	 int i;
	 for(i = 1; i < n; i++)
	 {

	 }
}


