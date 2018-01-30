import random
import time
from handle_data import *


class Prize:

    def __init__(self, log):
        self.source_arr = get_data(EXCEL_NAME)
        self.prize_people = get_data(EXCEL_NAME, 1)
        self.prize = None
        self.arr = [[], []]
        self.log = log

    def random_arr(self, count=1):
        if count < 1:
            return

        for i in range(0, count):
            self.log("打乱中。。。\n")
            time.sleep(1)
            random.shuffle(self.source_arr)

    def start(self):
        # count = random.randint(1, 10)
        count = 1
        self.random_arr(count)

    def stop(self):
        self.prize = self.source_arr.pop()
        return self.prize

    def save(self):
        self.prize_people.append(self.prize)

        self.arr[0] = self.source_arr
        self.arr[1] = self.prize_people

        save_data(self.arr)

    def show_prize(self):
        if not self.prize_people:
            return

        arr_len = len(self.prize_people)
        if arr_len < 1:
            return

        for i in range(0, arr_len):
            if 0 <= i < 8:
                print("幸运奖\t", self.prize_people[i])
            elif 8 <= i < 12:
                print("三等奖\t", self.prize_people[i])
            elif 12 <= i < 14:
                print("二等奖\t", self.prize_people[i])
            elif 14 == i:
                print("一等奖\t", self.prize_people[i])

        print()


if __name__ == '__main__':
    for i in range(0, 15):
        prize_app = Prize()
        prize_app.start()
        prize_app.show_prize()
