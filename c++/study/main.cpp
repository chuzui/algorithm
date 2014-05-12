#include <stdio.h>
#include <iostream>
#include <initializer_list>

/*void print(std::initializer_list<int> vals)
{

	for (auto p = vals.begin(); p!= vals.end(); ++p)
	{
		std::cout << *p << "\n";
	}
}*/

void lamda()
{
	int x = 89;
	int y = 66;
	auto l = [=]{
		std::cout << x << std::endl;
		};
	l();
}
//int main(int argc, char **argv)
//{
//	int x;
//	lamda();
//	std::cout << R"nc(\\\\)nc";
//	std::cin >> x;
//	std::cin >> x;
//
//	printf("hello world\n");
//	return 0;
//}
