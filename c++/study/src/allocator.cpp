/*
 * allocator.cpp
 *
 *  Created on: 2014Äê5ÔÂ13ÈÕ
 *      Author: Administrator
 */

#include <memory>
#include <list>
#include <iostream>
using namespace std;

class W{
public:
	W(int i) : mI(i){};
	void print(){
		cout << mI << endl;
	}
private:
	int mI;
};

int main()
{
	typedef shared_ptr<W> SPW;
	list<SPW> lw;
	while(true) {
		for (int i = 0; i < 10000; i++) {
			SPW w(new W(i));
			lw.push_back(w);
		}
		lw.clear();
	}

}


