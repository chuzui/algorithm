#include "algostuff.hpp"
using namespace std;

class MeanValue{
private:
    long num;
    long sum;
public:
    MeanValue(): num(0), sum(0){}

    void operator() (int elem){
        ++num;
        sum += elem;
    }

    operator double(){
        return static_cast<double>(sum) / static_cast<double>(num);
    }
};
//
//int main()
//{
//    vector<int> l1;
//    INSERT_ELEMENTS(l1, 1, 8);
//    double mv = for_each(l1.begin(), l1.end(), MeanValue());
//    cout << mv << endl;
//}
