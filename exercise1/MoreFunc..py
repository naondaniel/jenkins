# #1
# numbers = [
#     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#     743, 527
# ]
#
# list1 = []
# for i in numbers:
#     if i == 237:
#         break
#     if i % 2 == 0:
#         # print(i)
#         list1.append(i)
# print(list1)
#
# list2 = []
# for number in numbers:
#     if number == 237:
#         break
#     if number % 2 == 0:
#         # print(number)
#         list2.append(number)
# print(list2)

#2

# Write a function that takes in a numerical value, and returns
#  the word corresponding to that number.
# The program will handle numbers: 0 - 4, for other numbers it will
# return that the input is incorrect.

# def numerical(num):
#     if num == 1:
#         return "one"
#     elif num == 2:
#         return "two"
#     elif num == 3:
#         return "three"
#     elif num == 4:
#         return "four"
#     else:
#         print("wrong number, please try again.")
#         numerical(int(input("please enter a number in between 1-4:")))
#
# x=numerical(int(input("please enter a number in between 1-4:")))
# print(x)


#3
# Write a program that receives a list of strings and it will return the amount of variables in that list.
#
list1 = ["Eve", "Alice", "Bob"]
# count = 0
# for i in list1:
#     if i is not str:
#         ""
#     else:
#         count += 1
#     print(count)
#

# result = 0
# for i in list1:
#     if i is not str:
#         break
#     result += 1
#     print(result)


#4
# Write a function that receives a dictionary and it will validate if the dictionary is in the following format:
# {‘name’: String, ‘age’: Number, ‘Hobbies’: List}

def valid(dict):
    if type(dict["name"]) == str:
        print("valid name key")
    else:
        print("missing valid name key")
    if type(dict["age"]) == int:
        print("valid age key")
    else:
        print("missing valid age key")
    if type(dict["hobbies"]) == list:
        print("valid hobbies key")
    else:
        print("missing valid hobbies key")

valid({"name": 13, "age": 22, "hobbies": ["football", "TV"]})
