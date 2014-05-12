#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <functional>
#include "fopow.hpp"
using namespace std;
using namespace std::placeholders;

//int main()
//{
//    vector<int> l1 = {1,2,3,4,5,6,7,8,9};
//
//    transform(l1.begin(), l1.end(), ostream_iterator<float>(cout, " "), bind(fopow<float, int>(), 3, _1));
//
//    transform(l1.begin(), l1.end(), ostream_iterator<float>(cout, " "), bind(fopow<float, int>(), _1, 3));
//}
