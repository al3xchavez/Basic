print("hello_world")

#mean function
def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)
