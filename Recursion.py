def function(x):
    if x == 1:
        return 1
    else:
        return x * function(x-1)

print(function(5))

def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))