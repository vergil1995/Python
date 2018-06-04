# def balanceAfter1Year(balance, annualInterestRate, monthlyPaymentRate):
#     resultValue = balanceAfterMonth(12, balance, annualInterestRate, monthlyPaymentRate)
#     return resultValue

# def balanceAfterMonth(month, balance, annualInterestRate, monthlyPaymentRate):   
#     '''
#     Input: 
#         month - so thang can tinh gia tri
#         balance - so $ con lai phai tra
#         annualInterestRate - Lai suat hang nam
#         monthlyPaymentRate - Lai suat hang thang
#     Output:
#         balanceAfterMonth - so $ con lai sau thang
#     '''
#     if month == 0:
#         return round(balance, 2)
#     else:
#         minPayment = round(balance*monthlyPaymentRate, 2)
#         unpaidBalance = balance - minPayment
#         interestValue = round((annualInterestRate / 12.0)*unpaidBalance, 2)
#         month -= 1
#         return balanceAfterMonth(month, unpaidBalance + interestValue, annualInterestRate, monthlyPaymentRate)
# # # Prob1:
# # print("Remaining balance: ",balanceAfter1Year(484, 0.2, 0.04))

################################## PROB 2 ###################################################
# def lowestPayment2(balance, annualInterestRate):
#     minPayment = 10
#     monthlyInterest = annualInterestRate / 12.0
#     #  (balance - minPayment) > 0
#     while 1:
#         count = 0
#         while count<12: 
#             if count == 0:
#                 perblance = balance
#             unpaidBalance = perblance - minPayment
#             interestValue = monthlyInterest*unpaidBalance
#             perblance = unpaidBalance + interestValue
#             count+=1
#         if perblance <= 0:
#             break
#         else:
#             minPayment += 10
#     return minPayment

# print("Lowest Payment:", lowestPayment2(4779, 0.2))

################################## PROB 3 ###################################################
def lowestPayment(balance, annualInterestRate):  
    monthlyInterest = annualInterestRate / 12.0
    high = (balance * (1+monthlyInterest)**12) / 12.0
    low = balance/12
    minPayment = (high + low) / 2.0
    perblance = 100
    while perblance != 0.0:
        count = 0
        while count < 12: 
            if count == 0:
                perblance = balance
            unpaidBalance = perblance - minPayment
            interestValue = monthlyInterest*unpaidBalance
            perblance = unpaidBalance + interestValue
            count+=1
        if perblance > 0:
            low = minPayment
        else:
            high = minPayment
        minPayment = (high + low) / 2.0 
        perblance = round(perblance, 2)
    return round(minPayment,2)

print("Lowest Payment:", lowestPayment(320000, 0.2))
