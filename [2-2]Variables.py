time_now = int(input("현재 몇 시입니까?"))

hours_to_wait = int(input("몇 시간 후에 알람을 올리게 할 것입니까?"))

print((time_now + hours_to_wait)%24)