file = open('input.txt', 'r')
string = ''
nodes = []
ocurrences = {}
last_char = None
operations = 0

for line in file:
    line = line.replace('\n', '')
    string += line

for ch in string:
    if ch == None or ch != last_char:
        nodes.append(ch)
        last_char = ch
        if not ch in ocurrences:
            ocurrences[ch] = 0
        ocurrences[ch] += 1

for i in range(len(ocurrences)):
    if len(ocurrences) == 0:
        break
    ch = min(ocurrences, key=ocurrences.get)
    nodes_tmp = [ nodes[0] ]
    for idx in range(len(nodes)):
        if idx + 1 <= len(nodes) - 1 and nodes[idx] == ch:
            if nodes_tmp[-1] == nodes[idx + 1]:
                ocurrences[nodes[idx + 1]] -= 1
        elif nodes_tmp[-1] != nodes[idx]:
            nodes_tmp.append(nodes[idx])
    nodes = nodes_tmp.copy()
    nodes = list(filter(lambda x: x != ch, nodes))
    operations += ocurrences.pop(ch)

print(f'The minimum number of operations required is {operations}')
file.close()