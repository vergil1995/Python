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
def lowestPayment(balance, annualInterestRate):
    '''
    Input: 
        balance - so $ con lai phai tra
        annualInterestRate - Lai suat hang nam
        monthlyPaymentRate - Lai suat hang thang
    Output:
        balanceAfterMonth - so $ con lai sau thang
    '''
    minPayment = 10
    perblance = 100
    while perblance > 0:
        monthlyInterest = annualInterestRate / 12.0
        count = 0
        perblance = balance
        while count<12: 
            unpaidBalance = perblance - minPayment
            interestValue = monthlyInterest*unpaidBalance
            perblance = unpaidBalance + interestValue
            count+=1
        if perblance <= 0:
            break
        else:
            minPayment += 10
    return minPayment

print("Lowest Payment:", lowestPayment(balance, annualInterestRate))

