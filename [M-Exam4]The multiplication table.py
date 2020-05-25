n= int(input(("Multiplication table of N? ")))

a=0
while a<10:
    table=n*(a+1)
    a=a+1
    print("%d x %d = %d" %(n,a,table))
