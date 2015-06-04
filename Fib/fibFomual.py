def fib(n):
  res = ((1+math.sqrt(5))/2)**n- ((1-math.sqrt(5))/2)**n
  res /= math.sqrt(5) 
  return res


def fib(n):
  temp,res =0,1
  while res <n:
    yield res
    res,temp = res+temp,res

[i for i in fib(n)]
