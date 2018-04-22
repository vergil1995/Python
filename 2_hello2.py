################################### Bisection Search
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

################################### Mini Game Bisection Search
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

################################### Convert int 10 to 2
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

################################### Convert int 10 to 2
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

################################### Newton-Raphson
# Khi co guess g, co the tim dc gia tri tot hon nua
# g - p(g)/p'(g)
# g - guess
# p(g) = g^2 - y
# epsilon = 0.01
# y = 24.0
# guess = y/2.0
# numGuesses = 0

# while abs(guess*guess - y) >= epsilon:
#     numGuesses += 1
#     guess = guess - (((guess**2) - y)/(2*guess)) # Newton-Raphson
# print("numGuesses = " + str(numGuesses))
# print("Square root of " + str(y) + " is about " + str(guess))

################################### Function
# def test_funtion(i):
#     """ 
#     (Assumptions) Input: i, a positive int
#     (Guarantees) Return: True if i is even. Otherwise return False
#     """
#     print(i)
#     return i%2==0
    
# a = test_funtion(10)
# print(a)

# # Ex 1:
# def f(y):
#     x = 1
#     x += 1
#     print(x)        # 2

# x = 5
# f(x)
# print(x)            # 5

# # Ex 2: Khong thay x trong g-scope se tim x o parent scope, only look up
# def g(y):
#     print(x)            # 5
#     print(x+1)          # 6

# x = 5
# g(x)
# print(x)                # 5

# # Ex 3: Fail khi tinh toan lam thay doi x ma ko co x trong h-scope
# def h(y):
#     x = x+1
# x = 5
# h(x)
# print(x)

# # Ex 4:
# def g(x):
#     def h():
#         print("in h(): x =",x)     # 4

#     x = x+1
#     print("in g(x): x =", x)       # 4
#     h()
#     return x

# x = 3
# z = g(x)
# print("in global: x =", x)     # 3

### Ex 5: Khi tinh toan voi x nhung ko lam thay doi x
# # 5.1
# a = 10
# def f(x):
#     return x + a        # 4
# a = 3
# f(1)

### 5.2
# x = 12
# def g(x):                   # x is here
#     x = x + 1               # x trong g-scope = 13
#     def h(y):
#         return x + y        # 19
#     return h(6)
# g(x)

### Ex 6:
# def printName(firstName, lastName, reverse = False):
#     if reverse:
#         print(firstName + ', ' + lastName)
#     else:
#         print(firstName, lastName)

# printName("Altair", "Vergil")           # Altair Vergil
# ## Altair2, Vergil2: muon gan thi phai tu doi so tu duoi len
# # printName(firstName = "Altair2", "Vergil2", True)   # Fail
# # printName(firstName = "Altair2", "Vergil2", reverse = True)     # Fail
# printName("Altair2", "Vergil2", reverse = True)
# printName("Altair2", lastName = "Vergil2", reverse = True)
# printName(firstName = "Altair2", lastName = "Vergil2", reverse = True)
##################### Lặp và Đệ qui
# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
 
#     returns: int or float, base^exp
#     '''
#     # Your code here
#     result = 1
#     for k in range(1, exp + 1):
#         result *= base
#     return result

# print(iterPower(2,3))

# def recurPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
 
#     returns: int or float, base^exp
#     '''
#     # Your code here
#     if exp==0 :
#         return 1
#     else:
#         return base*recurPower(base, exp - 1)

# print(recurPower(2,3))

##################### Tower of HaNoi
# def printMove(fr, to):
#     print('move from ' + str(fr) + " to " + str(to))
# def Towers(n, fr, to, spare):
#     if n==1:
#         printMove(fr, to)
#     else:
#         Towers(n-1, fr, spare, to)
#         Towers(1, fr, to, spare)
#         Towers(n-1, spare, to, fr)

# print(Towers(4,"P1", "P2", "P3"))

##################### Tim Uoc chung nho nhat
# ## Dung lap Iteration
# def gcdIter(a, b):
#     '''
#     a, b: positive integers
    
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     # Your code here
#     minNum = 0
#     result = 0
#     if a < b:
#         minNum = a
#     else:
#         minNum = b

#     while minNum > 0:
#         if (a % minNum == 0) and (b % minNum == 0):
#             result = minNum
#             break
#         minNum -= 1
#     return result

# print(gcdIter(6,102))

# ## Dung Recursion
# def gcdRecur(a, b):
#     '''
#     a, b: positive integers
    
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     # Your code here
#     if b == 0:
#         return a
#     else:
#         return gcdRecur(b, a%b)
    
# print(gcdRecur(6,102))

## Fibonacci
def fib(x):
    """
    assumes x an int >= 0
    return Fibonacci of x (ex: month rabbit)
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)