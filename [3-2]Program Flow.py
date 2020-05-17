lower = 0
upper = 50
print("prime numbers between", lower, "and", upper, "are: ")
def prime(n):
    result = [2]
    if n <= 2:
        return result

    for i in range(3, n+1, 2):
        for j in range(3, int(i/2), 2):
            a = i%j
            if a == 0:
                break
        else:
            result.append(i)

    return result

result = prime(50)
print(result)
