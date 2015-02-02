#include <future>
#include <iostream>
#include <Windows.h>

int find_answer(int i)
{
	Sleep(1000);
	return i * i;
}

void do_other()
{
	std::cout << "hahha" << std::endl;
}

int main2()
{
	auto answer = std::async(find_answer, 5);
	do_other();
	std::cout << answer.get();
	return 0;
}