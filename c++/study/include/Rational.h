#ifndef RATIONAL_H
#define RATIONAL_H


class Rational
{
    public:
        Rational(int numerator, int denominator):m_numerator(numerator), m_denominator(denominator){};
        virtual ~Rational(){};
        operator double(){return double(m_numerator) / m_denominator;}
    protected:
    private:
        int m_numerator;
        int m_denominator;
};

#endif // RATIONAL_H
