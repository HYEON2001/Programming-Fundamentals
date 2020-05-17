a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

D = (b**2) - (4*a*c)

x_1 = (-b + D**0.5 ) / (2*a)
x_2 = (-b - D**0.5 ) / (2*a)

print(x_1, x_2)