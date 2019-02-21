#pragma once

#include "rest.h"
#include <iostream>
#include <vector>

constexpr int amountgearpieces = (6*14);

class LZBosses {
	public:
		LZBosses(int ma_tri);
		std::vector<int> event(std::vector<int> &all_tries);
	private:
		int max_tries;
		bool boolinarray(bool* boolarray, bool contains = true);

};