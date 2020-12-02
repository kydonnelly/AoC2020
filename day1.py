#!/usr/bin/python3

# Target sum of numbers given in prompt
target_sum = 2020

# Read input file
f = open('day1_input.txt', 'r')
lines = f.readlines()
inputs = [int(l.strip()) for l in lines]
f.close()

# Make a set of the pairs needed for each input value: O(N)
differences = [target_sum - i for i in inputs]

# Find all of the input values that have a pair: O(N)
sum_pairs = [i for i in inputs if i in differences]

# Print out the first pair, expected to have len == 2 but not worth validating
if len(sum_pairs) == 0:
   print("No pair found that adds to " + str(target_sum))
else:
   first_pair = sum_pairs[0]
   print("Found pair for "  + str(first_pair) + " with product " + str(first_pair * (target_sum - first_pair)))

