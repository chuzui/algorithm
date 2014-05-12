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
		~StringValue();
	};
	StringValue *value;

};

String::StringValue::StringValue(const char *initValue) : refCount(1)
{
	++count;
	data = new char[strlen(initValue) + 1];
	strcpy(data, initValue);
}

String::StringValue::~StringValue()
{
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

int main()
{
	String a,b,c,d;
	a = b = c = d = "asdasd";
	cout << count << endl;
}

