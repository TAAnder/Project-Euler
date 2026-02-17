# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,<br> where each “_” is a single digit.

# Brainstorm -- find the minimum and maximum for the correct number of digits.
# 19 digits total.  Between 10^19 and 10^20
# So the integer must be between 10^9 and 10^10
# Needs to be a multiple of 10.
# Even with those constraints that's way too many candidates to iterate through -- it's 
# 10**9(10-1) = 9000000000 numbers

# Another way to think about it is 9 blanks with 10 choices each.  That yields 10^9 choices for the perfect square.

# The target could be broken down like so:
# 1*10^18 + 2*10^16 + 3*10^14 + 4*10^12 + 5*10^10 + 6*10^8 + 7*10^6 + 8*10^4 + 9*10^2 + 0*10^0
# + a*10^17 + b*10^15 + c*10^13 + d*10*15 + e*10^13 + d*10^11 + f*10^9 + g*10^7 + h*10^5 + i*10^3 + j*10^1
#

# First digit is a 0. Second digit is a 3 or a 7.

# The third digit is a 3 5 or 8 --- actually this is not seeming to work

# The only number I can find that gets the 0 9 8 and 7 correct is 4170

# The only number that works for the 0 9 8 7 and 6 correct are: 25830 and 40830

# The only number that works for the 0 9 8 7 6 and 5 is 742070

# The two numbers that work for the 0 9 8 7 6 and 5 and 4 are 8022070 and 2204470

# The two numbers that work for the 0 9 8 7 6 5 4 and 3 are 79525830 and 73312070

# The numbers that work for the 0 9 8 7 6 5 4 3 and 2 are 156025830, 348417070, and 470525830
# for i in range(10,100,10):
#     print(f'i + 0 squared = {(i+0)**2}')


# There's a little luck with this solution.  Last two digits have to be either 30 or 70.  Tried 70 and it works.  Count by 100s until answer found
for j in range(100,10000000000,100):
    i = j + 70
    if (i%10 == 0 and (i**2) // 100)%10 == 9 and (i**2 // 10000)%10 == 8 and (i**2 // 1000000)%10 == 7 and (i**2 // 100000000)%10 == 6 and (i**2 // 10000000000)%10 == 5 and (i**2 // 1000000000000)%10 == 4 and (i**2 // 100000000000000)%10 == 3 and (i**2 // 10000000000000000)%10 == 2 and (i**2 // 1000000000000000000)%10 == 1:
        print(i)
        print(i**2)
    # print(f'{i} + 30 squared = {(i+30)**2}. {i} +70 squared = {(i + 70)**2}')

# for i in range(1000,10000,1000):
#     print(f'i + 430 squared = {(i+430)**2}. i + 530 squred = {(i + 530)**2} and i + 830 squared = {(i+830)**2}')