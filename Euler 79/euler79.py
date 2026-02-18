
higherthan = {}
lowerthan = {}

# file cleanup -- opening a text file and splitting the two 'new line' segments into a dna strand and a target pattern
with open("Euler 79/0079_keylog.txt",mode='r') as logs:
	contents = logs.read()
data = contents.split()

for item in data:
	if item[0] not in higherthan:
		higherthan[item[0]] = set()
	higherthan[item[0]].add(item[1])
	higherthan[item[0]].add(item[2])
	if item[1] not in higherthan:
		higherthan[item[1]] = set()
	if item[1] not in lowerthan:
		lowerthan[item[1]] = set()
	higherthan[item[1]].add(item[2])
	lowerthan[item[1]].add(item[0])
	if item[2] not in lowerthan:
		lowerthan[item[2]] = set()
	lowerthan[item[2]].add(item[1])
	lowerthan[item[2]].add(item[0])
	

# It was easy enough to do it manually with one of these dictionaries.  I was wondering if I'd need to find duplicate digits... turns out no
print('higherthan')
print(higherthan)

print("lowerthan")
print(lowerthan)


73162890