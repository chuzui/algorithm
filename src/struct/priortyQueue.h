/*
 * priortyQueue.h
 *
 *  Created on: 2013-2-25
 *      Author: chuzui
 */
#include <stdlib.h>
//#include "Item.h"
#ifndef PRIORTYQUEUE_H_
#define PRIORTYQUEUE_H_

typedef int Item;
typedef struct queue{
	Item* itemArray;
	int n;
	int size;
	}_queue;
typedef _queue* Queue;

#define less(x,y) ((x)<(y))
#define ex(x,y) {Item t; t = (x); (x) = (y); (y) = t;}
#define QUEUE_SIZE sizeof(_queue)
#define INIT_SIZE 8
Queue initQueue(Item* a, int n);
Queue insertQueue(Queue q, Item i);
Queue extractMinQueue(Queue q);
Queue decreaseKey(Queue q, Item i);

#endif /* PRIORTYQUEUE_H_ */
