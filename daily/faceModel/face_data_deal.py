import os
import numpy as np
import cv2

IMAGE_SIZE = 64  # 将图片大小设置为64*64


# 按照指定图像大小调整尺寸
def resize_image(image, height=IMAGE_SIZE, width=IMAGE_SIZE):
    top, bottom, left, right = (0, 0, 0, 0)
    if hasattr(images,'shape'):
        return
    # 获取图像尺寸
    h, w, _ = image.shape

    # 对于长宽不相等的图片，找到最长的一边
    longest_edge = max(h, w)

    # 计算短边需要增加多少像素宽度使其与长边等长
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass

        # RGB颜色
    BLACK = [0, 0, 0]

    # 给图像增加边界，是图片长、宽等长，cv2.BORDER_CONSTANT指定边界颜色由value指定
    constant = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK)
    # 将图像设置为灰度图
    constant = cv2.cvtColor(constant, cv2.COLOR_BGR2GRAY)

    # 调整图像大小并返回
    return cv2.resize(constant, (height, width))


# 读取训练数据
images = []
labels = []
clazz = {}

def read_path(path_name,label=None):
    for dir_item in os.listdir(path_name):
        # 从初始路径开始叠加，合并成可识别的操作路径
        full_path = os.path.abspath(os.path.join(path_name, dir_item))

        if os.path.isdir(full_path):  # 如果是文件夹，继续递归调用
            read_path(full_path,dir_item)
        else:  # 文件
            if clazz.get(label) is None:
                with open("./model/clazz.txt",'a') as f:
                    f.write(f"{label}\n")
                    clazz[str(label)] = label
            if dir_item.endswith('.jpg') or dir_item.endswith('.png'):
                image = cv2.imread(full_path)

                image = resize_image(image, IMAGE_SIZE, IMAGE_SIZE)

                images.append(image)
                labels.append(label)

    return images, labels


# 从指定路径读取训练数据
def load_dataset(path_name):
    with open('./model/clazz.txt',"w") as f:
        f.write("")
    images, labels = read_path(path_name)

    # 将输入的所有图片转成四维数组，尺寸为(图片数量*IMAGE_SIZE*IMAGE_SIZE*3)
    # 尺寸为 200*5* 64 * 64 * 3
    # 5个人 每个人200张 图片为64 * 64像素,一个像素3个颜色值(RGB)
    images = np.array(images)
    # 1 1 1
    # 1 1 4 4
    # 标注数据（采用onehot编码）（请注意必须从0开始算标签）
    temp = 0
    index =0
    tstr = labels[0]
    for label in labels:
        if label != tstr:
            tstr = label
            temp = temp + 1
        labels[index] = temp
        index = index + 1
    return images, labels


def get_user_number():
    with open('./model/clazz.txt','r',encoding='utf-8') as f:
        return f.read().splitlines()

if __name__ == '__main__':
    # images, labels = load_dataset("D:/data/face_mine")
    # print(images.shape)
    # print(len(labels))
    # print(labels)
    f = get_user_number()
    for (i,v) in f:
        print(i,v)