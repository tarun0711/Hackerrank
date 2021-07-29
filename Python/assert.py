
def fib_rec(n):
 if(n<=1):
    return n
 else:
     return fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
 cur, nxt = 0, 1
 for k in range(n):
     cur, nxt = nxt, cur+nxt
 return cur

def fib_upto(n):
 cur, nxt = 0, 1
 lst = []
 while(cur<=n):
     lst.append(cur)
     cur, nxt = nxt, cur+nxt
 return lst

def __print__():
 print(1)

def printHi():
 print("Hi")

if __name__ == "__main__":
 import sys
 print(fib_iter(int(sys.argv[1])))
