file = open('input.txt', 'r')
encoded = ''
codebook = {
    'a': '00',
    'b': '01',
    'c': '10',
    'd': '1100',
    'e': '1101',
    'f': '1110',
    'g': '111100',
    'h': '111101',
    'i': '111110',
    'j': '1111110000',
    'k': '1111110001',
    'l': '1111110010',
    'm': '1111110011',
    'n': '1111110100',
    'o': '1111110101',
    'p': '1111110110',
    'q': '1111110111',
    'r': '1111111000',
    's': '1111111001',
    't': '1111111010',
    'u': '1111111011',
    'v': '1111111100',
    'w': '1111111101',
    'x': '1111111110',
    'y': '1111111111',
    'z': '11111111110000',
    ' ': '11111111110001'
}

def decode(encoded):
    decoded = ''

    while encoded != '':
        for key, value in codebook.items():
            if encoded.find(value) == 0:
                encoded = encoded.replace(value, key, 1)
                decoded += encoded[0]
                encoded = encoded[1:]
                break
    
    decoded = decoded.replace('yaa', '/yaa/')
    decoded = decoded.replace('yab', '/yab/')
    decoded = decoded.replace('//', '/')

    return decoded

for line in file:
    line = line.replace('\n', '')
    encoded += line

decoded = decode(encoded)
print(f"The partially decoded string is: \n'{decoded}'\nYou can replace some '/yaa/'s with 'z' or '/yab/'s with ' ' to get a better response")
file.close()