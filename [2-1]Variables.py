p = int(input("원금을 입력하세요"))
r = float(input("이자율을 입력하세요"))
n = int(input("복리 계산 단위를 입력하세요"))
t = int(input("투자 기간을 입력하세요"))

A = p*((1+r/100*n)**(n*t))

print(int(A))