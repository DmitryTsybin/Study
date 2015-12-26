a = 999
b = 999
palindromes = []

for n in range(1,1000):
  for m in range(1,1000):
    num = m*n

    if str(num) == str(num)[::-1]:
      palindromes.append(num)

print(max(palindromes))
