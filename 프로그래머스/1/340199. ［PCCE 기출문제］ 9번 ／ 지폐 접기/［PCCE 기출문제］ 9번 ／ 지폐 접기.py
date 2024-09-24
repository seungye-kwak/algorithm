def solution(wallet, bill):
    answer = 0
    wallet_x, wallet_y = wallet
    bill_x, bill_y = bill
    while True:
        if (bill_x <= wallet_x and bill_y <= wallet_y) or (bill_x <= wallet_y and bill_y <= wallet_x) :
            break
        else :
            bill_x, bill_y = max([bill_x, bill_y])//2, min([bill_x, bill_y])
            answer += 1
    return answer