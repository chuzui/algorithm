#include <list>
#include <iostream>
#include <algorithm>
#include <iterator>
using namespace std;

void printLists(const list<int>& l1, const list<int>& l2)
{
    cout << "list1: ";
    copy(l1.cbegin(), l1.cend(), ostream_iterator<int>(cout, " "));
    cout << endl << "list2: ";
    copy(l2.cbegin(), l2.cend(), ostream_iterator<int>(cout, " "));
    cout << endl << endl;
}

//int main()
//{
//    list<int> l1, l2;
//    for (int i = 0; i < 6; ++i)
//    {
//        l1.push_back(i);
//        l2.push_front(i);
//    }
//    printLists(l1, l2);
//
//    l2.splice(find(l2.begin(), l2.end(), 3), l1);
//    printLists(l1, l2);
//}
