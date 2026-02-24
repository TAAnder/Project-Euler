cube_dict = {}


# Iterate through a bunch of numbers, calculate their cubes and then convert to a code.
# The codes are basically digit counts -- the place of the digit refers to its value (0-9).  The value of the digit refers to how many there are
# This only works to count up to 9 instances of a digit.  Could be swapped to hexadecimal or base 36 if we needed to track larger counts.
for i in range(1,100000):
    cube = i**3
    code = ""
    digs = [0,0,0,0,0,0,0,0,0,0]
    while cube >0:
        dig = cube%10
        digs[dig] +=1
        cube //= 10
    for d in digs:
        # right here could check for values of d larger than 10 and convert to A-Z...
        code += str(d)
    if code in cube_dict:
        cube_dict[code].append(i)
    else:
        cube_dict[code] = [i]

# Run through the cube dictionary and find the codes for which 5 cubes all mapped to the same value.  
# Turns out my search was overkill -- Found a bunch of cubes that all map to permutations of the same digits!
for k in cube_dict:
    if len(cube_dict[k]) > 4:
        print(cube_dict[k])

# Print the answer - the lowest value from these sets.
print(5027**3)