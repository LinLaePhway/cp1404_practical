# What did you see on line 1?
# Output: 14
# Line 1 prints a random integer between 5(inclusive) and 20(inclusive).
# What was the smallest number you could have seen, what was the largest?
# The smallest number that could have been seen is 5, and the largest number is 20.
#
# What did you see on line 2?
# Output: 9
# Line 2 prints a random integer from the range(3, 10) with a step of 2. 10 is exclusive.
# What was the smallest number you could have seen, what was the largest?
# The smallest number that could have been seen is 3, and the largest number is 9.
# Could line 2 have produced a 4?
# No, line 2 could not produce a 4 because the step value is 2, so starting from 3, the possible values are 3, 5, 7, and 9.
#
# What did you see on line 3?
# Output: 3.444352446266845
# Line 3 prints a random floating-point number between 2.5(inclusive) and 5.5(inclusive).
# What was the smallest number you could have seen, what was the largest?
# The smallest number that could have been seen is 2.5, and the largest number is 5.5.

"""Write code, not a comment, to produce a random number between 1 and 100 inclusive."""

import random

random_number = random.randint(1, 100)
print(random_number)