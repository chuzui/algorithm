#include <iostream>
#include <list>
#include <algorithm>
#include <future>

template<typename T>
std::list<T> se_quick_sort(std::list<T> input)
{
	if (input.empty())
		return input;

	std::list<T> re;
	re.splice(re.begin(), input, input.begin());
	T const& pivot = *re.begin();

	auto divide_point = std::partition(input.begin(), input.end(),
		[&](T const& t){return t < pivot; });

	std::list<T> lower_part;
	lower_part.splice(lower_part.end(), input, input.begin(), divide_point);

	auto new_lower(se_quick_sort(std::move(lower_part)));
	auto new_higher(se_quick_sort(std::move(input)));

	re.splice(re.end(), new_higher);
	re.splice(re.begin(), new_lower);
	return re;
}

template<typename T>
std::list<T> parallel_quick_sort(std::list<T> input)
{
    if (input.empty())
        return input;

    std::list<T> re;
    re.splice(re.begin(), input, input.begin());
    T const& pivot = *re.begin();

    auto divide_point = std::partition(input.begin(), input.end(), [&](T const& t){return t<pivot;});

    std::list<T> lower_part;
    lower_part.splice(lower_part.end(), input, input.begin(), divide_point);

    std::future<std::list<T> > new_lower(std::async(&parallel_quick_sort<T>, std::move(lower_part)));

    auto new_higher(parallel_quick_sort(std::move(input)));

    re.splice(re.end(), new_higher);
    re.splice(re.begin(), new_lower.get());
    return re;
}

int main()
{
	std::list<int> a{ 6, 2, 4, 6, 8, 1, 2, 9, 4, 3, 2, 1 };
	auto b = parallel_quick_sort(a);
	for (auto& x : b)
		std::cout << x << " ";
	int x;
	std::cin >> x;
	return 0;
}