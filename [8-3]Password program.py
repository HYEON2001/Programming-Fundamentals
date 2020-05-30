def encode():
    with open('ori.txt', 'r', encoding='utf-8') as f1:
        with open('encoded.txt', 'w', encoding='utf-8') as f2:
            for line in f1.readlines():
                for i in line:
                    f2.write( chr( ord(i) + 100))

def decode():
    with open('encoded.txt', 'r', encoding='utf-8') as f1:
        with open('decoded.txt', 'w', encoding='utf-8') as f2:
            for line in f1.readlines():
                for i in line:
                    f2.write( chr( ord(i) - 100))

encode()
decode()