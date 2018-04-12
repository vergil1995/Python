# # Bisection Search
# # Tinh can bac 2
# x = 25
# epsilon = 0.01
# numGuesses = 0
# # Both low = 1.0 and low = 0.0 work.
# low = 0.0
# high = x
# ans = (high + low)/2.0

# while abs(ans**2 - x) >= epsilon:
#     print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans 
#     ans = (high + low)/2.0
# print('numGuesses = ' + str(numGuesses))
# print(str(ans) + ' is close to square root of ' + str(x))

## Mini Game Bisection Search
# x = 100
# epsilon = 0.5
# low = 0
# high = x
# ans = (high + low)/2
# print("Please think of a number between 0 and 100!")
# while ans >= epsilon :
#     print("Is your secret number " + str(int(ans)) + "?")
#     inputText = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
#     if inputText == "c":
#         print("Game over. Your secret number was: " + str(int(ans)))
#         break
#     else:
#         # h - neu du doan lon hon think
#         if inputText == "h" :
#             high = int(ans)
#         # l - neu guess < think
#         elif inputText == "l" :
#             low = int(ans)
#         else:
#             print("Sorry, I did not understand your input.")
#         ans = (high + low)/2

# ## Convert int 10 to 2
# num = 19
# if num <0:
#     isNeg = True
#     num = abs(num)
# else:
#     isNeg = False
# result = ''
# if num == 0:
#     result = '0'
# while num > 0:
#     result = str(num % 2) + result
#     num = num//2
# if isNeg:
#     result = '-' + result
# print(result)

# ## Convert int 10 to 2
# # Ex: 0.375 to dec. 
# # 0.375 * 2^3 = 3 is interger
# # 3 -> 0011 (binary)
# # lay 0011 chia cho 2*3 = 0011 dich phai 3 don vi -> 0.011
# x = float(input("Enter a decimal number between 0 and 1: "))
# p = 0
# while ((2**p)*x)%1 != 0:
#     print("Remainder = " + str((2**p)*x - int((2**p)*x)))
#     p+=1
# num = int(x*(2**p))
# result = ""
# if num == 0:
#     result = "0"
# while num > 0:
#     result = str(num%2) + result
#     num = num//2

# for i in range(p - len(result)):
#     result = "0" + result
# result = result[0:-p] + "." + result[-p:]
# print("The binary representation of the decimal " + str(x) + " is " + result)

# Newton-Raphson: Khi co guess g, co the tim dc gia tri tot hon nua
# g - p(g)/p'(g)
# g - guess
# p(g) = g^2 - y
epsilon = 0.01
y = 24.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess)) # Newton-Raphson
print("numGuesses = " + str(numGuesses))
print("Square root of " + str(y) + " is about " + str(guess))