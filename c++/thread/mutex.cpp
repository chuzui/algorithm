#include <iostream>
#include <mutex>
#include <thread>
#include <vector>
#include <algorithm>
#include <windows.h>

using namespace std;
int a = 0;
mutex mut;

void read_and_add(int& t)
{
	while (true)
	{		
		//lock_guard<mutex> guard(mut);
		int b = t;
		Sleep(100);
		t += 1;
		cout << b << endl;
	}
}

int tmain()
{
	int N = 10;
	vector<thread> threads(N);
	for (int i = 0; i < 10; ++i)
	{
		threads[i] = thread(read_and_add, ref(a));
	}

	for_each(threads.begin(), threads.end(), mem_fn(&thread::join));
	return 0;
}