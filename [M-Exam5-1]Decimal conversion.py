dec =int(input("Enter a decimal number: "))

def dec_converter(dec, base):
    s=""
    if base==8:
        while True:
            a=dec//base
            b= dec%base
            s=str(b)+s
            if (a==0):
                break
            dec=a
        return s
    elif base==2:
        while (dec >0):
            c=dec%2
            dec=dec//2
            s=str(c)+s
        return s



print(dec_converter(dec, 2))
print(dec_converter(dec, 8))
