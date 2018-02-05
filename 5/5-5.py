#coding:utf-8
x = input()
A = list(divmod(x,25))[0]
a = list(divmod(x,25))[1]
B = list(divmod(a,10))[0]
b = list(divmod(a,10))[1]
C = list(divmod(b,5))[0]
D = list(divmod(b,5))[1] 
print('25:%d\n10:%d\n5:%d\n1:%d') % (A,B,C,D)
