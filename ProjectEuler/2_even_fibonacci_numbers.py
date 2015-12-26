a = 0
b = 1
fib = 0
sum = 0

while a+b < 4000000:
    fib = a + b
    a = b
    b = fib

    if fib % 2 == 0:
        sum += fib

print(sum)
