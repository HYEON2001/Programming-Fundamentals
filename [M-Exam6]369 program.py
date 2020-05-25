r =0
l=str(369)
while 1:
    r+=1
    n =input("Enter your number: ")
    count = (lambda x: sum([x.count(c) for c in l]))(str(r))
    if count:
        d  = "clap"*count
        if n ==d:
            print(n)
        else:
            print("Game over!")
            break
    else:
        if r == int(n):
            print(n)
        else:
            print("Game over!")
            break   #수고하셨습니다