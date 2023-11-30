#A
def compare(x: int, y: int):
    if x > y:
        print("Bigger")
    else:
        print("Smaller")

compare(14, 13)
compare(1, 12)

#B
for i in range(1, 6):
    print(i)

#C
x = int(input("Please enter a number between 1-4:"))

if x == 1:
    print("Summer")
elif x ==2:
    print("Winter")
elif x ==3:
    print("fall")
elif x== 4:
    print("Spring")
else:
    print("Not between 1-4...")

#D
# Answer: It will print till 10, because 11 < 11 will stop the loop

#E
age = 27
currency = 3.81
abroad = True
apt = 4
print(f"{age} {currency} {abroad} {apt}")
print(age + currency)

#F
x = input("Enter your number:")
print(f"Phone number: {x}")

#G
def printHelllo():
    print("hello world")

def calculate():
    print(5+3.2)

printHelllo()
calculate()

#H
def printName(name: str):
    print(name)

def printNum(num):
    print(num / 2 )

printName("Dani")
printNum(14)

#I
def number(x: int, y: int) -> int:
   return x + y

def words(x: str, y: str) -> str:
    return f"{x} {y}"

print(number(1, 3))
print(words("coco", "momo"))

#Challenge1


for i in range(1, 6):
    word = ''
    for y in range(i):
        word = word + "*"
    print(word)

#Challenge2
for i in range(7):
    word = '       '
    myList = list(word)
    myList[i] = '*'
    myList[-(i+1)] = '*'
    print("".join(myList))

#Challange3

def getNumFromUser():
    return int(input("Enter a number:"))

def sumOfDigits():
    sum = 0
    x = str(getNumFromUser())
    for i in x:
        sum = sum + int(i)
    calc = list(x)
    calc_string = " + ".join(calc) + f" = {sum}"
    print(calc_string)
    print(sum)

sumOfDigits()

