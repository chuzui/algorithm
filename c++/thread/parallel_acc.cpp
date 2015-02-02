#include <iostream>
#include <algorithm>
#include <thread>
#include <numeric>
#include <vector>
#include <time.h>
using namespace std;

template<typename Iterator, typename T>
struct accmulate_block
{
	void operator()(Iterator first, Iterator last, T& result)
	{
		result = accumulate(first, last, result);
	}
};

template<typename Iterator, typename T>
T parallel_accumulate(Iterator first, Iterator last, T init)
{
	unsigned long const length = distance(first, last);
	if (!length)
		return init;

	unsigned long const num_threads = thread::hardware_concurrency();
	unsigned long const block_size = length / num_threads;

	vector<T> results(num_threads);
	vector<thread> threads(num_threads);

	Iterator block_start = first;
	for (unsigned long i = 0; i < num_threads; ++i)
	{
		Iterator block_end = block_start;
		advance(block_end, block_size);
		threads[i] = thread(accmulate_block<Iterator, T>(), block_start, block_end, ref(results[i]));
		block_start = block_end;
	}

	for_each(threads.begin(), threads.end(), mem_fn(&thread::join));
	return accumulate(results.begin(), results.end(), init);

}

int tmain1()
{
	vector<char> a(1000000000, 1);
	clock_t t1 = clock();
	cout << parallel_accumulate(a.begin(), a.end(), 0);
	clock_t t2 = clock();
	cout << t2 - t1 << endl;

	clock_t t3 = clock();
	cout << accumulate(a.begin(), a.end(), 0);
	clock_t t4 = clock();
	cout << t4 - t3 << endl;

	int i;
	cin >> i;
	return 0;
}