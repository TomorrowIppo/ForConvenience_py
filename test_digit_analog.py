import os

diagonal = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1]
]


# try:
#     while True:
#         for i in diagonal:
#             for j in i:
#                 print(j, end=' ')
#             print()
# except KeyboardInterrupt:
#     print('KeyboardInterrupt 발생, 프로그램 종료')


# 8x8 초기화 (0으로 채워짐)
diagonal_stack = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

try:
    idx = 0
    count = 0
    comand = 'clear'
    while True:
        del diagonal_stack[0]
        if idx > 16:
            idx = 0
        diagonal_stack.append(diagonal[idx])
        idx += 1
        for i in diagonal_stack:
            for j in i:
                print(j, end=' ')
            print()
        os.system(command=comand)

except KeyboardInterrupt:
    print('foo')

