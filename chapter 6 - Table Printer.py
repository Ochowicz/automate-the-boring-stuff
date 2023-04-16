tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table():
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for element in tableData[i]:
            if len(element) > colWidths[i]:
                colWidths[i] = len(element)
    for j in range(len(tableData[0])):  # all elements of list have the same length
        for i in range(len(tableData)):
            print(tableData[i][j].rjust(colWidths[i]), end=' | ')
        print(end='\n')


print_table()
