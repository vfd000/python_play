def make_squares(max_squares):
  squares = []
  i=0
  while i < max_squares:
    squares.append(i**2)
    i += 1
  return squares

def make_fib(max_fib):
  fib = []
  i=0
  a, b = 0,1
  while i< max_fib:
    fib.append(a)
    a, b = b, a+b
    i +=1
    
  return fib

def make_fib_squares(max_value):
  return {'fib':make_fib(max_value), 'squares':make_squares(max_value)}

for l in range(10):
  
  alpha = make_fib_squares(l)
  print('calculations for ' , l, ':\t')
  for key in (sorted(list(alpha.keys()))):
    
    print(key, ":\t" , alpha[key])

  

