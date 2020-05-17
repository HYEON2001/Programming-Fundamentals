year = int(input("년도를 입력하세요 : "))
if year%4 == 0 and year&100 != 0:
    print("A leap year")
elif year%400 == 0:
    print("A leap year")
elif year >= 0:
    print("not a leap year")
