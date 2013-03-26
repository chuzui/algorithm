/*
 * Item.h
 *
 *  Created on: 2013-2-25
 *      Author: chuzui
 */

#ifndef ITEM_H_
#define ITEM_H_

typedef int Key ;
typedef char* Value;

//typedef struct Item{
//	Key key;
//	Value value;
//} Item;

typedef int Item;
#define key(i) (i->key)
#define value(i) (i->value)
#define ex(x,y) {Item t; t=x; x=y; y=t;}
#define le(x,y) ((x) < (y))

#endif /* ITEM_H_ */
