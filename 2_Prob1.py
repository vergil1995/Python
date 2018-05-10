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
    return paymentAfterMonth(12, balance, annualInterestRate)
    
def paymentAfterMonth(month, balance, annualInterestRate):   
    monthInterestRate = annualInterestRate / 12.0
    if month == 0:
        return round(balance*monthInterestRate, 2)
    else:  
        minPayment = round(balance*monthInterestRate, 2)
        unpaidBalance = balance - minPayment
        month -= 1
        return paymentAfterMonth(month, unpaidBalance + (monthInterestRate*unpaidBalance), annualInterestRate)

print("Lowest Payment:", lowestPayment(4773, 0.2))

