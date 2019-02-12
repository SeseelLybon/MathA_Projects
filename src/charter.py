

class Chart:
    def __inti__(self):
        self.ones = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixes = 0

        self.three_total = 0
        self.fours_total = 0
        self.full_house = 0
        self.short_straight = 0
        self.long_straight = 0
        self.yatzee = 0
        self.chance = 0

    def sum_top(self):
        top_sum = self.ones + self.twos + self.threes +\
                  self.fours + self.fives + self.sixes
        if top_sum > 63:
            top_sum += 35
        return top_sum

    def sum_bottom(self):
        return self.three_total + self.fours_total + self.full_house +\
               self.short_straight + self.long_straight + self.yatzee + self.chance