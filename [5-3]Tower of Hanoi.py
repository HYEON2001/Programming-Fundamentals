def hanoi(disk, start, aux, end):
    if disk == 1:
        print(disk, ":" , start, '->' , end)
    else:
        hanoi(disk-1, start, end, aux)
        print(disk, ":", start, '->', end)
        hanoi(disk-1, aux, start, end)

n= int(input("원반 갯수: "))
hanoi(n, "start", "aux", "end")

