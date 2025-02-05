import cProfile
import calendar
import collections
import datetime
import getpass
import glob
import hashlib
import math
import os
import platform
import re
import site
import socket
import struct
import subprocess
import sys
import time
import traceback
import urllib.request
from functools import reduce
from http.client import HTTPResponse
from pathlib import Path

# TASK 1
string_ = (" ".join(sys.argv[1:len(sys.argv) - 1]))
# @formatter:off
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
# @formatter:on

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
# seq = input().replace(" ", "")
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
print(f"First item: {color_list[0]}\nLast item: {color_list[-1]}")

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
# print(inspect.getdoc(abs))

# TASK 12
monthlist = calendar.monthcalendar(1987, 1)

for week in monthlist:
    for day in week:
        if day == 0:
            print("   ", end="")
        else:
            print(str(day).rjust(3, " "), end="")
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
    print(f"{num} " + ("within 100 of 1000" if abs(num - 1000) <= 100 else "within 100 of 2000" if abs(
        num - 2000) <= 100 else "IS NOT within 100 of 1000 or 2000"))


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


# TASK 19
# str_ = input("String: ")
# if str_.startswith("Is"):
#     print(str_)
# else:
#     print(f"Is{str_}")
def newstr(str_: str):
    print(f"{"Is" if not str_.startswith("Is") else ""}{str_}")


newstr("All")
newstr("IsDone")


# TASK 20
def multstr(s: str, mult: int) -> str:
    return s * mult if mult > 0 else "empty" if mult == 0 else "negative mult is not allowed"


print(multstr("test", 0))
print(multstr("test", -1))
print(multstr("test", 2))


# TASK 21
def oddeven(num: int):
    print(f"{num} is {"odd" if num % 2 == 1 else "even"}")


oddeven(1)
oddeven(2)
oddeven(-1)
oddeven(0)
oddeven(-7)

# TASK 22
l = [1, 2, 3, 4, 5, 6, 4, 3, 4, 5, 2, 4, 5, 6, 7, 4, 5, 4, 4, 4, 4, 4, 4]
# print(f"Number of fours in a list is {l.count(4)}")
counter = 0

for i in l:
    if i == 4:
        counter += 1

print(f"Number of fours in a list is {counter}")


# TASK 23
# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
def copy2first(str_: str, n: int) -> str:
    return str_ * n if n < 2 else str_[0:2] * n


print(copy2first("abcdef", 1))
print(copy2first("abcdef", 2))
print(copy2first("abcdef", 0))


# TASK 24
# all_vowels = "aeiou" #test in all_vowels
def is_vowel(char: str) -> bool:
    if len(char) != 1:
        print(f"{char} is not a single character")
        return False
    return True if char in ["a", "e", "i", "o", "u", "y"] else False


print(is_vowel("a"))
print(is_vowel("d"))

# TASK 25
print(f"Is 3 in [1,2,4,3]? {3 in [1, 2, 4, 3]}")
print(f"Is -1 in [1,2,4,3]? {-1 in [1, 2, 4, 3]}")


# TASK 26
# todo add checking for negative numers in list and/or print negative values
def hist(l: list, char: str = "-"):
    for item in l:
        print(char * item)


hist([2, 5, 8, 1, 2, 3])
hist([2, 5, 8, 1, 2, 3], "#")

# TASK 27
print("".join([str(x) for x in [1, 3, 4, 5, 6, 7]]))

# TASK 28
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 743, 527
]

for i in numbers:
    if i % 2 == 0:
        print(f"{i} ", end="")
    elif i == 237:
        break
print()

# TASK 29
color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]

# if len(color_list_1) >= len(color_list_2):
for i in color_list_1:
    if i not in color_list_2:
        print(i)


# else:
#     for i in color_list_2:
#         if i not in color_list_1:
#             print(i)

# TASK 30
def triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height  # todo learn what is faster, div by 2 or mult by 0.5


print(triangle_area(1, 2))


# TASK 31
# Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
def gcd(num1: int, num2: int) -> int:
    # make sure that num1 is lower than num2 despite the args (swap)
    if num1 > num2:
        num1, num2 = num2, num1
        # tmp = num2
        # num2 = num1
        # num1 = tmp

    greatest = 1
    for i in range(num1):
        if i < 1: continue
        index = i + 1
        if num1 % index == 0 and index <= num2 / 2 and num2 % index == 0:
            greatest = index
    return greatest


print(gcd(120, 60))
print(gcd(60, 12))


# TASK 32
# Write a Python program to find the least common multiple (LCM) of two positive integers.
def lcm(num1: int, num2: int) -> int:
    # make sure that num1 is lower than num2 despite the args (swap)
    if num1 > num2:
        num1, num2 = num2, num1

    lowest = 1
    for i in range(num2):
        index = i + 1
        mult = num1 * index
        if num2 % mult == 0 or mult % num2 == 0:
            lowest = mult if mult > num2 else num2
            break
    return lowest


print(lcm(21, 63))


# TASK 33
# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
def sumsum(ints: []) -> int:
    for i in range(len(ints)):
        if ints.count(i) >= 2:
            return 0
    return sum(ints)


print(sumsum([1, 2, 4]))
print(sumsum([1, 1, 1]))
print(sumsum([1, 2, 2]))

# TASK 34
# SKIPPED, TOO EASY

# TASK 35
# SKIPPED, TOO EASY

# TASK 36
a = 1
b = 2.1
if type(a) is int and type(b) is int:
    print("Both objects are integers")
else:
    print("At least one of the object is not integer")


# TASK 37
# SKIPPET, TOO EASY

# TASK 38
# SKIPPET, TOO EASY

# TASK 39
# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79
def count_money(amount: float, interest: float, years: int) -> float:
    for i in range(years):
        amount += amount * (interest / 100)
    return amount


print(f"{count_money(10000, 3.5, 7):.2f}")

# TASK 40
# SKIPPED, TOO EASY

# TASK 41
print(Path("C:\\Users\\Shooler\\PycharmProjects\\python\\p01.py").exists())
print(Path("./p01.py").exists())
print(Path("p01.py").exists())

# TASK 42
print(f"{struct.calcsize("P") * 8}bit")

# TASK 43
print(os.name)
print(os.path.sep)
print(os.cpu_count())
print(platform.version())
print(platform.system())
print(platform.architecture())
print(platform.machine())
print(platform.node())
print(platform.processor())
print(platform.release())
print(platform.system())
print(platform.uname())

# TASK 44
print(site.getsitepackages())

# TASK 45
# call(["notepad", "/A", "p01.py"])

# TASK 46
print(Path(__file__))


# TASK 47
# SKIPPED, TOO EASY

# TASK 48
# Write a Python program to parse a string to float or integer.
def numconv(numerical: str) -> int | float:
    numerical = numerical.replace(" ", "")

    if "." in numerical or "," in numerical:
        return float(numerical)
    elif re.fullmatch("-?[0-9]+", numerical):
        return int(numerical)
    else:
        return -999.999


print(numconv("1234"))
print(numconv("-1234"))
print(numconv("1234.4"))
print(numconv("-1234.4"))
print(numconv("1 234"))


# TASK 49
def getfiles(dir: str = "", showhidden: bool = False):
    # todo fix hidden files because they contain the full path when dir is specified
    for i in Path(dir).iterdir():
        if not showhidden and str(i).startswith("."): continue
        print(i)


getfiles("c:\\users\\shooler")
getfiles(showhidden=True)


# TASK 50
# SKIPPED, TOO EASY

# TASK 51
def sumit():
    print(1 + 2)


cProfile.run("sumit()")

# TASK 52
# print("ERROR EXAMPLE", file=sys.stderr)

# TASK 53
# for i in os.environ.items():
#     print(i)
for item, value in os.environ.items():
    print("{}: {}".format(item, value))

print(os.environ.get("SESSIONNAME"))

# TASK 54
print(getpass.getuser())

# TASK 55
local_hostname = socket.gethostname()
print(local_hostname)
print(socket.gethostbyname(local_hostname))
print(socket.gethostbyname_ex(local_hostname))
# filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]

# TASK 56
# SKIPPED, SEEMED USELESS

# TASK 57
# SKIPPED, TOO EASY

# TASK 58
# SKIPPED, TOO EASY

# TASK 59
# SKIPPED, TOO EASY

# TASK 60
# SKIPPED, TOO EASY

# TASK 61
# SKIPPED, TOO EASY

# TASK 62
# SKIPPED, TOO EASY

# TASK 63
# SKIPPED, TOO EASY

# TASK 64
accessed_time = time.ctime(os.path.getatime("p01.py"))
created_time = time.ctime(os.path.getctime("p01.py"))
modified_time = time.ctime(os.path.getmtime("p01.py"))
print(f"{"accesed:":10} {accessed_time}\n{"created:":10} {created_time}\n{"modified:":10} {modified_time}")

# TASK 65
# SKIPPED, TOO EASY

# TASK 66
# SKIPPED, TOO EASY

# TASK 67
# SKIPPED, TOO EASY

# TASK 68
print(sum([int(x) for x in str(123600)]))

# TASK 69
print(sorted([1, 4, 2]))

# TASK 70
# sort files by date
files = glob.glob("*.py")
files.sort(key=os.path.getmtime)
print("\n".join(files))

# TASK 71
items = []
for i in list(Path().iterdir()):
    items.append(str(i))
items.sort(key=os.path.getctime)
print(items)
# check
for i in items:
    print(f"{i}: {time.ctime(os.path.getctime(i))}")

# TASK 72
# pretty print info
# help(math)
# functions and variables list
print(dir(math))

# TASK 73
# SKIPPED, TOO EASY

# TASK 74
print(hashlib.md5(b"word").digest())
print(hashlib.md5(b"word").hexdigest())

# TASK 75
# SKIPPED, SEEMED USELESS

# TASK 76
# SKIPPED, TOO EASY

# TASK 77
# SKIPPED, TOO EASY

# TASK 78
print(sorted(sys.builtin_module_names))

# TASK 79
# sys.getsizeof("asd")

# TASK 80
# sys.getrecursionlimit()

# TASK 81
tuple_ = (1, 2)
list_ = [1, 2]
set_ = {1, 2}
dictionary_ = {"a": 1, "b": 2}
print(sum(tuple_))
print(sum(list_))
print(sum(set_))
print(sum(dictionary_.values()))

# TASK 82
# SKIPPED, TOO EASY

# TASK 83
# todo collections.Counter does the same
sample = "Write a Python program to count the number of occurrences of a specific character in a string."
occurences = dict()
for i in sample:
    if occurences.get(i):
        occurences[i] += 1
    else:
        occurences[i] = 1

# ASCII alphabetic order
print(sorted(occurences.items(), key=lambda x: x[0]))
# ordered by value
print(sorted(occurences.items(), key=lambda x: x[1]))

# TASK 84
# SKIPPED, TOO EASY

# TASK 85
# SKIPPED, TOO EASY

# TASK 86
# SKIPPED, TOO EASY

# TASK 87
bytes = os.path.getsize(__file__)
print(f"{bytes}B")
print(f"{(bytes / 1024):.2f}KB")

# TASK 88
# SKIPPED, TOO EASY

# TASK 89
# SKIPPED, TOO EASY

# TASK 90
# f = open(__file__)
# d = open("copy.py", "w")
#
# for i in f:
#     d.write(i)
#
# f.close()
# d.close()

# TASK 91
# SKIPPED, TOO EASY

# TASK 92
# SKIPPED, TOO EASY

# TASK 93
x = 34
print("Value: ", x)
print("Type: ", type(x))
print("Memory address: ", id(x))

# TASK 94
str_ = b"abecedary"
print(list(str_))
# print(str_[0])
str_ = "abecedary"
print([ord(x) for x in str_])

# TASK 95
str_ = "a345"
try:
    # all characters are digits
    str_.isdigit()
    i = float(str_)
except (ValueError, TypeError):
    print("Not numeric")


# TASK 96
def s1():
    return s2()


def s2():
    return s3()


def s3():
    traceback.print_stack()
    print("s3")


# s1()

# TASK 97
# s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set("_ names i".split()))
# print("\n".join(" ".join(s_var_names[i:i + 8]) for i in range(0, len(s_var_names), 8)))

# TASK 98
# SKIPPED, TOO EASY

# TASK 99
# not working
os.system("cls")

# TASK 100
# SKIPPED, TOO EASY

# TASK 101
resp: HTTPResponse
with urllib.request.urlopen("https://raw.githubusercontent.com/Shooler87/python/refs/heads/final/README.md") as resp:
    print(resp.read().decode("utf-8"))

# TASK 102
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
# print(returned_text)

# TASK 103
p = Path("C:/users/shooler/desktop/why.png")
print(f"Dir separator: {os.sep}")
# print(str(p).rsplit(os.sep, 1)[1])
print(os.path.basename(p))

# TASK 104
# NOT FOR WINDOWS
# print("Effective group id: ", os.getegid())
# print("Effective user id: ", os.geteuid())
# print("Real group id: ", os.getgid())
# print("List of supplemental group ids: ", os.getgroups())

# TASK 105
# SKIPPED, TOO EASY

# TASK 106
# SKIPPED, TOO EASY

# TASK 107
# SKIPPED, TOO EASY

# TASK 108

# TASK 109
# SKIPPED, NO SOLUTION

# TASK 110
num_list = [45, 55, 60, 37, 100, 105, 220]
div15 = list(filter(lambda x: (x % 15 == 0), num_list))
print("Divisible by 15:", div15)

# TASK 111
# SKIPPED, TOO EASY

# TASK 112
a = [1, 2, 3, 4, 5, 2]
b = a[1:]
a.pop(0)
a.remove(2)
del a[0]
print(a)
print(b)

# TASK 113
# SKIPPED, TOO EASY

# TASK 114
a = [1, -8, 2, 3, -4, -5, -1, 99]
print([x for x in a if x > 0])
print(list(filter(lambda x: x > 0, a)))


# TASK 115
def multit(a: int, b: int) -> int:
    return a * b


a = [10, 20, 30]
print(reduce(multit, a))
print(reduce((lambda x, y: x * y), a))

# TASK 116
# SKIPPED, TOO EASY

# TASK 117
# SKIPPED, TOO EASY

# TASK 118
print(bytearray([1, 2, 3, 255]))

# TASK 119
# SKIPPED, TOO EASY

# TASK 120
t = "test"
print(f"{t:.2s}")

# TASK 121
try:
    x = 1
    yyyy
except NameError:
    print("oops")

# TASK 122
print([type(x)() for x in ["python", {"x": 12}, [10, 12, "sfsd"], (4, 5), 200]])

# TASK 123
print(f"Int value information: {sys.int_info}\nFloat value information: {sys.float_info}\nMax int: {sys.maxsize}")

# TASK 124
a, b, c = 1, 1, 2
print(f"{"Same value" if len({a, b, c}) == 1 else "Different values"}")

# TASK 125
num = [2, 2, 4, 6, 6, 8, 6, 10, 4]
print(collections.Counter(num), sum(collections.Counter(num).values()))

# TASK 126
# SKIPPED, TOO EASY

# TASK 127
# int_val.bit_length()

# TASK 128
s = "The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE The Big Words Are HERE "
# "".join(list(filter(lambda x: x == x.lower(), s*100)))
start = time.time()
any(x.islower() for x in s * 100000)
end = time.time() - start
print(end)
start = time.time()
for i in s * 100000:
    if i.islower():
        break
end = time.time() - start
print(end)

# TASK 129
s = "984.98"
a = 984
b = 984.12
print(f"{s:-^17s}", f"{a:06}")
print(str(a).ljust(6, "0"), str(b).rjust(9, "0"))
print(f"{a:<08} {b:>08}")


# TASK 130
# todo check json dump function
def quot(s: str) -> str:
    return f"\"{s}\""


print(quot("testing this"))

# TASK 131
# var_list = ['a', 'b', 'c']
# x, y, z = (var_list + [None] * 3)[:3]

# TASK 132
# SKIPPED, SEEMED USELESS

# TASK 133
# SKIPPED, TOO EASY

# TASK 134
# s = input("Provide two integers separated by space: ")
s = "12 66"
try:
    a, b = map(int, s.split())
    print(a, b)
except ValueError:
    print("Next time integers only please")

# TASK 135
# SKIPPED, TOO EASY

# TASK 136
# SKIPPED, TOO EASY

# TASK 137
d = {"test": 2, "too": 5}
a, b = "test", d.get("test")
print(a, b)
a, b = list(d.items())[1]
print(a, b)

# TASK 138
print(int(True), int(False))


# TASK 139
def valip(ip: str) -> bool:
    if not re.match("^([0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
        print(f"invalid {ip=} (simple regex check)")
        return False
    else:
        return not False in [0 <= int(x) <= 255 for x in ip.split(".")]


def regexvalip(ip: str) -> bool:
    return bool(re.match("^((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$", ip))


print(valip("133.123.123.133"), regexvalip("133.123.123.133"))
print(valip("0.0.0.0"))
print(valip("133.123.123"))
print(valip("133.123"))

# TASK 140
# SKIPPED, TOO EASY

# TASK 141
print(hex(100), int(0x64))


# TASK 142
def check(s: str) -> bool:
    if not s.startswith("0"):
        return False
    pos = None
    for i in range(len(s)):
        # print(f"{str(i):-^7s}")
        if s[i] == "1":
            pos = i
            break

    # print(pos, f"^(0{{{pos}}}1{{{pos}}})+$")
    return bool(re.match(f"^(0{{{pos}}}1{{{pos}}})+$", s))

print(check("001100111"))

# TASK 143
# SKIPPED, DUPLICATE

# TASK 144
# isinstance vs type(var)

# TASK 145
# SKIPPED, TOO EASY

# TASK 146
# SKIPPED, DUPLICATE

# TASK 147
# SKIPPED, TOO EASY

# TASK 148
# SKIPPED, TOO EASY

# TASK 149
# SKIPPED, TOO EASY

# TASK 150
# SKIPPED, TOO EASY
