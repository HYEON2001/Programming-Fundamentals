import time

def getDay():
    t = time.localtime()
    day_list = ['월', '화', '수', '목', '금', '토', '일']
    return day_list[t.tm_wday]




print('오늘은 {}요일입니다.'.format(getDay()))