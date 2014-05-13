/*
 * refCount.cpp
 *
 *  Created on: 2014Äê5ÔÂ12ÈÕ
 *      Author: Administrator
 */
#include <iostream>
#include <cstring>
using namespace std;

static int count;

template<class T>
class RCPtr {
public:
	RCPtr(T* realPtr = 0);
	RCPtr(const RCPtr& rhs);
	~RCPtr();
	RCPtr& operator =(const RCPtr& rhs);
	T* operator ->() const;
	T& operator *() const;
private:
	T *pointee;
	void init();
};

template<class T>
RCPtr<T>::RCPtr(T* realPtr) : pointee(realPtr)
{
	init();
}

template<class T>
RCPtr<T>::RCPtr(const RCPtr& rhs) : pointee(rhs.pointee)
{
	init();
}

template<class T>
void RCPtr<T>::init()
{
	if (pointee == 0) { // if the dumb pointer is
		return; // null, so is the smart one
	}
	if (pointee->isShareable() == false) { // if the value
		pointee = new T(*pointee); // isn't shareable,
	} // copy it
	pointee->addReference(); // note that there is now a new reference to the value
}

class String {
public:
	String(const char *initValue = "");
	String(const String& rhs);
	String& operator =(const String& rhs);
	const char& operator [](int index) const;
	char& operator [](int index);
	~String();
	static void printCount(){
		cout << count << endl;
	}

private:
	struct StringValue{
		int refCount;
		char *data;
		StringValue(const char *initValue);
		StringValue(const StringValue& rhs);
		~StringValue();
	};
	StringValue *value;

};

String::StringValue::StringValue(const char *initValue) : refCount(1)
{
	data = new char[strlen(initValue) + 1];
	strcpy(data, initValue);
}

String::StringValue::StringValue(const StringValue& rhs) : refCount(1)
{
	data = new char[strlen(rhs.data) + 1];
	strcpy(data, rhs.data);
}

String::StringValue::~StringValue()
{
	--count;
	delete []data;
}

String::String(const char* initValue) : value(new StringValue(initValue))
{

}

String::String(const String& rhs) : value(rhs.value)
{
	++value->refCount;
}

String::~String()
{
	if (--value->refCount == 0) delete value;
}

String& String::operator =(const String& rhs)
{
	if (value == rhs.value) {
		return *this;
	}

	if (--value->refCount == 0) {
		delete value;
	}

	value = rhs.value;
	++value->refCount;
	return *this;
}

const char& String::operator[](int index) const
{
	return value->data[index];
}

char& String::operator[](int index)
{
	return value->data[index];
	if (value->refCount > 1) {
		--value->refCount;
		value = new StringValue(value->data);
	}
	return value->data[index];

}
/*
int main()
{
	String a,b,c,d;
	cout << count << endl;
	a = b = c = d = "asdasd";
	cout << count << endl;
}*/

