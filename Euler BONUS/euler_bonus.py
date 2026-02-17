import mpmath

min_val = 0
min_dist = 1

# Had to do quite a bit of research to solve this one.  The correct answer was one of the  Heegner numbers, hence the name of the puzzle
# For the positive values, the calculation was fairly straightforward.  I thought that's all there was so I used the Decimal class to get a high degree of precision
# This didn't work despite numerous trials.
# I then imported mpmath and used its decimal precision.  No improvement.  I had to do some research to learn that you can take the cosine of an imaginary value.
# This put negative values for n on the table.
# The function becomes cosh instead of cos (hyperbolic cosine function instead of cosine function)
# I had some additional difficulty with rounding these values and sorting out imaginary numbers.  I ended up getting it by trying -163 randomly.  There are only 9 Heegner numbers so the odds were decent.
# When I came back to my solution below, I swapped in floor and ceiling functions and that got it.  Rounding wasn't working.

mpmath.mp.dps = 50
for i in range(-1000,0):
	if mpmath.sqrt(abs(i))%1 != 0:
		val = mpmath.cosh(mpmath.pi*mpmath.sqrt(abs(i)))
		dist = min(val-mpmath.floor(val), mpmath.ceil(val)-val)
		if dist <= min_dist:
			min_dist = dist
			min_val = i
			print(min_val)
			print(f'For value {i}, the function outputs {val} and the distance of the real number to an integer is {dist}')


print(f'Minimum distance value is: {min_dist} and the winning integer is {min_val}')

		
