# #1
#
# x = "python course"
# y = 3.0
# a = x[:6] + str(y) +x[7:]
# print(a)
#
# #2
# space = x.find(" ")
# a2 = x[:space]+" " + str(y) +" "+ x[space+1:]
# print(a2)
#
# #3
# a = 14.55673
# x = str(a)
# point = x.find('.')
# final = x[:point+3]
# print(final)
#
# #4
# x= "abcdefghigkl"
# if ((x[7] == 'd' and x[8] == 'e') or (x[7] =='h' and x[8] == 'i')):
#     print("Version A")
# else:
#   print("Version B")
#
# #5
# x = "python course"
# space1 = x.find(" ")
# final_result = x[space1+1:] +" " + x[:space1]
# print(final_result)
#
# num=1
# print(f"My Number Is: {num}")
#
# #6
# list = [1,2,3,4,5]
# counter = 0
#
# for i in range(1001):
#     counter+=i
# print(counter)
#
# #7
# p = [1,2,3,"dani",4,5]
# for q in p:
#     if type(q) == str:
#         continue
#     print(q)

#8

x= "aaabcdiaaart"
counter = 0

# for i in x:
#     if i == 'a':
#         counter=counter+1
# print(counter)
# i=0
# while i < len(x):
#     if x[i] == 'a':
#         counter+=1
#     i+=1
# print(counter)

#9
# x = int(input("please enter your age"))
# while x< 18:
#     x = int(input("please enter your age"))

#10
def fun_example(x):
    if x < 100:
        print(True)
    elif x > 100:
        print(False)

fun_example(int(input("please enter a number:")))