dec = int(input("Enter a decimal number: "))

def dec_converter(dec, base):
    T = '0123456789ABCDE'
    if dec ==0:
        return ''
    else:
        return dec_converter(dec //base, base)+ T[dec%base]

print(dec_converter(dec, 2))
print(dec_converter(dec, 8))
