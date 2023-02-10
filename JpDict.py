from abc import ABC, abstractmethod
from copy import deepcopy
import random


class AbstractDict(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def recite_words(self, n):
        pass

    @abstractmethod
    def show_error_log(self):
        pass


def dict_merge(dict1, dict2):
    new_dict = deepcopy(dict1)
    for i, j in zip(dict1, dict2):
        assert i == j
        new_dict.update({i: (dict1.get(i), dict2.get(j))})
    return new_dict


class HiraganaDict(AbstractDict):

    def __init__(self):
        self.word_dict = {'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お', 'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け',
                          'ko': 'こ', 'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ', 'ta': 'た', 'chi': 'ち',
                          'tsu': 'つ', 'te': 'て', 'to': 'と', 'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
                          'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ', 'ma': 'ま', 'mi': 'み', 'mu': 'む',
                          'me': 'め', 'mo': 'も', 'ya': 'や', 'yu': 'ゆ', 'yo': 'よ', 'ra': 'ら', 'ri': 'り', 'ru': 'る',
                          're': 'れ', 'ro': 'ろ', 'wa': 'わ', 'wo': 'を', 'n': 'ん'}
        self.words_count = len(self.word_dict.keys())
        self.log_dir = "./logs/hiragana.log"

    def recite_words(self, n):
        assert 0 < n <= self.words_count
        return self.__get_n_words__(n)

    def show_error_log(self):
        pass

    def __get_n_words__(self, n):
        keys_pick = random.sample(list(self.word_dict.keys()), n)
        words_pick = [self.word_dict.get(i) for i in keys_pick]
        return keys_pick, words_pick


class KatakanaDict(AbstractDict):

    def __init__(self):
        self.word_dict = {'a': 'ア', 'i': 'イ', 'u': 'ウ', 'e': 'エ', 'o': 'オ', 'ka': 'カ', 'ki': 'キ', 'ku': 'ク', 'ke': 'ケ',
                          'ko': 'コ', 'sa': 'サ', 'shi': 'シ', 'su': 'ス', 'se': 'セ', 'so': 'ソ', 'ta': 'タ', 'chi': 'チ',
                          'tsu': 'ツ', 'te': 'テ', 'to': 'ト', 'na': 'ナ', 'ni': 'ニ', 'nu': 'ヌ', 'ne': 'ネ', 'no': 'ノ',
                          'ha': 'ハ', 'hi': 'ヒ', 'fu': 'フ', 'he': 'ヘ', 'ho': 'ホ', 'ma': 'マ', 'mi': 'ミ', 'mu': 'ム',
                          'me': 'メ', 'mo': 'モ', 'ya': 'ヤ', 'yu': 'ユ', 'yo': 'ヨ', 'ra': 'ラ', 'ri': 'リ', 'ru': 'ル',
                          're': 'レ', 'ro': 'ロ', 'wa': 'ワ', 'wo': 'ヲ', 'n': 'ン'}

        self.words_count = len(self.word_dict.keys())
        self.log_dir = "./logs/katakana.log"

    def recite_words(self, n):
        assert 0 < n <= self.words_count
        return self.__get_n_words__(n)

    def show_error_log(self):
        pass

    def __get_n_words__(self, n):
        keys_pick = random.sample(list(self.word_dict.keys()), n)
        words_pick = [self.word_dict.get(i) for i in keys_pick]
        return keys_pick, words_pick




class RomajiDict(AbstractDict):
    def __init__(self):
        self.hiragana = HiraganaDict()
        self.katakana = KatakanaDict()
        self.word_dict = dict_merge(self.hiragana.word_dict , self.katakana.word_dict)

    def recite_words(self, n):
        pass

    def show_error_log(self):
        pass

    def __get_n_words__(self, n):
        keys_pick = random.sample(list(self.word_dict.keys()), n)
        words_pick = [self.word_dict.get(i) for i in keys_pick]
        return keys_pick, words_pick
