input_str = input("문자열을 입력하세요: ")
dic = {}
for i in input_str:
    dic[i] = dic.get(i, 0)+1




print('Dictionarty: ', dic)
print('한번만 등장한 문자 수: ', len([i for i in dic.keys() if dic[i] ==1]))