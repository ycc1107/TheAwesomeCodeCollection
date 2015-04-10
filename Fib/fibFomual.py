def fib(n):
  res = ((1+math.sqrt(5))/2)**n- ((1-math.sqrt(5))/2)**n
  res /= math.sqrt(5) 
  return res
