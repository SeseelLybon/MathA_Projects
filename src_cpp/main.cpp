
#include "lzbosses.h"
#include <iostream>
#include "rest.h"
#include <vector>
#include <algorithm>

constexpr int max_tries = (10E5);


void format_results();


std::vector<short> all_tries(max_tries);

int main()
{
	std::cout << "Hello World!" << std::endl;
	LZBosses LZB(max_tries);
	std::cout << "Starting event\n";
	LZB.event(all_tries);
	std::cout << "Event is done!" << std::endl;
	format_results();
	return 0;
}

void format_results() {
	/* Prints out every individual try
	for (int i = 0; i < max_tries; i++) {
		std::cout << tries[i] << std::endl;
	}
	*/
	std::cout << "Average: " << averagearray(all_tries, max_tries) << std::endl;

	auto minimum = *std::min_element(all_tries.begin(), all_tries.end());
	std::cout << "Minimum: " << minimum << std::endl;

	auto maximum = *std::max_element(all_tries.begin(), all_tries.end());
	std::cout << "Maximum: " << maximum << std::endl;

	std::sort(all_tries.begin(), all_tries.end());
	auto mean = all_tries[int(max_tries/2)];
	std::cout << "Mean: " << mean << std::endl;

	std::cout << "Done" << std::endl;
}