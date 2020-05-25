X= [[12,7],
    [4,5],
    [3,8]]

result = [[0,0,0],
          [0,0,0]]

for i in range(3):
    for j in range(2):
        result[j][i] = X[i][j]

print("{} --> {}".format(X, result))
