#ifndef BST_H
#define BST_H
#include <iostream>

class BST
{
    public:
        BST(int n):m_n(n){};
        virtual ~BST(){};
        friend std::ostream& operator<<(std::ostream& os, const BST& b);
    protected:
    private:
        int m_n;
};

std::ostream& operator<<(std::ostream& os, const BST& b)
{
    os << b.m_n << std::endl;
    return os;
}
#endif // BST_H
