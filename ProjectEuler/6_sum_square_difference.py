sumSquare = 0
squareSum = 0

for i in range (1,101):
  squareSum += i
  sumSquare += i**2
squareSum = squareSum**2

print(squareSum - sumSquare)
