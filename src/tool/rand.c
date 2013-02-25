#include <stdlib.h>
#include "rand.h"

int randAtoB(int a, int b)
{
	int randNum = a + (double)rand() / (RAND_MAX + 1) * (b-a);
	return randNum;
}
