""""
Asilbek Omonkulov
WorkingWithStrings
7/2/2018

Takes a text from a user and finds the top 10 most used words and displays them is console
"""
import re


def print_about():
    print("Asilbek Omonkulov")
    print("Takes a text from a user and finds the top 10 most used words and displays them is console,"
          " input should be one line.")
    print("---------------------------------------------------------------------------")


print_about()
# Input
words = input("Type here:   ")

# edit string
words = re.sub(r'[.,]', '', words)
words = words.replace("\n", "")
words = words.lower()
list1 = (words.split())

# create empty list2
list2 = [list1[0]]  # empty list 2
ab = 0
tempt = ""

# loop to put original worlds, non repeat in list 2
while ab < len(list1):
    tempt = list1[ab]
    if tempt not in list2:
        list2.append(tempt)
    ab = ab + 1
print("Word count: " + str(len(list1)))
print(list2)
list3 = []
d = 0
while len(list2) > d:
    tempt = list2[d]
    list3.append([list1.count(tempt), tempt])
    d = d + 1
list3.sort()
list3.reverse()
choice = int(input("The top numbers:    "))
inc = 0
print(list3[0:choice])
while inc < choice:
    print(inc + 1, ")  ", list3[inc][0], ":", list3[inc][1])
    inc += 1
