import re
# #A
#
# def compare(x: int, y: int):
#     if x > y:
#         print("Bigger")
#     else:
#         print("Smaller")
#
# compare(14, 15)
# compare(17, 15)
#
# # #B
# #
# # for i in range(1, 6):
# #     print(i)
# #
# # #C
# #
# # x = input("please enter a number:")
# # if x == 1:
# #     print("Summer")
# # elif x == 2:
# #     print("Winter")
# # elif x == 3:
# #     print("Fall")
# # else:
# #     print("Spring")
# #
# # #D
# # count = 1
# # while count < 11:
# #     print(count)
# #     count = count + 1
# # #10 times, print 10.
# #
# # #E
# # def sum(age ,letter, currency, abroad, apt):
# #     print(f"{age} {letter} {currency} {abroad} {apt}")
# #     x = currency + age
# #     print(f"{x}")
# #
# # sum(27, "N", 5, True, 4)
# #
# # #F
# #
# # def phone():
# #     x = str(input("what is your phone number:"))
# #     print(f"Phone number: {x}")
# #
# # phone()
# #
# # #G
# #
# # def printHello():
# #     print("Hello")
# #
# # def calculate():
# #     result = 5+3.2
# #     print(result)
# #
# # printHello()
# # calculate()
# #
# # #H
# # def yourName(name):
# #     print(name)
# #
# # def number(num):
# #     x = num / 2
# #     print(x)
# #
# # yourName(input("please enter your name:"))
# # number(12)
#
# #I
#
# def num1(x:int, y:int):
#     return x + y
#
# def num2(x: str, y:str):
#    result = x + " " + y
#    space = result.find(" ")
#    newResult = result[:space] + result[space +1:]
#    print(newResult)
#
# p = num1(4, 6)
# print(p)
# num2("daniel", "naon")

#challenge1
#
# for i in range(5):
#     for y in range(i + 1):
#         print("* ", end="")
#     print("\n")
#
#
# #challenge2
#
# for row in range(9):
#     for column in range(9):
#         if (row == column or row + column ==  9 - 1):
#             print("* ", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# #M
#
# def getsNum(x):
#     receiveNum(x)
#
# def receiveNum(x):
#     sum = 0
#     for i in str(x):
#         sum = sum + int(i)
#     print(sum)
#
# getsNum(int(input("please enter a number:")))

#PythonTasks

#1
# def is_palindrome(name):
#     nameLower = name.lower()
#     if nameLower == nameLower[::-1]:
#         print("True, is_palindrome is the function name")
# is_palindrome("racecar")

#2
with open("file.txt", "r") as file:
    # content = file.read()
    # print(content)

    #Number of lines
    # lines = file.readlines()
    # line_count = len(lines)
    # print(lines)

    content = file.read()
    print(content)
    num_lines = len(content.splitlines())
    print(num_lines)

    #Number of words
    list_of_words = content.split()
    num_of_words = len(list_of_words)
    print(num_of_words)

    #Number of character
    print(len(content))
    num_of_char = 0
    for i in content:
        if i == ' ':
            ''
        else:
            num_of_char+=1
    print(num_of_char)

print(f"Number of lines: {num_lines}, number of words: {num_of_words}, number of characters: {num_of_char}")

#3
#
# def pass_criteria(password):
#     count = 0
#     if len(password) >= 8: #checks the length of the string
#         count += 1
#     if password.isalpha(): #checks if the string has letters
#         count += 1
#     if password.isdigit(): #check if the string has digits
#         count += 1
#     return count
#
# def pass_criteria2(password):
#     count = 0
#     if re.search("[^a-zA-Z0-9s]", password):
#         print("String contains special character(s).")
#         count +=1
#     else:
#         print("String does not contain special character(s).")
#     if not password.islower() and not password.isupper():
#         count += 1
#         print("Mixed Cases")
#     return count
#
# word = input("Please enter a password:")
# count1 = pass_criteria(word)
# count2 = pass_criteria2(word)
#
# def calculation(count1, count2):
#     print(count1, count2)
#     sum = count1 + count2
#     if sum < 3:
#         print("You password is weak, please try again.")
#     elif sum >=3 and sum < 5:
#         print("Your password is Medium.")
#     else:
#         print("Your password is strong.")
#
# calculation(count1, count2)