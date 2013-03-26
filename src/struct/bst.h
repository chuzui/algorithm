/*
 * bst.h
 *
 *  Created on: 2013-2-27
 *      Author: chuzui
 */

#ifndef BST_H_
#define BST_H_

#include "Item.h"
typedef struct _node* link;
struct _node{
	Item key;
	link parent;
	link lchild,rlchild;
};

typedef struct bst{
	link head;
}*BST;


#define key(i) ((i)->key)
#define lc(i) ((i)->lchild)
#define rc(i) ((i)->rlchild)
#define pa(i) ((i)->parent)
#define SIZE_NODE sizeof(struct _node)
#define SIZE_BST sizeof(struct bst)

#define root(b) ((b)->head)
BST initBST();
void walkBST(BST b, void(*ptr)(Item));
void insertBST(BST b, Item i);
#endif /* BST_H_ */
