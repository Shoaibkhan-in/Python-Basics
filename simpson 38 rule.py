def simpson38(f,a,b,n):
    h=float(b-a)/n
    result=f(a)+f(b)
    for i in range (1,n):
        k=a+i*h
        if i%2==0:
            result=result+2*f(k)
        else:
            result=result+3*f(k)
            result=(3*h)/8
            return result

from math import *
def f(x):
    return cos(x)
