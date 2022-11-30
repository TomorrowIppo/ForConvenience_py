import os

file_path = '/Users/gimbyeongjin/Downloads/pascal to yolo classification digits/train_data/labels/val'
file_names = os.listdir(file_path)
file_names

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.txt'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1