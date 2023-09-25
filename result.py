def result(cash, lottoDict):
    print("3개 일치 (5,000원) - {0}개".format(lottoDict["three"]))
    print("4개 일치 (50,000원) - {0}개".format(lottoDict["four"]))
    print("5개 일치 (1,500,000원) - {0}개".format(lottoDict["five"]))
    print("5개 일치, 보너스 볼 일치 (30,000,000원) - {0}개".format(lottoDict["bonus"]))
    print("6개 일치 (2,000,000,000원) - {0}개".format(lottoDict["six"]))
    earnings = (lottoDict["three"] * 5000) + (lottoDict["four"] * 50000) + (lottoDict["five"] * 1500000) + \
               (lottoDict["bonus"] * 30000000) + (lottoDict["six"] * 2000000000)

    print("총 수익률은 {0}%입니다.".format(round(earnings / cash * 100, 1)))
    print("수익 : {0}".format(earnings))
    return earnings