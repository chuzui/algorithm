#include <utility>
#include <iostream>
#include <tuple>
#include "tuple.cpp"
using namespace std;
class Foo
{
public:
    Foo (tuple<int, float>)
    {
        cout << "Foo::Foo(tuple)" << endl;
    }
    template <typename... Args>
    Foo (Args... args)
    {
        cout << "Foo::Foo(args...)" << endl;
    }
};

ostream& operator << (ostream& strm, const Foo& foo)
{
    return strm << "Foo";
}

template <typename T1, typename T2>
ostream& operator << (ostream& strm, const pair<T1,T2>& p)
{
    return strm << "[" << p.first << "," << p.second << "]";
}

//int main()
//{
//    typedef pair<int,float> IntFloatPair;
//    IntFloatPair p(42,3.14);
//    cout << p << "\n";
//    cout << get<0>(p) << "\n"; // yields p.first
//    cout << get<1>(p) << "\n"; // yields p.second
//    cout << tuple_size<IntFloatPair>::value; // yields 2
//    //cout << tuple_element<0,IntFloatPair>::type; // yields int
//
//    tuple<int,float> t(1, 2.22);
//    pair<int,Foo> p1(42, t);
//    pair<int,Foo> p2(piecewise_construct, make_tuple(42), t);
//    cout << p1;
// }
