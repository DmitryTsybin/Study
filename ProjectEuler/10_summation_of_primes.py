import math

def calculateDividers(number):
    dividers = []

    sqrt = int(math.sqrt(number))
    for i in range(2, sqrt + 1):
        if number % i == 0:
            dividers.append(i)
            
    return dividers

simpleNumbers= [2]

i = 3
while (i < 2000000):
  if len(calculateDividers(i)) == 0:
    simpleNumbers.append(i)
    # print(i)
  i += 2

sum = 0
for i in simpleNumbers:
    sum += i

print(sum)
