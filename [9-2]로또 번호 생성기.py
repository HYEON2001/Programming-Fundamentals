import random
lotto = []
print("** 로또 추첨을 시작합니다 **\n")
for a in range(6):
    while True:
        a=random.randrange(1,46)
        if a not in lotto:
            lotto.append(a)
            break
print("추첨된 로또 번호 ==> {}".format(lotto))