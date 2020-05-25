deta_list = [(90, 80), (85, 75), (90, 100)]

for i, data in enumerate(deta_list):
    print("{}번 학생: 총정 {}점, 평균 {}점".
          format(i+1, sum(data), sum(data)/2))
