def f(n):
  a = (n % 100 - n % 10) / 10
  b = (n % 10) / 10
  c = ((n - n % 10) / 10) % 10

  return a, b, c

print f(2359)
