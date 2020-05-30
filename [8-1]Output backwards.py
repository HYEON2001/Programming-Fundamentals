with open("input.txt", 'w', encoding='utf-8') as f:
    f.write("안녕하세요?\n")
    f.write("저는 프로그래밍기초 수업을\n")
    f.write("정말 즐겁고 행복하게 듣고 있습니다.\n")

with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f.readlines()[::-1]:
        print(line)
