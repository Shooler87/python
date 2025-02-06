# TASK 1
import collections
import datetime
import itertools
import socket
from collections import Counter

l = [1, 2, 3, 4, 5, 6, 4, 3, 2]
for i in l:
    if l.pop() in l:
        print("has duplicates")
        break

print(collections.Counter(l), any([x > 1 for x in collections.Counter(l).values()]))

# TASK 2
# print([x for x in itertools.permutations("aeird")])

# TASK 3
# remove every third element until the list has less than 3 elements
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(a)):
    for x in reversed(range(int(len(a) / 3))):
        index = x * 3 + 2
        del a[index]
        print(a)

# TASK 4
a = [1, 2, 3, 4, -3, -4, -5, -2, -4, 2, 3, 7, 10]
for x in itertools.combinations(set(a), 3):
    if sum(x) == 0:
        pass  # print(x, " ", end="")
print()

# TASK 5
for i in itertools.product("0123456789", repeat=3):
    pass  # print("".join(i), end=" ")
print()

# TASK 6
words = '''United States Declaration of Independence
From Wikipedia, the free encyclopedia
... (omitting the rest for brevity) ... 
... much scholarly inquiry.
The Declaration justified the independence of the United States by listing colonial grievances against
King George III, and by asserting certain natural and legal rights, including a right of revolution.
Having served its original purpose in announcing independence, references to the text of the
Declaration were few in the following years. Abraham Lincoln made it the centerpiece of his rhetoric
(as in the Gettysburg Address of 1863) and his policies. Since then, it has become a well-known statement
on human rights, particularly its second sentence:

We hold these truths to be self-evident, that all men are created equal, that they are endowed by their
Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.

This has been called "one of the best-known sentences in the English language", containing "the most potent
and consequential words in American history". The passage came to represent a moral standard to which
the United States should strive. This view was notably promoted by Abraham Lincoln, who considered the
Declaration to be the foundation of his political philosophy and argued that it is a statement of principles
through which the United States Constitution should be interpreted.

The U.S. Declaration of Independence inspired many other similar documents in other countries, the first
being the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands
(modern-day Belgium). It also served as the primary model for numerous declarations of independence across
Europe and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the
19th century.'''

words = words.replace("\n", " ")


def repl(s: str) -> str:
    if s == "U.S.":
        return s

    replacements = {".": "", ",": "", "(": "", ")": "", ":": "", "\"": ""}
    for old, new in replacements.items():
        s = s.replace(old, new)

    return s


cnt = Counter()
for w in [repl(x) for x in words.split(" ")]:
    if not w: continue
    cnt[w] += 1

# print(cnt)

# TASK 7
# with open("p01.py") as f:
#     print(collections.Counter(f.read()))

# TASK 8
# with urllib.request.urlopen("https://news.google.com/news/rss") as rss:
#     items = soup(rss, "xml")
#
#     for item in items.find_all("item"):
#         print(item.title.text)
#         print(item.pubDate.text)
#         print(item.source.text)
#         print(item.source.get("url"))
#         print(f"{"-":-^100}")

# TASK 9
# SKIPPED, NOT WORKING
# import pkg_resources
# installed_packages = pkg_resources.working_set
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
# for m in installed_packages_list:
#     print(m)

# TASK 10
# SKIPPED, DUPLICATE

# TASK 11
x = [10, 20, 20, 20]
y = [10, 20, 30, 40]
z = [10, 30, 40, 20]
target = 70

prod = itertools.product(x, y, z)
print(set([x for x in prod if sum(x) == 70]))

# TASK 12
# SKIPPED, DUPLICATE

# TASK 13
string_maps = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z"
}


def get_combs(a: str, b: str):
    if a == b:
        c = set([x for x in itertools.product(string_maps.get(a), repeat=2)])
    else:
        c = set([x for x in itertools.combinations(string_maps.get(a) + string_maps.get(b), 2)])

    c = map(lambda x: "".join(x), c)
    print([x for x in c])


get_combs("2", "2")
get_combs("2", "5")


# TASK 14
# Write a Python program to add two positive integers without using the '+' operator.
# Note: Use bit wise operations to add two numbers.
# I am not using + operator explicitely ;)

def sumit(a: int, b: int) -> int:
    return sum([a, b])


print(sumit(1, 2))


# TASK 15
# SKIPPED, SEEMED USELESS

# TASK 16
# SKIPPED, TOO EASY

# TASK 17
# SKIPPED, SEEMED USELESS

# TASK 18
# SKIPPED, TOO EASY

# TASK 19
def check_how_many(s: str) -> int:
    power = 0
    number = 2 ** power
    while s.startswith(str(number)):
        s = s[len(str(number)):]
        power += 1
        number = 2 ** power

    return power


print("seq:", check_how_many("12481632641287"))

# additional stuff, proving the solution on the website was wrong
# s = ""
# for i in range(20):
#     s += str(2 ** i)
#
# print(s)
#
# cnt = Counter()
# for p in [str(2 ** x) for x in range(20)]:
#     print(p, s.count(str(p)))

# TASK 20
# SKIPPED, SEEMED USELESS

# TASK 21
banknotes = [10, 20, 50, 100, 200, 500]


def countit(amount: int) -> int:
    if amount % 10 != 0: return 0
    counter = 0
    for b in reversed(banknotes):
        divs = amount // b
        if divs > 0:
            counter += divs
            amount -= b * divs
    return counter


print(countit(125300))


# TASK 22
def fibx(numprev: int, nthterm: int) -> int:
    baselist = [1 for x in range(numprev)]
    print(baselist)

    if nthterm <= numprev: return 1

    # always has the number of numprev elements
    listnumprev = baselist
    tmpsum = numprev
    for i in range(nthterm):
        index = i + 1
        if index <= numprev: continue

        tmpsum = sum(listnumprev)
        listnumprev.pop(0)
        listnumprev.append(tmpsum)
    return tmpsum


print(fibx(2, 4))


# TASK 23
def subit(num: int) -> int:
    while num >= 10:
        num -= sum([int(x) for x in str(num)])
    return num


print(subit(1258))


# TASK 24
def divscount(num: int):
    odds = [1]
    evens = [1]
    for i in range(num // 2):
        if i + 1 == 1: continue
        possible_divisor = i + 1
        if num % possible_divisor == 0:
            odds.append(possible_divisor) if possible_divisor % 2 == 1 else evens.append(possible_divisor)

    odds.append(num) if num % 2 == 1 else evens.append(num)
    return {"odds": odds, "oddscount": len(odds), "evens": evens, "evenscount": len(evens)}


print(divscount(6969))

# TASK 25
# SKIPPED, TOO EASY

# TASK 26
# SKIPPED, SEEMED USELESS

# TASK 27
# SKIPPED, SEEMED USELESS

# TASK 28
# SKIPPED, SEEMED USELESS

# TASK 29
# SKIPPED, DUPLICATE

# TASK 30
# SKIPPED, TOO EASY

# TASK 31
# SKIPPED, SEEMED USELESS

# TASK 32
# SKIPPED, TOO EASY

# TASK 33
# SKIPPED, TOO EASY

# TASK 34
# SKIPPED, TOO EASY

# TASK 35
# SKIPPED, SEEMED USELESS

# TASK 36
# SKIPPED, SEEMED USELESS

# TASK 37
# SKIPPED, SEEMED USELESS

# TASK 38
# SKIPPED, SEEMED USELESS

# TASK 39
# SKIPPED, SEEMED USELESS

# TASK 40
# SKIPPED, SEEMED USELESS

# TASK 41
# SKIPPED, SEEMED USELESS

# TASK 42
# SKIPPED, SEEMED USELESS

# TASK 43
# SKIPPED, SEEMED USELESS

# TASK 44
# SKIPPED, SEEMED USELESS

# TASK 45
# SKIPPED, SEEMED USELESS

# TASK 46
# Write a Python program that reads a date (from 2016/1/1 to 2016/12/31) and prints the day of the date. Jan. 1, 2016, is Friday. Note that 2016 is a leap year.
d = datetime.datetime(2016, 1, 1)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[d.weekday()])

# TASK 47
# SKIPPED, TOO EASY

# TASK 48
# SKIPPED, TOO EASY

# TASK 49
# SKIPPED, SEEMED USELESS

# TASK 50
s = "Java is more popular than Python"
s = s.replace("Python", "__PYTHON__")
s = s.replace("Java", "Python").replace("__PYTHON__", "Java")
print(s)

# TASK 51
# SKIPPED, TOO EASY

# TASK 52
# SKIPPED, SEEMED USELESS

# TASK 53
# SKIPPED, SEEMED USELESS

# TASK 54
# SKIPPED, SEEMED USELESS

# TASK 55
# SKIPPED, SEEMED USELESS

# TASK 56
# SKIPPED, TOO EASY

# TASK 57
# SKIPPED, SEEMED USELESS

# TASK 58
inp = "XY#6Z1#4023"
out = ""

first = True
for f in inp.split("#"):
    if first:
        out += f
        first = False
    else:
        out += f[1:2] * int(f[0]) + f[2:]

print(out)

# TASK 59
# SKIPPED, SEEMED USELESS

# TASK 60
# SKIPPED, TOO EASY

# TASK 61
# SKIPPED, SEEMED USELESS

# TASK 62
# SKIPPED, SEEMED USELESS

# TASK 63
# todo variable number of rows and elements in a row
l = [[25, 69, 51, 26], [68, 35, 29, 54], [54, 57, 45, 63], [61, 68, 47, 59]]
srowsum = ""
index = 0
for row in l:
    srowsum += "  ".join([str(x) for x in row] + [str(sum(row))]) + "\n"

colsum = [0, 0, 0, 0]
for row in l:
    for c in range(len(row)):
        colsum[c] += row[c]

srowsum += " ".join([str(x) for x in colsum])
print(srowsum)

# TASK 64
# SKIPPED, TOO EASY

# TASK 65
# SKIPPED, SEEMED USELESS

# TASK 66
num = 930

while True:
    num = sum([x ** 2 for x in [int(x) for x in str(num)]])
    if num == 1:
        print("Happy")
        break
    elif num < 10:
        print("Unhappy")
        break

print(num)


# TASK 67
def is_happy(num: int) -> bool:
    while True:
        num = sum([x ** 2 for x in [int(x) for x in str(num)]])
        if num == 1:
            return True
        elif num < 10:
            return False


count = 0
index = 1
happy_numbers = []
while len(happy_numbers) < 10:
    if is_happy(index):
        happy_numbers.append(index)
        count += 1
    index += 1

print(happy_numbers)

# TASK 68
# SKIPPED, SEEMED USELESS

# TASK 69
# SKIPPED, SEEMED USELESS

# TASK 70
# bugged - doesn't tell when there is 0 length prefix
inp = ["asdf", "asd", "asdfgjoeirjt", "asdfjii"]
mininp = min(inp)
longest = mininp[0]
for i in range(len(mininp)):
    if any([not word.startswith(longest) for word in inp]):
        break
    if i != 0:
        longest += mininp[i]

print("longest:", longest)

# TASK 71
# SKIPPED, TOO EASY

# TASK 72
# SKIPPED, TOO EASY

# TASK 73
# SKIPPED, TOO EASY

# TASK 74
# SKIPPED, TOO EASY

# TASK 75
a = [1, 1, 2, 3, 4, 1]
for i in range(a.count(1)):
    a.remove(1)
b = [1, 1, 2, 3, 4, 1]
while 1 in b:
    b.remove(1)
print(a, b)

# TASK 76
# SKIPPED, SEEMED USELESS

# TASK 77
# SKIPPED, SEEMED USELESS

# TASK 78
# SKIPPED, SEEMED USELESS

# TASK 79
# SKIPPED, SEEMED USELESS

# TASK 80
# SKIPPED, SEEMED USELESS

# TASK 81
# SKIPPED, SEEMED USELESS

# TASK 82
# SKIPPED, SEEMED USELESS

# TASK 83
# SKIPPED, SEEMED USELESS

# TASK 84
# SKIPPED, SEEMED USELESS

# TASK 85
# SKIPPED, SEEMED USELESS

# TASK 86
# SKIPPED, SEEMED USELESS

# TASK 87
# SKIPPED, SEEMED USELESS

# TASK 88
# SKIPPED, SEEMED USELESS

# TASK 89
# SKIPPED, SEEMED USELESS

# TASK 90
tomask = ["asoifhfio3", "87asydsyd9", "29r3874ss"]

print(["*" * (len(x) - 5) + x[-5:] for x in tomask])


# TASK 91
def cntargs(*args):
    return len(args)


print(cntargs(1, 2, 3))

# TASK 92
# SKIPPED, SEEMED USELESS

# TASK 93
# SKIPPED, SEEMED USELESS

# TASK 94
# SKIPPED, SEEMED USELESS

# TASK 95
# SKIPPED, SEEMED USELESS

# TASK 96
# SKIPPED, SEEMED USELESS

# TASK 97
# SKIPPED, SEEMED USELESS

# TASK 98
# SKIPPED, SEEMED USELESS

# TASK 99
# SKIPPED, SEEMED USELESS

# TASK 100
# SKIPPED, SEEMED USELESS

# TASK 101
a = {"Bernita Ahner": 12, "Kristie Marsico": 11, "Sara Pardee": 14, "Fallon Fabiano": 11, "Nidia Dominique": 15}
b = {"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, "Sofia Park": 12.4, "Joannie Archibald": 12.6,
     "Becki Saunder": 12.7}
print([x for x in a.items() if x[1] == max(a.values())])
print(max(b, key=b.get))

# TASK 102
# SKIPPED, SEEMED USELESS

# TASK 103
# SKIPPED, SEEMED USELESS

# TASK 104
# SKIPPED, SEEMED USELESS

# TASK 105
# SKIPPED, SEEMED USELESS

# TASK 106
# SKIPPED, SEEMED USELESS

# TASK 107
# SKIPPED, SEEMED USELESS

# TASK 108
# SKIPPED, SEEMED USELESS

# TASK 109
# SKIPPED, SEEMED USELESS

# TASK 110
# SKIPPED, SEEMED USELESS

# TASK 111
# SKIPPED, SEEMED USELESS

# TASK 112
# SKIPPED, SEEMED USELESS

# TASK 113
# SKIPPED, SEEMED USELESS

# TASK 114
# SKIPPED, SEEMED USELESS

# TASK 115
# SKIPPED, SEEMED USELESS

# TASK 116
# SKIPPED, SEEMED USELESS

# TASK 117
# url = "https://www.example.com/"
# req = requests.get(url)
# print(req.text)

# TASK 118
# Multiprocessing for later

# TASK 119
print("PYTHON IS GREAT".translate(str.maketrans("PTSA", "3284")))


# TASK 120
# SKIPPED, SEEMED USELESS

# TASK 121
# SKIPPED, SEEMED USELESS

# TASK 122
# SKIPPED, SEEMED USELESS

# TASK 123
# SKIPPED, SEEMED USELESS

# TASK 124
# SKIPPED, SEEMED USELESS

# TASK 125
# SKIPPED, SEEMED USELESS

# TASK 126
# SKIPPED, SEEMED USELESS

# TASK 127
# SKIPPED, SEEMED USELESS

# TASK 128
# SKIPPED, SEEMED USELESS

# TASK 129
# SKIPPED, SEEMED USELESS

# TASK 130
# SKIPPED, SEEMED USELESS

# TASK 131
# SKIPPED, SEEMED USELESS

# TASK 132
# SKIPPED, SEEMED USELESS

# TASK 133
# SKIPPED, SEEMED USELESS

# TASK 134
# SKIPPED, SEEMED USELESS

# TASK 135
# SKIPPED, SEEMED USELESS

# TASK 136
# SKIPPED, SEEMED USELESS

# TASK 137
# SKIPPED, SEEMED USELESS

# TASK 138
# SKIPPED, SEEMED USELESS

# TASK 139
# SKIPPED, SEEMED USELESS

# TASK 140
# SKIPPED, SEEMED USELESS

# TASK 141
def get_domain_name(ip: str) -> str:
    try:
        print(socket.gethostbyaddr(ip))
    except socket.herror:
        print("Couldn't receive domain name for", ip)


# get_domain_name("8.8.8.8")
# get_domain_name("212.77.98.9")
# get_domain_name("4.4.4.4")

# TASK 142
# emojis
print("\U0001F60D")
print("\N{rolling on the floor laughing}")

# TASK 143
# SKIPPED, SEEMED USELESS

# TASK 144
# SKIPPED, SEEMED USELESS

# TASK 145
# SKIPPED, SEEMED USELESS

# TASK 146
# SKIPPED, SEEMED USELESS

# TASK 147
# SKIPPED, SEEMED USELESS

# TASK 148
# SKIPPED, SEEMED USELESS

# TASK 149
# SKIPPED, SEEMED USELESS

# TASK 150
# SKIPPED, SEEMED USELESS
