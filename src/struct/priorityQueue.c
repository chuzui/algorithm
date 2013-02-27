/*
 * priortyQueue.c
 *
 *  Created on: 2013-2-25
 *      Author: chuzui
 */
#include <stdlib.h>
#include <stddef.h>
#include <limits.h>
#include "priorityQueue.h"

#define left(i) (((i)<<1)+1)
#define right(i) (((i)<<1)+2)
#define parent(i) (((i)-1)>>1)
#define item(q,i) ((q)->itemArray[(i)])
#define num(q) ((q)->n)
#define size(q) ((q)->size)
#define array(q) ((q)->itemArray)

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

void insertQueue(Queue q, Item i)
{
	++num(q);
	if(num(q) > size(q))
	{
		int newSize;
		Item* tmp;
		newSize = size(q) << 1;
		tmp = array(q);
		array(q) = (Item*)malloc(sizeof(Item)*newSize);
		memcpy(array(q), tmp, size(q) * sizeof(Item));
		size(q) = newSize;
	}
	item(q, (num(q) - 1)) = INT_MIN;
	increaseKey(q, num(q) - 1, i);

}

Item extractMaxQueue(Queue q)
{
	int max;
	if(q->n < 1)
		printf("error: the queue is empty");
	max = q->itemArray[0];
	q->itemArray[0] = q->itemArray[q->n - 1];
	q->n--;
	return max;
}

Item maxQueue(Queue q)
{
	return q->itemArray[0];
}

void increaseKey(Queue q, int i, Item key)
{
	if(less(key, q->itemArray[i]))
		printf("error: key is small than ");
	item(q,i) = key;
	while((i > 0) && (item(q,parent(i)) < item(q,i)))
	{
		ex(item(q,parent(i)), item(q,i));
		i = parent(i);
	}
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
