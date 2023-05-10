import sys
file = open("input.txt", "r")
numbers = []

for line in file:
    numbers_line = line.split(',')
    for number in numbers_line:
        numbers.append(int(number))

acc = [ 0 for _ in numbers ]
numbers.sort()

for idx in range(1, len(numbers)):
    if idx - 2 >= 0:
        acc[idx] += acc[idx - 2]
    if idx - 1 >= 0:
        acc[idx] += (numbers[idx] - numbers[idx - 1])

mn = sys.maxsize
for idx in range(len(acc)):
    cost = 0
    if idx % 2 == 0:
        if idx - 1 >= 0:
            cost += acc[idx - 1]
        cost += (acc[len(acc) - 1] - acc[idx])
        mn = min(mn, cost)
    else:
        if idx - 2 >= 0:
            cost += acc[idx - 2]
        if idx + 1 < len(acc):
            cost += (acc[len(acc) - 1] - acc[idx + 1])
        cost += (numbers[idx + 1] - numbers[idx - 1])
        mn = min(mn, cost)

print(f"The minimum cost of this array of efficiencies is {mn}.")
file.close()