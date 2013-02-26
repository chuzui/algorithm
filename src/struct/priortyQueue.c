/*
 * priortyQueue.c
 *
 *  Created on: 2013-2-25
 *      Author: chuzui
 */
#include <stdlib.h>
#include <stddef.h>
#include "priortyQueue.h"

#define left(i) (((i)<<1)+1)
#define right(i) (((i)<<1)+2)
#define parent(i) (((i)-1)>>1)
static void buildMaxHeap(Queue q);
static void maxHeapify(Queue q, int i);

Queue initQueue(Item* a, int n)
{
	Queue q = (Queue)malloc(QUEUE_SIZE);
	if(a != NULL)
	{
		int i = 1;
		while(i < n)
			i = i << 1;
		q->n = n;
		q->size = i;
		q->itemArray = (Item*)malloc(sizeof(Item) * i);
		memcpy(q->itemArray, a, n*sizeof(Item));
		buildMaxHeap(q);
	}
	else
	{
		q->n = 0;
		q->size = INIT_SIZE;
		q->itemArray = (Item*)malloc(sizeof(Item) * INIT_SIZE);
	}
	return q;
}

static void buildMaxHeap(Queue q)
{
	int i, n;
	n = q->n;
	for(i = (n-2)/2; i!= 0; --i)
	{
		maxHeapify(q,i);
	}
}

static void maxHeapify(Queue q, int i)
{
	int l,r,max;
	Item* a = q->itemArray;
	l = left(i);
	r = right(i);
	if(less(a[l],a[r]))
		max = r;
	else
		max = l;
	if(less(a[i], a[max]))
	{
		ex(a[i],a[max]);
		maxHeapify(q, max);
	}
}
