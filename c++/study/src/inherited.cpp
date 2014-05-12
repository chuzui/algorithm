/*
 * inherited.cpp
 *
 *  Created on: 2014Äê5ÔÂ12ÈÕ
 *      Author: Administrator
 */
#include <iostream>
#include <vector>
using namespace std;

class Base{
public:
	virtual void update(){
		cout << "base" << endl;
	}
};

class Inherited1: public Base {
public:
	void update(){
		cout << "Inherited1" << endl;
	}
};

class Inherited2: public Base {
public:
	void update(){
		cout << "Inherited2" << endl;
	}
};

/*
int main()
{
	vector<Base*> myObjects;
	Base *i1 = new Inherited1();
	Base *i2 = new Inherited2();
	myObjects.push_back(i1);
	myObjects.push_back(i2);
	for (auto iter = myObjects.begin(); iter != myObjects.end(); ++iter)
	{
		(*iter)->update();
	}
}
*/
