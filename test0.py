# from collections import Iterable
# import os
#
# print(isinstance('abc',Iterable))
# def trim(L=None):
#     if L is None:
#         L=''
#     M=L[1:len(L)-1]
#     return M
# print(trim(' qazxswedc '))
# print('\n qazxswedc ')
# d={'a':1,'b':2,'c':3}
# for value in d:
#     print(d[value])
# for key,value in enumerate(['a','b','c']):
#     print(key,value)
# print([x*x for x in range(1,11) if x %5==0])
# print([m +n for m in 'abc' for n in 'mfe'])
# print([d for d in os.listdir('.')])
# d={'s':'a','w':'q','r':'d'}
# for k,v in d.items():
#     print(k,'=',v)
# print([k + '=' + v for k,v in d.items()])
# g=(x*x for x in range(1,11))
# print(g)
# for i in g:
#     print(i)
# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         yield(b)
#         a,b=b,a+b
#         n=n+1
#     return 'done'
# a=fib(7)
# for  i in a:
#     print(i)
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)
# b=odd()
# for i in b:
#     print(i)
def lie(n=1):
    L=[1]
    if n ==1:
        print(L)
    else:
        for m in range(n):
            p=[1]
            print(L)
            if m==0:
                p.append(1)
            else :
                if m<n-1:
                    for i in range(m):
                            p.insert(i+1,L[i]+L[i+1])
                p.append(1)
            L=p
lie(8)
