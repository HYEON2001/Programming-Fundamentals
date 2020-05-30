with open('q2.txt', 'r') as f:
    contents =f.read()
    word_list =contents.split()
    line_list =contents.split('\n')


print("총 글자 수: ", len(contents))
print("총 단어 수: ", len(word_list))
print("총 줄 수: ", len(line_list))
