# -*- coding: utf-8 -*-
import os


class ImageRename():
    """
    图片重命名
    """
    def __init__(self,path):
        # 换成自己图片集所在路径
        self.path = path

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)

        i = 1

        for item in filelist:
            # 如果是png就把.jpg改成.png
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                # 自己可以更改0的个数
                dst = os.path.join(os.path.abspath(self.path), '0000' + format(str(i), '0>3s') + '.jpg')
                os.rename(src, dst)
                print('converting %s to %s ...' % (src, dst))
                i = i + 1
        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    newname = ImageRename(r'D:/data/face_mine')
    newname.rename()