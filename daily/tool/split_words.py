import jieba
import os
import utils


class SplitWords():
    def __init__(self, path=None):
        self.__my_words__ = []
        self.__my_ones_words__ = []
        self.path = path

    def split_words_dir(self, dir_path):
        dir = os.listdir(dir_path)
        today = utils.get_today_str()
        for d in dir:
            full_path = os.path.abspath(os.path.join(dir_path, d))
            # path is a dir and it doesn't contain today date
            if full_path.find(today) < 0 and os.path.isdir(full_path):
                self.split_words_dir(full_path)
            elif os.path.isdir(full_path):
                print(d)
                ind = d.index(today)
                word = d[ind + len(today):]
                splits = jieba.cut(word)
                self.__my_words__.append(splits)
            else:
                pass

    def get_word_split_dir(self, path):
        if path is None:
            path = self.path
        self.split_words_dir(path)
        return self.__my_words__

    def split_every_word_dir(self, dir_path):
        dir = os.listdir(dir_path)
        today = utils.get_today_str()
        for d in dir:
            full_path = os.path.abspath(os.path.join(dir_path, d))
            # path is a dir and it doesn't contain today date
            if full_path.find(today) < 0 and os.path.isdir(full_path):
                self.split_every_word_dir(full_path)
            elif os.path.isdir(full_path):
                print(d)
                ind = d.index(today)
                word = d[ind + len(today):]
                splits = ",".join(word)
                self.__my_ones_words__.append(splits)
            else: # path is not a dir
                pass

    def get_split_every_word_dir(self, path=None) -> []:
        """
        return dirs's every word that a str will be split ',' for a dir
        example: /data/20210101每个人都有爱好  this will be return a str '每,个,人,都,有,爱,好'
        :param path:
        :return:
        """
        if path is None:
            path = self.path
        self.split_every_word_dir(path)
        return self.__my_ones_words__


if __name__ == "__main__":
    sw = SplitWords()
    for w in sw.get_word_split_dir(r"D:/data"):
        print(",".join(w))
    for w in sw.get_split_every_word_dir(r"D:/data"):
        print(w)
    print('split words over！')
