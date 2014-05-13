/*
 * array2D.cpp
 *
 *  Created on: 2014Äê5ÔÂ12ÈÕ
 *      Author: Administrator
 */

template<class T>
class Array2D {
public:
	class Array1D {
	public:
		T& operator [](int index);
		const T& operator[](int index) const;
	};
	Array1D operator[](int index);
	const Array1D operator[](int index) const;
};


