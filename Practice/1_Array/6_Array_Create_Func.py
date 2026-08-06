from numpy import *

# linspace(): Method in numpy module is used to create an array of evenly spaced numbers over a specified range.
# The linspace() method takes three parameters: start, stop, and num

val = linspace(1, 10, 5) # start=1, stop=10, num=5
print(val)
# Output: [ 1 3.25 5.5 7.75 10 ]

# arange(): Method in numpy module is used to create an array of evenly spaced numbers over a specified range.
# The arange() method takes three parameters: start, stop, and step

val = arange(1, 10, 2) # start=1, stop=10, step=2
print(val)
# Output: [1 3 5 7 9]

# logspace(): Method in numpy module is used to create an array of evenly spaced numbers over a specified range.
# The logspace() method takes three parameters: start, stop, and num

val = logspace(1, 10, 5) # start=1, stop=10, num=5
print(val)
# Output: [1.00000000e+01 1.77827941e+02 3.16227766e+03 5.62341325e+04 1.00000000e+06]

# zeros(): Method in numpy module is used to create an array of zeros.
val = zeros(5) # create an array of 5 zeros
print(val)
# Output: [0. 0. 0. 0. 0.]