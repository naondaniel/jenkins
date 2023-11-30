# import datetime
#
# file = open("Exercise.py")
#
# print(file.read(4))
# a = datetime.datetime.now()
# print(a)
#

# try:
#     "no" + 5
# except BaseException as e:
#     print(e.args)
# finally:
#     print("This will be excuted!")
#
# try:
#     myfile = open("read_my_content.txt", 'r')
#     extracontents = myfile.write("\nsome more text\n")
# except BaseException as e:
#     print("Oops something when wrong.\nError is: " + str(e.args[0]))
# finally:
#     print("Closing file descriptor")
# myfile.close()
#
#
#

def myname(a):
	print("Hello, my name is:")

@myname
def fun():
	print("daniel")
