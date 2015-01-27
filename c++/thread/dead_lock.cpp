#include <iostream>
#include <thread>
#include <Windows.h>
#include <mutex>
using namespace std;

class X
{
private:
	int t;
	mutex m;

public:
	X(int const& _t) : t{ _t }{}
	friend void swap_safe(X& lhs, X& rhs)
	{
		if (&lhs == &rhs)
			return;
		lock(lhs.m, rhs.m);
		lock_guard<mutex> lock_a(lhs.m, adopt_lock);
		Sleep(1000);
		lock_guard<mutex> lock_b(rhs.m, adopt_lock);
		swap(lhs.t, rhs.t);
		cout << lhs.t << "  " << rhs.t << endl;
	}
};

void swap_safe(X& lhs, X& rhs); 

int main1()
{
	X a(4);
	X b(5);
	thread t1(swap_safe, ref(a), ref(b));
	thread t2(swap_safe, ref(b), ref(a));
	t1.join();
	t2.join();

	return 0;
}