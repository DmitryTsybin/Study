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
while (len(simpleNumbers) < 10001):
  if len(calculateDividers(i)) == 0:
    #if i == 9:
    #  print('9: ', calculateDividers(9))
    simpleNumbers.append(i)
  i += 2

print(simpleNumbers)
print(simpleNumbers[-1])

