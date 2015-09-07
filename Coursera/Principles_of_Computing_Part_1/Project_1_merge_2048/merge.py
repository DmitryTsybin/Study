"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    tight_line = tight(line[:])

    iter_i = 0
    while iter_i <= len(tight_line) - 2:
      if tight_line[iter_i] != 0 and tight_line[iter_i] == tight_line[iter_i + 1]:
        tight_line[iter_i] *= 2
        tight_line[iter_i + 1] = 0
        iter_i += 2
      else:
        iter_i += 1

    return tight(tight_line)


def tight(line):
  """
  Function that move all zeroes to the end of the list.
  """
  for iter_j in xrange(len(line)):
    iter_i = iter_j - 1
    while iter_i >= 0:
      if line[iter_i] == 0:
        line[iter_i] = line[iter_i + 1]
        line[iter_i + 1] = 0
      iter_i -= 1
  return line


#print tight([2, 0, 2, 4])
#print tight([0, 0, 2, 2])
#print tight([2, 2, 0, 0])
#print tight([2, 2, 2, 2, 2])
#print tight([8, 16, 16, 8])


print merge([8, 8]) == [16, 0]
print merge([4, 8, 4, 4, 8]) == [4, 8, 8, 8, 0]
#print merge([4, 8, 4, 4, 8])
print merge([2, 0, 2, 4]) == [4, 4, 0, 0]
print merge([0, 0, 2, 2]) == [4, 0, 0, 0]
print merge([2, 2, 0, 0]) == [4, 0, 0, 0]
print merge([2, 2, 2, 2, 2]) == [4, 4, 2, 0, 0]
#print merge([2, 2, 2, 2, 2])
print merge([8, 16, 16, 8]) == [8, 32, 8, 0]

