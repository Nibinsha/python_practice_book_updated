import time
def fib(n):
    if n ==0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)


def profile(fun):
   def g(x):
      t=0
      start=time.time()
      v=fun(x)
      t=time.time()-start
      return str(t)+'  sec'
   return g

fib = profile(fib)
print fib(26)
