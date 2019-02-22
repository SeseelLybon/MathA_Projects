
#include "lzbosses.h"

constexpr int amountgearpieces = (6 * 14);

LZBosses::LZBosses(int ma_tri) {
	max_tries = ma_tri;
}

std::vector<short> LZBosses::event(std::vector<short> &all_tries) {

//	random_c random_o = random_c();
	for (int x = 0; x < max_tries; x++) {
		all_tries[x] = 0;
	}



	int roll;
	bool gearpieces[amountgearpieces];
	bool notdone;

	for (int i = 0; i < max_tries; i++) {
		if (i % 10000 == 0) {
			std::cout << "At step " << i << " @ " << getruntime() << std::endl;
		}

		notdone = true;

		// Set all gearpieces to false
		for (int x = 0; x < amountgearpieces; x++) {
			gearpieces[x] = false;
		}

		int tries = 0;
		while (notdone) {
			tries += 1;
			if (random_o.randomint(1, 6) == 1) {
				roll = random_o.randomint(1, amountgearpieces) - 1;

				gearpieces[roll] = true;
			}

			if (boolinarray(gearpieces, false, amountgearpieces) == false) {
				notdone = false;
			}
		}
		all_tries[i] = tries;
	}
	return all_tries;
}