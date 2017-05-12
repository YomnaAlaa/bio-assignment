# for i in range(0,6,1):
#     temp = input("enter seq")
#     length = len(temp)
#     print(length)

# k = {}
#
# arr = ["123aa", "132ll" , "3445nj", "4k"]
# uu = []
# print("123aaa".__contains__("123"))
# for x in range(0, 4, 1):
#     uu.append(int(arr[x]))
#
# uu.sort()
# print(uu)
# CONV = {"K":["AAA","AAG"],
# "N":["AAC","AAU"],
# "T":["ACA","ACC","ACG","ACU"],
# "R":["AGA","AGG","CGA","CGC","CGG","CGU"],
# "S":["AGC","AGU","UCA","UCC","UCG","UCU"],
# "I":["AUA","AUC","AUU"],
# "Q":["CAA","CAG"],
# "H":["CAC","CAU"],
# "P":["CCA","CCC","CCG","CCU"],
# "L":["CUA","CUC","CUG","CUU","UUA","UUG"],
# "A":["GCA","GCC","GCG","GCU"],
# "D":["GAC","GAU"],
# "G":["GGA","GGC","GGG","GGU"],
# "V":["GUA","GUC","GUG","GUU"],
# "Y":["UAC","UAU"],
# "W":["UGG"],
# "C":["UGC","UGU"],
# "F":["UUC","UUU"],
# "E":["GAA","GAG"]}
#
# TR = input("enter letter: ")
# print(CONV[TR])

from itertools import permutations
from itertools import product

ll1 = 'ILEM'
ll = list(map(str, ll1))
print(ll)
# kk = list(permutations(ll))
# print(kk)
op = list(product(*ll))
print(op)