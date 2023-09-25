import random
class Lotto:
    def __init__(self):
        self.lotto = []
    def lottery_issue(self):
        for i in range(6):
            numlock = True
            while numlock == True:
                num = random.randrange(1, 46)
                if i == 0:
                    numlock = False
                for j in range(i):
                    if num != self.lotto[j]:
                        numlock = False
            self.lotto.append(num)
        return self.lotto
    def compare(self, winning_list, bonus_num):
        temp = 0
        bonus_temp = 0
        for i in range(6):
            for j in range(6):
                if self.lotto[i] == winning_list[j]:
                    temp = temp + 1
            if self.lotto[i] == bonus_num:
                bonus_temp = bonus_temp + 1
        if temp == 3:
            return [1, 0, 0, 0, 0]
        elif temp == 4:
            return [0, 1, 0, 0, 0]
        elif temp == 5 and bonus_temp == 0:
            return [0, 0, 1, 0, 0]
        elif temp == 5 and bonus_temp == 1:
            return [0, 0, 0, 1, 0]
        elif temp == 6:
            return [0, 0, 0, 0, 1]
        else:
            return [0, 0, 0, 0, 0]