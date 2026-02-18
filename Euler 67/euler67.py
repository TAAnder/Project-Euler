# Set up a list of lists.  
# Index mapping: the ith index maps onto either the ith or i+th index of the following row.

# Strategy:
# Set up an empty list the size of the following row.  Run through the current row. 
# Add the current values from the current row to empty cells in the upcoming row.  For non-empty cells, if greater, replace, otherwise skip.
# 3 -- add to index 0; 3 -- add to index 1;
# Process the queue 

sample = [[3], 
          [7, 4], 
          [2, 4, 6], 
          [8, 5, 9, 3]]


with open("/home/snakemistake/repos/Project-Euler/Euler 67/0067_triangle.txt",mode='r') as f:
	contents = f.read()
triangle = contents.split('\n')

for i in range(len(triangle)):
    copy = triangle[i]
    copy = copy.split(' ')
    new = []
    for item in copy:
        new.append(int(item))
    triangle[i] = new


def process_matrix(matrix):
    for j in range(len(matrix)):
        if j == len(matrix)-1:
            return max(matrix[j])
        new_row = []
        for i in range(len(matrix[j])):
            if i ==0:
                new_row.append(matrix[j][i])
                new_row.append(matrix[j][i])
            else:
                new_row[i] = max(matrix[j][i], new_row[i])
                new_row.append(matrix[j][i])
        for i in range(len(new_row)):
            matrix[j+1][i] += new_row[i]

# print(process_matrix(sample))

print(process_matrix(triangle))

    