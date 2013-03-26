/*
 * bst.c
 *
 *  Created on: 2013-2-27
 *      Author: chuzui
 */
#include <stddef.h>
#include "bst.h"
static void walk_recursive(link b, void(*ptr)(Item));

BST initBST()
{
	BST head = (BST)malloc(SIZE_BST);
	head->head = NULL;
	return head;
}

void walkBST(BST b, void(*ptr)(Item))
{
	walk_recursive(root(b), ptr);
}

void walk_recursive(link b, void(*ptr)(Item))
{
	if(b != NULL)
	{
		walk_recursive(lc(b), ptr);
		ptr(key(b));
		walk_recursive(rc(b), ptr);
	}
}

void insertBST(BST b, Item i)
{
	link x, y, z;
	x = root(b);
	y = NULL;
	z = (link)calloc(1,SIZE_NODE);
	z->key = i;
	while(x!=NULL)
	{
		y = x;
		if(le(i,key(x)))
			x = lc(x);
		else
			x = rc(x);
	}
	pa(z) = y;
	if(y == NULL)
	{
		root(b) = z;
	}
	else if(le(i,key(y)))
	{
		lc(y) = z;
	}
	else
	{
		rc(y) = z;
	}
}

