
#include "classified.h"

constexpr int amountgearpieces = (6);

Classified::Classified(int ma_tri) {
	max_tries = ma_tri;
}

std::vector<short> Classified::event(std::vector<short> &all_tries) {

	//	random_c random_o = random_c();
	for (int x = 0; x < max_tries; x++) {
		all_tries[x] = 0;
	}

	int roll_s;
	int roll_p;
	bool gearpieces[14][6];
	bool notdone;

	for (int i = 0; i < max_tries; i++) {
		if (i % 10000 == 0) {
			std::cout << "At step " << i << " @ " << getruntime() << std::endl;
		}

		notdone = true;

		// Set all gearpieces to false
		for (int s = 0; s < 14; s++) {
			for(int p = 0; p < 6; p++) {
				gearpieces[s][p] = false;
			}
		}

		int tries = 0;
		while (notdone) {
			tries += 1;
			roll_s = random_o.randomint(1, 14) - 1;
			roll_p = random_o.randomint(1, 6) - 1;

			gearpieces[roll_s][roll_p] = true;

			bool temp = false;
			for (int s = 0; s < 6; s++) {
				if(boolinarray(gearpieces[s], false, 6) == true) {
					temp = true;
				}
			}
			notdone = temp;
		}
		all_tries[i] = tries;
	}
	return all_tries;
}