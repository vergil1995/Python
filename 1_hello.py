################################### BRANCH
####### IF - ELSE
# print("Hello World")
# x = int (input('Enter an interger :'))
# y = int (input('Enter an interger :'))
# z = int (input('Enter an interger :'))
# if x<y and x<z :
#     print('x is least')
# elif y<z:
#     print('y is least')
# #elif z<x and z<y:
# else:
#     print('z is least')
# print('Done with conditional')
####### WHILE
# n = 0
# while n < 5:        # print 0 to 4
#     print(n)
#     n+=1

####### FOR
## range(start,stop,step)
# for n in range(5):      # print 0 to 4  
#     print(n)
# for n1 in range(1,10):    # print 1 to 9
#     print(n1)
# for n2 in range(1,10,2):    # print 1 3 5 7 9
#     print(n2)
# for m in ["saber", "archer", "lancer", "ruler"]:    # print all in array
#     print(m)

# print("Hello!")
# for num in range(11,1,-1):    # print 10 8 6 4 2 
#     if num%2 == 0:
#         print(num)
# s = "abcdef"
# # C1: 
# for n in s:
#     print(n)        # a,b,c,d,e,f
# # C2:
# for n in range(len(s)):
#     print(s[n])
    
####### DO-WHILE
############### STRING
# a = "HelloWorld"
# b = a[1:3]
# c = a[-1]
# d = a[::-1]
# e = a[1::2]
# f = 16101995
# g = "hello"
# g = "y" + g[1:]
# print(g)            #yello
# f_str = str(f)
# print(a)    # HelloWorld
# print(b)    # el
# print(c)    # d
# print(d)    # dlroWolleH
# print(e)    # elWrd
# print("F in INT", f)            # F in INT 16101995
# print("F in String" + f_str)    # F in String16101995 + only String
# print("F in String", f_str)     # F in String 16101995
# print("F in INT", f, ".", "F in String", f_str) # F in INT 16101995 . F in String 16101995
# varA = "a"
# varB = "b"
# if type(varA) is str or type(varB) is str:
#     print("string involved")
# elif varA > varB:
#     print("bigger")
# elif varA == varB:
#     print("equal")
# else:
#     print("smaller")
################### EXAMPLE ####################
# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0

# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print(char)
#     else:
#         numCons -= 1

# print('numVowels is: ' + str(numVowels))
# print('numCons is: ' + str(numCons)) 
############################################################
################################### Convert Ansi to int Decimal
# number = ord("a")
# print(number)
# charr = chr(number)
# print(charr)    
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))