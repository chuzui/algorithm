/*
 * priortyQueue.h
 *
 *  Created on: 2013-2-25
 *      Author: chuzui
 */
#include <stdlib.h>
#include "Item.h"
#ifndef PRIORTYQUEUE_H_
#define PRIORTYQUEUE_H_

typedef int* Queue;
Queue initQueue(size_t n);
Queue insertQueue(Queue q, Item i);
Queue extractMinQueue(Queue q);
Queue decreaseKey(Queue q, Item i);

#endif /* PRIORTYQUEUE_H_ */
