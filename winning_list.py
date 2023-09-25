from repitation import repetition
from repitation import repetition_bonus
class Winning_list:
    def __init__(self):
        self.winning_list = []
        self.bonus_num = 0
    def get_winning_list(self):
        self.winning_list = list(map(int, input("당첨 번호를 입력해주세요.(쉼표 기준)\n").split(",")))
        if repetition(self.winning_list) == True:
            print("[ERROR] 중복된 당첨 번호가 있습니다. 다시 입력하세요. ")
        else:
            return False
    def get_bonus_num(self):
        self.bonus_num = int(input("보너스 번호를 입력해주세요.\n"))
        if repetition_bonus(self.winning_list, self.bonus_num) == True:
            print("[ERROR] 보너스 번호가 당첨 번호 중 하나와 중복되였습니다. 다시 입력하세요. ")
        else:
            return False

