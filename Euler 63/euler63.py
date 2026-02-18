ct = 0
for i in range(50):
	j = 1
	while j**i < 10**i:
		if j**i >= 10**(i-1):
			print(f'{j}^{i} = {j**i}')
			ct += 1
		j+=1

print(f"Final count = {ct}")