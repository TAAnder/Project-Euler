

# Need to find the last 10 digits of 28433 x 2^7830457 + 1.

# The power of two could be represented in bits: 1 + 783546 zeroes + 1

# 28433 could also be represented in bits.


# Multiplying the bits should be easy -- We should end with 1 + a bunch of zeroes + 28433 in bits.  The problem is... I'm not super well versed in ways to divide by 10 in bits

# Alternative strategy -- Keep track of only the last 10 digits.  Multiply by 2 7830457 times.  
# Floor divide by 10000000000 at each step to keep the data tracking manageable.
# Then add 1
# Then multiply by 38433.
# Floor dividbe by 10000000000 again.

def main():
	print(find_last_10_prime())

def find_last_10_prime():
	ans = 1
	for i in range(7830457):
		ans *= 2
		ans = ans%10000000000
	ans *= 28433
	ans += 1
	return ans %10000000000


if __name__ == "__main__":
	main()
