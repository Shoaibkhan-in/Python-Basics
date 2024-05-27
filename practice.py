def falseposition(f, x0, x1, e):
    x0=float(x0)
    x1=float(x1)
    e=float(e)
    if f(x0)*f(x1)>0.0:
        print("The given guessed value does not bracket the root")
        print("try again with different value")
    else:
        step=1
        condition=True
        while condition:
            x2=x0-(x1-x0)*f(x0)/f(x1)-f(x0)
            print("the iteration %d  x2=%0.6f  f(x2)=%0.6f"%(step, x2, f(x2)))
            break
        if f(x0)*f(x2)<0:
            x1=x2
        else:
            x0=x2
            step=step+1
            condition=abs(f(x2))>e
            print("The required root is %0.8f"%x2)

def f(x):
    return x**3-2*x-5
