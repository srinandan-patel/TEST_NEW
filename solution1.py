A = [[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12],
	[13, 14, 15, 16]]
	
## print nth column
n = int(input("Enter column number to be printed:"))
col_num = n - 1
column = []
for row in A:
	column.append(row[col_num])

print("3rd column : ", column)

##print 2nd row
n = int(input("Enter Row number to be printed:"))
row_num = n - 1
print("2nd row : ", A[row_num])

## print quadrant at n,m position

row_num = n - 1
col_num = m - 1

print(A[n][m])
