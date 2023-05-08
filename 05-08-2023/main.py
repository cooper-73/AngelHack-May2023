import itertools
import sys

file = open("input.txt", "r")
number = file.readline()
flag = False
mn = sys.maxsize
mx = 0

for permutation in itertools.permutations(number):
    n_permutation = int("".join(permutation))
    if n_permutation % 7 == 0:
        flag = True
        mn = min(mn, n_permutation)
        mx = max(mx, n_permutation)

if flag:
    average = (mn + mx) / 2
    print(f"There are divisible permutations and the average of the min ({mn}) and max ({mx}) of them is {average}")
else:
    print("There aren't divisible permutations")
file.close()