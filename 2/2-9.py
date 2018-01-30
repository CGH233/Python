#coding: utf-8
a = 1
c = 0
while a < 6:
    b = input('输入第%d个数字'  %a)
    a += 1
    c += b
print(float(c)//5)
