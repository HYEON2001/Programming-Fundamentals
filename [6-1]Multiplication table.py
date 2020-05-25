print("           1    2    3    4    5    6    7    8    9   10   11   12")
print('-------------------------------------------------------------------')


for i in range(1,13):
    print(' {0:3d}:   '.format(i), end='')
    for j in range(1,13):
        print(" {0:3d}".format(i*j), end=" ")
    print()