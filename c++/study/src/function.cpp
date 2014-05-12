#include <functional>
#include <iostream>
using namespace std;

class C{
public:
    void memfunc (int x, int y)
    {
        cout << x + y << endl;
    }
};

//int main()
//{
//    function<void(C, int, int)> mf;
//    mf = &C::memfunc;
//    mf(C(), 42, 77);
//}
