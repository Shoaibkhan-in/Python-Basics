def newtonraphson (f,g,x0,e,N):
    x0=float(x0)
    e=float(e)
    N=int(N)
    step=1
    flag=1
    condition=True
    while condition:
        if g(x0)==0.0:
            print("Divide By Zero Error!")
            break
        x1=x0-f(x0)/g(x0)
        print("iteration- %d, x1=%0.6f and f(x1)=%0.6f"%(step, x1, f(x1)))
        x0=x1
        step=step+1
        if step>N:
            flag=0
            break
        condition=abs(f(x1))>e
        if flag==1:
            print("\n required root is : %0.8f"%x1)
        else: print("\n Not conveyed.")
        
        
def f(x):
    return x**3-5*x+1

def g(x):
    return 3*x**2-5
