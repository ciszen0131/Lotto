class Cash:
    def __init__(self):
        self.cash = 0
        self.number_of_lottoes = 0
    def get_cash(self):
        self.cash = int(input("로또 구입 금액을 입력하세요. (1000원당 1장)\n"))
        if self.cash % 1000 == 0:
            self.number_of_lottoes = self.cash // 1000
            print("{0}개를 구매했습니다.".format(self.number_of_lottoes))
            return False
        else:
            print("[ERROR] 잘못된 금액입니다. 다시 입력하세요.")