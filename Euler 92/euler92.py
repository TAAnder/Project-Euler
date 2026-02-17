from collections import defaultdict

found = defaultdict(int)
def main():
	ct = 0
	for i in range(1,10000001):
		if sum_sq_digs(i):
			found[i] = 89
			ct +=1
		else:
			found[i] = 1
	print(ct)



def sum_sq_digs(num) -> bool:
	if num == 1 or found[num] ==1:
		return False
	elif num == 89 or found[num]==89:
		return True
	else:
		new_num = 0
		while num:
			new_num += pow((num%10),2)
			num //= 10
		return sum_sq_digs(new_num)

if __name__ == '__main__':
	main()