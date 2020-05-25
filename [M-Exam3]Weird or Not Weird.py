n = int(input("Enter an integer number, n(1 <= n <= 100): "))

def is_weird(num):
    if num%2!=0:
        return"Weird"
    elif 2<=n<=5:
        return "Not Weird"
    elif 6<=n<=20:
        return "Weird"
    elif n>20:
        return "Not Weird"


print(is_weird(n))



