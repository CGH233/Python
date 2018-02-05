#coding:utf-8
a = input()
if (a % 4) == 0 or (a % 100) == 0:
    print('闰年')
else:
    print('平年')
