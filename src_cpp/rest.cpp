

#include "rest.h"

random_c random_o = random_c();

random_c::random_c() {
		rng.seed(std::random_device()());
		std::uniform_int_distribution<std::mt19937::result_type> dist6(1, 6);
}

int random_c::randomint(int min, int max) {
		return dist6(rng) % max + min;
}

int averagearray(std::vector<short> &list, int length) {
	int sum = 0;
	for (int i = 0; i < length; i++) {
		sum += list[i];
	}
	return sum / length;
}

auto start_time = std::chrono::system_clock::now();

double getruntime() {
	return round(( std::chrono::system_clock::now() - start_time).count()/1000000)/10;
}

bool boolinarray(bool* boolarray, bool contains, int amountgearpieces) {
	bool temp = false;
	for (int i = 0; i < amountgearpieces; i++) {
		if (boolarray[i] == contains) {
			temp = true;
		}
	}
	return temp;
}