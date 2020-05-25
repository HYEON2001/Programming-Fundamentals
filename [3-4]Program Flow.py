num = int(input("Enter a number: "))

num1= num//100
num2= (num//10)%10
num3= num%10
if num == num1*num1*num1 + num2*num2*num2 + num3*num3*num3:
    print(str(num)+ " is an Armstrong number")
else:
    print(str(num)+ " is not an Armstrong number")

