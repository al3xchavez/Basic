print("hello_world")

#median function
def median(input):
  input.sort()
  length = len(input)-1              #length of string
  middle = math.floor(length/2)      #median value
  if length % 2 == 0:
    umiddle = middle + 1
    uppermiddle = input[umiddle]
    lowermiddle = input[middle]
    avgmiddle = (uppermiddle + lowermiddle) / 2
    return avgmiddle
  else:
    return input[middle]