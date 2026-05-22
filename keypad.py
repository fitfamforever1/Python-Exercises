# Replicating a phone keypad using nested loops

# Variables to hold the rows of the keypad
row1 = ('1', '2', '3')
row2 = ('4', '5', '6')
row3 = ('7', '8', '9')
row4 = ('*', '0', '#')

# Grouping the rows together in a tuple
row = (row1, row2, row3, row4)

# Printing the keypad using nested loops
for x in row:
    for y in x:
        print(y, end=' ')
    print()
