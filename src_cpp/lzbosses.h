#pragma once

#include "rest.h"
#include <iostream>
#include <vector>


class LZBosses {
	public:
		LZBosses(int ma_tri);
		std::vector<short> event(std::vector<short> &all_tries);
	private:
		int max_tries;

};