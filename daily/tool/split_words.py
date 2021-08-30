import jieba
import os
import utils

__my_words__ = []
__my_ones_words__ = []

def split_words_dir(dir_path):
    dir = os.listdir(dir_path)
    today = utils.get_today_str()
    for d in dir:
        full_path = os.path.abspath(os.path.join(dir_path, d))
        # 是目录，并且包含今天日期
        if full_path.find(today) < 0 and os.path.isdir(full_path):
            split_words_dir(full_path)
        elif os.path.isdir(full_path):
            ind = d.index(today)
            word = d[ind+len(today):]
            splits = jieba.cut(word)
            __my_words__.append(splits)
        else:
            pass

def get_word_split_dir():
    split_words_dir(r"D:/data")
    return __my_words__


def split_every_word_dir(dir_path):
    dir = os.listdir(dir_path)
    today = utils.get_today_str()
    for d in dir:
        full_path = os.path.abspath(os.path.join(dir_path, d))
        # 是目录，并且包含今天日期
        if full_path.find(today) < 0 and os.path.isdir(full_path):
            split_every_word_dir(full_path)
        elif os.path.isdir(full_path):
            ind = d.index(today)
            word = d[ind + len(today):]
            splits = ",".join(word)
            __my_ones_words__.append(splits)
        else:
            pass


def get_split_every_word_dir():
    split_every_word_dir(r"D:/data")
    return __my_ones_words__


if __name__ == "__main__":
    for w in get_word_split_dir():
        print(",".join(w))
    for w in get_split_every_word_dir():
        print(w)
    print('split words over！')


