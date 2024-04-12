# 对日期进行处理的操作
import datetime
import time
from time import struct_time
def timestamp2Datetime(timestamp):
    '''
    时间戳 转 日期字符串 此处没有考虑时区
    :param timestamp: 1607746332
    :return: 2020-12-12 12:12:12
    '''
    s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
    return s

def datetime2Timestamp(dateTime):
    '''
    时间字符串 转时间戳，此处没有考虑时区的问题
    :param dateTime:
    :return:
    '''
    # print(time.strptime(dateTime, "%Y-%m-%d %H:%M:%S"))
    s = time.mktime(time.strptime(dateTime, "%Y-%m-%d %H:%M:%S"))
    return s

def get_time_struct_from_datestr(dateTime)->struct_time:
    '''
    时间字符串转化为时间类型
    :param dateTime:
    :return:
    '''
    return time.strptime(dateTime, "%Y-%m-%d %H:%M:%S")

def getAfterNDays(dateStrStart,ndays):
    '''

    :param dateStrStart: 2020-01-02
    :param ndays:  10
    :return: 2020-01-12,None
    '''
    start = datetime2Timestamp(dateStrStart)
    if not start:
        return None
    else:
        end = start + ndays * 24*3600
        end = timestamp2Datetime(end)
        return end[:10]

def getNowStr():
    t = int(time.time())
    return timestamp2Datetime(t)


if __name__ == "__main__":
    datetime = getNowStr()
    print(get_time_struct_from_datestr(datetime).tm_hour)