from result import result
from Lotto import Lotto
from winning_list import Winning_list
from cash import Cash
cash_status = True
earnings = 1000
first_status = True
winning_list = Winning_list()
bonus_status = True
cash = Cash()
while earnings / 1000 >= 1:
    lottoDict = {"three" : 0, "four" : 0, "five" : 0, "bonus" : 0, "six" : 0}
    while first_status == True:
        while cash_status == True:
            cash_status = cash.get_cash()
        first_status = False
    cash.number_of_lottoes = earnings//1000
    winning_list_status = True
    while winning_list_status == True:
        winning_list_status = winning_list.get_winning_list()
    while bonus_status == True:
        bonus_status = winning_list.get_bonus_num()
    for i in range(cash.number_of_lottoes):
        lotto = Lotto()
        lotto.lottery_issue()
        [Three, Four, Five, Bonus, Six] = lotto.compare(winning_list.winning_list, winning_list.bonus_num)
        if Three == 1:
            lottoDict["three"] = lottoDict["three"] + 1
        if Four == 1:
            lottoDict["four"] = lottoDict["four"] + 1
        if Five == 1:
            lottoDict["five"] = lottoDict["five"] + 1
        if Bonus == 1:
            lottoDict["bonus"] = lottoDict["bonus"] + 1
        if Six == 1:
            lottoDict["six"] = lottoDict["six"] + 1
    earnings = result(cash.cash, lottoDict)
