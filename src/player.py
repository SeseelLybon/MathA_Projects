
from charter import Chart as charter_chart

class Player:
    def __init__(self, name):
        self.chart = charter_chart()
        self.name = name