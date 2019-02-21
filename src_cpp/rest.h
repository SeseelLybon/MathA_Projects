#pragma once



#include <random>
#include <vector>
#include <chrono>
#include <math.h>

class random_c {
private:
	std::mt19937 rng;
	std::uniform_int_distribution<std::mt19937::result_type> dist6;

public:
	random_c();
	int randomint(int min = 1, int max = 20);

};

int averagearray(std::vector<int> &list, int length);

double getruntime();