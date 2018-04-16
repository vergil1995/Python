################################### Problem 1
# s = input("Press String here: ")
# # Problem1: dem nguyen am
# numberOfVowels = 0
# for num in s:
#     if num =="a" or num == "e" or num == "i" or num == "o" or num == "u" :
#         numberOfVowels += 1
# print("Number of vowels:", numberOfVowels)

################################### Problem 2: Dem chuoi bob
# numberTimesBob = 0
# num = 0

# while num < len(s):
#     temp = ""
#     temp += s[num:num+3]
#     if temp == "bob":
#         numberTimesBob+=1
#     num+=1
# print("Number of times bob occurs is:", numberTimesBob)

################################### Problem 3: Tim chuoi theo thu tu dai nhat
s= "oyubonaenn"
temp = ""
subString = ""
lenTemp = 0
lenCmp = 0
beforeLetter = 96
s+=chr(96)
for num in s:
    if ord(num) >= beforeLetter:
        temp+=num
        beforeLetter = ord(num)
        
    else:
        beforeLetter = ord(num)
        lenCmp = len(temp)
        if(lenCmp > lenTemp):
            lenTemp = lenCmp
            subString = temp
        temp = num
print(subString)