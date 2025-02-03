import calendar
import datetime
import math
import sys

# TASK 1
string_ = (" ".join(sys.argv[1:len(sys.argv) - 1]))
print(
# adds new line after """
"""
Twinkle, twinkle, little star, 
    How I wonder what you are! 
        Up above the world so high, 
        Like a diamond in the sky. 
Twinkle, twinkle, little star, 
    How I wonder what you are
""")

# TASK 2
print(sys.version)

# TASK 3
print("Current date and time:")
print(str(datetime.datetime.now())[0:19])

# TASK 4
# r = float(input())
r = 1.7
print(f"r: {r}")
area = math.pi * (r ** 2)
print(f"area: {area:.2f}")

# TASK 5
# variant = int(input("[1] Full name.\n[2] Name and then Surname.\nChoose: "))
variant = 1
if variant == 1:
    # name = str(input("Full name: "))
    name = "Tester Testowy"
    split_ = name.split()
    print(f"{split_[1]} {split_[0]}")
elif variant == 2:
    name = str(input("Name: "))
    surname = str(input("Name: "))
    print(f"{surname} {name}")
else:
    print("Wrong input")

# TASK 6
# seq = input().replace(' ', '')
seq = "1,2,3,4,5,6,7,8"
seq_arr = seq.split(",")
lis = list(seq_arr)
tup = tuple(seq_arr)
print(f"list: {lis}")
print(f"tuple: {tup}")
# more inplace operations
# print("list: " + str(list(seq.split(","))))
# print("tuple: " + str(tuple(seq.split(","))))

# TASK 7
# inp = input("Filename: ")
inp = "file.add.txt"
spl = inp.split(".")
print(f"Extension: {spl[-1]}")
# print(f"Extension: {spl[len(spl) - 1]}")

# TASK 8
color_list = ["Red", "Green", "White", "Black"]
print(f"First item: {color_list[0]}\nLast item: {color_list[-1]}") \
 \
# TASK 9
exam_st_date = (11, 12, 2014)
print(" / ".join(str(item) for item in exam_st_date))

# TASK 10
# num = int(input("Integer please: "))
num = 21
strnum = str(num)
print(f"{strnum} + {strnum * 2} + {strnum * 3} equals {num + int(strnum * 2) + int(strnum * 3)}")

# TASK 11
print(abs.__doc__)
#print(inspect.getdoc(abs))

# TASK 12
monthlist = calendar.monthcalendar(1987, 1)

for week in monthlist:
    for day in week:
        if day == 0:
            print("   ", end='')
        else:
            print(str(day).rjust(3, ' '), end='')
    print("")

# print(calendar.month(1987, 1))

# TASK 13
print("""
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
""")

# TASK 14
x = datetime.date(2014, 7, 2)
y = datetime.date(2014, 7, 11)
print(f"{(y - x).days} days")

# TASK 15
r = 6
vol = 4 / 3 * math.pi * r ** 3
print(vol)

# TASK 16
num = 7
# num = 30
print(abs(num - 17) * (2 if num > 17 else 1))


# TASK 17
def close_check(num: int):
    print(f"{num} " + ("within 100 of 1000" if abs(num - 1000) <= 100 else "within 100 of 2000" if abs(num - 2000) <= 100 else "IS NOT within 100 of 1000 or 2000"))


close_check(100)
close_check(900)
close_check(999)
close_check(1000)
close_check(1080)
close_check(1280)
close_check(1900)
close_check(1999)
close_check(2000)
close_check(2050)
close_check(2250)

# TASK 18
def summit(a: int, b: int, c: int) -> int:
    if a == b == c:
        return a * 9
    else:
        return a + b + c


def summit2(a: int, b: int, c: int) -> int:
    return a * 9 if a == b == c else a + b + c


print(summit(1, 2, 3))
print(summit(3, 3, 3))
