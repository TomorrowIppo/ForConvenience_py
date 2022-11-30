d_matrix = [
    [5,   4,   4,   5,   4,   3,   3,   4,   3,   2,   2,   3,   2,   1,   1,   2],
    [2,   3,   4,   5,   1,   2,   3,   4,   1,   2,   3,   4,   2,   3,   4,   5],
    [2,   1,   1,   2,   3,   2,   2,   3,   4,   3,   3,   4,   5,   4,   4,   5]
]

fc_matrix = [
    [150*5,   25*5,   88*5,   3],
    [60*7,   200*3,   150*6,   5],
    [96*4,   15*7,   85*9,   2],
    [175*15,   135*8,   90*12,   6]
]


def show_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()


def reverse_matrix(matrix):
    matrix_len = len(matrix[0])
    #new_matrix = []

    row_matrix = []
    for i in range(matrix_len):
        col_matrix = []
        for j in range(len(matrix)):
            col_matrix.append(matrix[j][i])
        row_matrix.append(col_matrix)

    return row_matrix


def stp(fc_matrix, d_matrix):
    #result = []
    m = 4
    n = 16
    p = 3

    row_matrix = []
    for i in range(m):
        col_matrix = []
        for j in range(n):
            temp_sum = 0
            for k in range(p):
                temp_sum += fc_matrix[k][i] * d_matrix[j][k]
                #print(temp_sum)
            temp_sum = temp_sum / fc_matrix[3][i]
            #temp_sum = temp_sum * x[i][j]
            col_matrix.append(temp_sum)
        row_matrix.append(col_matrix)
    #result.append(row_matrix)

    return row_matrix


fc_matrix = reverse_matrix(fc_matrix)
d_matrix = reverse_matrix(d_matrix)
show_matrix(fc_matrix)
print('#----------------------------------------------------#')
show_matrix(stp(fc_matrix=fc_matrix, d_matrix=d_matrix))
#print(fc_matrix)
#print(d_matrix)


