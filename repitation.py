def repetition (winning_list):
    for i in range(6):
        for j in range(i):
            if winning_list[j] == winning_list[i]:
                return True
    return False
def repetition_bonus (winning_list, bonus_num):
    for i in range(6):
        if bonus_num == winning_list[i]:
            return True
    return False