# TASK 1
import collections
import itertools
import urllib.request
from collections import Counter
import bs4
from bs4 import BeautifulSoup as soup, PageElement, Tag, NavigableString

l = [1, 2, 3, 4, 5, 6, 4, 3, 2]
for i in l:
    if l.pop() in l:
        print("has duplicates")
        break

print(collections.Counter(l), any([x > 1 for x in collections.Counter(l).values()]))

# TASK 2
print([x for x in itertools.permutations("aeird")])

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
        print(x, " ", end="")
print()

# TASK 5
for i in itertools.product("0123456789", repeat=3):
    print("".join(i), end=" ")
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

print(cnt)

# TASK 7
with open("p01.py") as f:
    print(collections.Counter(f.read()))

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


# TASK 10


# TASK 11


# TASK 12


# TASK 13


# TASK 14


# TASK 15


# TASK 16


# TASK 17


# TASK 18


# TASK 19


# TASK 20


# TASK 21


# TASK 22


# TASK 23


# TASK 24


# TASK 25


# TASK 26


# TASK 27


# TASK 28


# TASK 29


# TASK 30


# TASK 31


# TASK 32


# TASK 33


# TASK 34


# TASK 35


# TASK 36


# TASK 37


# TASK 38


# TASK 39


# TASK 40


# TASK 41


# TASK 42


# TASK 43


# TASK 44


# TASK 45


# TASK 46


# TASK 47


# TASK 48


# TASK 49


# TASK 50


# TASK 51


# TASK 52


# TASK 53


# TASK 54


# TASK 55


# TASK 56


# TASK 57


# TASK 58


# TASK 59


# TASK 60


# TASK 61


# TASK 62


# TASK 63


# TASK 64


# TASK 65


# TASK 66


# TASK 67


# TASK 68


# TASK 69


# TASK 70


# TASK 71


# TASK 72


# TASK 73


# TASK 74


# TASK 75


# TASK 76


# TASK 77


# TASK 78


# TASK 79


# TASK 80


# TASK 81


# TASK 82


# TASK 83


# TASK 84


# TASK 85


# TASK 86


# TASK 87


# TASK 88


# TASK 89


# TASK 90


# TASK 91


# TASK 92


# TASK 93


# TASK 94


# TASK 95


# TASK 96


# TASK 97


# TASK 98


# TASK 99


# TASK 100


# TASK 101


# TASK 102


# TASK 103


# TASK 104


# TASK 105


# TASK 106


# TASK 107


# TASK 108


# TASK 109


# TASK 110


# TASK 111


# TASK 112


# TASK 113


# TASK 114


# TASK 115


# TASK 116


# TASK 117


# TASK 118


# TASK 119


# TASK 120


# TASK 121


# TASK 122


# TASK 123


# TASK 124


# TASK 125


# TASK 126


# TASK 127


# TASK 128


# TASK 129


# TASK 130


# TASK 131


# TASK 132


# TASK 133


# TASK 134


# TASK 135


# TASK 136


# TASK 137


# TASK 138


# TASK 139


# TASK 140


# TASK 141


# TASK 142


# TASK 143


# TASK 144


# TASK 145


# TASK 146


# TASK 147


# TASK 148


# TASK 149


# TASK 150
