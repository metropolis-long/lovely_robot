import jieba
import os
import utils

__my_words__ = []


def split_words_dir(dir_path):
    dir = os.listdir(dir_path)
    today = utils.get_today_str()
    for d in dir:
        full_path = os.path.abspath(os.path.join(dir_path, d))
        if full_path.find(today) < 0 and os.path.isdir(full_path):
            split_words_dir(full_path)
        else:
            ind = d.index(today)
            word = d[ind+len(today):]
            splits = jieba.cut(word)
            __my_words__.append(splits)


def get_word_split_dir():
    split_words_dir(r"D:/data")
    return __my_words__


if __name__ == "__main__":
    for w in get_word_split_dir():
        print(", ".join(w))
    print('split words over！')


