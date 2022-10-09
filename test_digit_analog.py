import os
import platform
import time

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
    command = ''
    _os = platform.system()
    if _os == 'Windows':
        command = 'cls'
    elif _os == 'Darwin':
        command = 'clear'
    else:
        pass

    while True:
        del diagonal_stack[0]
        if idx == 16:
            idx = 0
        diagonal_stack.append(diagonal[idx])
        idx += 1
        for i in diagonal_stack:
            for j in i:
                _str = ''
                if j == 1:
                    _str = '\033[91m' + '1' + '\033[37m'
                elif j == 0:
                    _str = '\033[97m' + '0' + '\033[37m'

                print(_str, end=' ')
            print()
        time.sleep(0.1)
        os.system(command=command)


except KeyboardInterrupt:
    print('foo')

