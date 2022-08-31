import os

mon = input('월을 입력 하세요 예)8 : ')
end_day = int(input('월의 마지막 숫자를 입력하세요 예)31 : '))
start = input('1일의 요일은 무엇인가요? 예)월 : ')

day = {'월': 0, '화': 1, '수': 2, '목': 3, '금': 4, '토': 5, '일': 6}
day2 = {0: '월', 1: '화', 2: '수', 3: '목', 4: '금', 5: '토', 6: '일'}
count = day[start]

for i in range(1, end_day + 1):

    if len(str(i)) == 1:
        i = str(i)
        i = '0' + i
    else:
        i = str(i)

    msg = mon + '월' + i + '일(' + start + ')'

    count = (count + 1) % 7
    start = day2[count]

    # print (msg)
    os.mkdir(msg)

print('폴더 생성 완료')