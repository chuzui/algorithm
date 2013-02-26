/*
 * quickSort.h
 *
 *  Created on: 2013-2-25
 *      Author: chuzui
 */

#ifndef QUICKSORT_H_
#define QUICKSORT_H_
#include <stddef.h>
#include "../struct/Item.h"
#define DEBUG
#define RAND
void QuickSort(int* a, int l, int r);
#ifdef DEBUG
int GetCount();
#endif
#endif /* QUICKSORT_H_ */
