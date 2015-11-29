import re

sample_data = open('regex_sum_42.txt')
actual_data = open('regex_sum_190644.txt')

sample_sum = 0
actual_sum = 0

sample_numbers = re.findall("[0-9]+", sample_data.read())
actual_numbers = re.findall("[0-9]+", actual_data.read())

for num in sample_numbers:
  sample_sum += int(num)

for num in actual_numbers:
  actual_sum += int(num)

print "Sample sum: " + str(sample_sum)
print "Actual sum: " + str(actual_sum)
