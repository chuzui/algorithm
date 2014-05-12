#include <utility>
#include <iostream>
#include <tuple>
#include <string>
#include <complex>
#include <functional>
using namespace std;

template <typename... Args>
ostream& operator << (ostream& strm, const tuple<Args...>& t)
{
    return strm << "[]";
}

//int main1()
//{
//    // create a four-element tuple
//    // - elements are initialized with default value (0 for fundamental types)
//    tuple<string,int,int,complex<double>> t;
//    // create and initialize a tuple explicitly
//    tuple<int,float,string> t1(41,6.3,"nico");
//    // ¡®¡®iterate¡¯¡¯ over elements:
//    cout << get<0>(t1) << " ";
//    cout << get<1>(t1) << " ";
//    cout << get<2>(t1) << " ";
//    cout << endl;
//    // create tuple with make_tuple()
//    // - auto declares t2 with type of right-hand side
//    // - thus, type of t2 is tuple
//    auto t2 = make_tuple(22,44,"nico");
//    // assign second value in t2 to t1
//    get<1>(t1) = get<1>(t2);
//    // comparison and assignment
//    // - including type conversion from tuple<int,int,const char*>
//    // to tuple<int,float,string>
//    if (t1 < t2)   // compares value for value
//    {
//        t1 = t2; // OK, assigns value for value
//    }
//
//    string s;
//    auto x = make_tuple(s);
//    get<0>(x) = "my value";
//    cout << s;
//
//    //auto y = make_tuple(ref(s));
//    //get<0>(y) = "12345" << endl;
//    //cout << s;
//
//    typename std::tuple<int, float, string> TupleType;
//    cout << tuple_size<decltype(TupleType)>::value << endl;
//    //cout << tuple_element<3,TupleType>::type << endl
//    return 0;
//}
