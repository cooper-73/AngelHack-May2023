instructions = open("input.txt", "r")
floor = 0

while True:
    ch = instructions.read(1)

    if not ch:
        break
    
    if ch == '<':
        floor += 1
    elif ch == '>':
        floor -= 1

print(floor)
instructions.close()