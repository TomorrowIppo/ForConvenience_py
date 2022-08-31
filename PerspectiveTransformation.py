import cv2
import numpy as np
import os

try:
    src = input('imgs 폴더 안에 있는 이미지를 이름.확장자 형식으로 입력하시오 : ')
    src_img = cv2.imread('imgs/' + src)
    COLOR = (255, 0, 255)
    THICKNESS = 3
    drawing = False
    point_list = []


    def mouse_handler(event, x, y, flags, param):
        global drawing
        dst_img = src_img.copy()

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            point_list.append((x, y))

        if drawing:
            prev_point = None
            for point in point_list:
                cv2.circle(dst_img, point, 15, COLOR, cv2.FILLED)
                if prev_point:
                    cv2.line(dst_img, prev_point, point, COLOR, THICKNESS, cv2.LINE_AA)
                prev_point = point
            next_point = (x, y)
            if len(point_list) == 4:
                show_result()
                next_point = point_list[0]
            cv2.line(dst_img, prev_point, next_point, COLOR, THICKNESS, cv2.LINE_AA)

        cv2.imshow('img', dst_img)


    def show_result():
        width, height = 640, 240
        src = np.float32(point_list)
        dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

        matrix = cv2.getPerspectiveTransform(src, dst)
        result = cv2.warpPerspective(src_img, matrix, (width, height))
        cv2.imshow('result', result)


    cv2.namedWindow('img')
    cv2.setMouseCallback('img', mouse_handler)
    cv2.imshow('img', src_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except cv2.error as e:
    print(f'에러 발생 : {e}')

print('프로그램 종료')