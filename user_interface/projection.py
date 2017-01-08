import sys
import os
sys.path.insert(0, os.path.abspath('../'))
from settings import general_settings

class Projection:
    def __init__(self, proj_id, movie_id, movie_type, m_date, m_time):
        self.proj_id = proj_id
        self.movie_id = movie_id
        self.type = movie_type
        self.date = m_date
        self.time = m_time
        self.seats = [["." for x in range(10)] for x in range(10)]

    def __str__(self):
        return "{0} {1} ({2}) - {3} spots available".format(self.date, self.time, self.type, self.available_seats())

    def available_seats(self):
        count = 0
        for row in self.seats:
            for seat in row:
                if seat == ".":
                    count += 1
        return count

    def print_seats(self):
        res = "   "
        for x in range(1, 11):
            res += str(x)
            res += " "
        curr_row = 1
        for row in self.seats:
            res += "\n{0:2} ".format(curr_row)
            for seat in row:
                res += seat
                res += " "
            curr_row += 1
        print(res)

    def reserve_seat(self, coordinates):
        self.seats[coordinates[0] - 1][coordinates[1] - 1] = 'X'

    def try_reserve_seat(self, coordinates):
        if coordinates[0] > 10 or coordinates[0] < 0 or coordinates[1] > 10 or coordinates[1] < 0:
            print(general_settings.SEAT_OUT_OF_RANGE)
            return False
        elif self.seats[coordinates[0] - 1][coordinates[1] - 1] == "X":
            print(general_settings.TAKEN_SEAT)
            return False
        self.reserve_seat(coordinates)
        return True








