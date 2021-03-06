from time import asctime
from time import localtime
from time import time

def giveTime():
    '''RETURN string in format: YYYYMMDDhhmmss
    exp: output 20210625230300 means 2021/06/25 at 23:03:00
    '''
    lct = localtime()
    year = str(lct[0])
    month = fom0(str(lct[1]))
    date = fom0(str(lct[2]))
    hr = fom0(str(lct[3]))
    minute = fom0(str(lct[4]))
    sec = fom0(str(lct[5]))
    
    res = year + '/' + month + '/' + date + ' @  '+ hr +':'+ minute +':'+ sec
    return res

def sec():
    return time()

def diff(before,after):
    res = -1
    # compare
    res = after - before
    
    # return
    return res
    
    
def fom(sec):
    hr = int(sec / 3600)
    rim = sec % 3600
    minute = int(rim / 60)
    sec = int(rim % 60)
    res = [hr,minute,sec]
    return res

def fom0(str):
    if len(str) == 1:
        return('0'+str)
    else:
        return(str)
