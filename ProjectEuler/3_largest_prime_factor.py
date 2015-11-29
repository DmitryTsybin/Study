import math
num = 600851475143
sqrt = int(math.sqrt(num))
numDividers = []
simpleNumDividers = []

def calculateDividers(number):
    print('inside calculateDividers, number: ', number)
    dividers = []

    sqrt = int(math.sqrt(number))
    for i in range(2, sqrt):
        if number % i == 0:
            dividers.append(i)
            
    return dividers

numDividers = calculateDividers(num)

for elem in numDividers:
    dividers = calculateDividers(elem)
    if len(dividers) == 0:
        simpleNumDividers.append(elem)

print(max(simpleNumDividers))
