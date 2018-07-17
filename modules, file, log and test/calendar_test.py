import calendar


cl_year = calendar.calendar(2018, w=2, l=1, c=8)
print(cl_year)  # 输出某年的日历
print(calendar.month(1028,2))  # 获取某一个某一月的日历

print('-----------------------')
print(calendar.isleap(2018))  # 判断是不是闰年
print(calendar.leapdays(1823,2018))  # 获取两个年份之间有多少个闰年
print(calendar.monthrange(2018,12))  #获取某年某月是周几开始的，以及有多少天
print(calendar.monthcalendar(2018,3))  # 获取一个月每天的矩阵列表
calendar.prcal(2018)   # 打印某一年的日历
calendar.prmonth(2018,3)  # 打印某月的日历
print('--'*20)
print(calendar.weekday(2018,3,21))  # 获取某天是周几
