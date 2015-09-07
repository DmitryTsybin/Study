def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    if len(lst) < 3:
      return


    for i in xrange(25):
      sum = 0
      sum += lst[-1] + lst[-2] + lst [-3]
      lst.append(sum)


sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[20]

