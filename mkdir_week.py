import os

week = int(input('몆 주차까지 있나요? : '))

for i in range(1, week + 1):
    if len(str(i)) == 1:
        i = str(i)
        i = '0' + i
    else:
        i = str(i)

    msg = f'{i}주차'

    # print(msg)
    os.mkdir(msg)