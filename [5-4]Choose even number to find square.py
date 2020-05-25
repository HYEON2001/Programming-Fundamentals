list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_2 =list(filter( lambda a: (a%2==0) , list_1) )
result =list(map( lambda b: b*b, list_2))

print("list :", list_1)
print("result : ", result)
