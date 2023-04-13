from abc import ABC, abstractmethod
from copy import deepcopy
import random

mode_list = ["eng", "jpn"]


class AbstractDict(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def recite_words(self, n, mode):
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
                          're': 'れ', 'ro': 'ろ', 'wa': 'わ', 'wo': 'を', 'n': 'ん', 'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ',
                          'ge': 'げ', 'go': 'ご', 'za': 'ざ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ', 'da': 'だ',
                          'ji(di)': 'ぢ', 'zu(du)': 'づ', 'de': 'で', 'do': 'ど', 'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ',
                          'bo': 'ぼ', 'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ'}
        self.words_count = len(self.word_dict.keys())
        self.log_dir = "./logs/hiragana.log"

    def recite_words(self, n, mode):
        assert 0 < n <= self.words_count
        return self.__get_n_words__(n)

    def show_error_log(self):
        pass

    def __get_n_words__(self, n):
        keys_pick = random.sample(list(self.word_dict.keys()), n)
        words_pick = [self.word_dict.get(i) for i in keys_pick]
        return keys_pick, words_pick


class KatakanaDict(HiraganaDict):

    def __init__(self):
        super().__init__()
        self.word_dict = {'a': 'ア', 'i': 'イ', 'u': 'ウ', 'e': 'エ', 'o': 'オ', 'ka': 'カ', 'ki': 'キ', 'ku': 'ク', 'ke': 'ケ',
                          'ko': 'コ', 'sa': 'サ', 'shi': 'シ', 'su': 'ス', 'se': 'セ', 'so': 'ソ', 'ta': 'タ', 'chi': 'チ',
                          'tsu': 'ツ', 'te': 'テ', 'to': 'ト', 'na': 'ナ', 'ni': 'ニ', 'nu': 'ヌ', 'ne': 'ネ', 'no': 'ノ',
                          'ha': 'ハ', 'hi': 'ヒ', 'fu': 'フ', 'he': 'ヘ', 'ho': 'ホ', 'ma': 'マ', 'mi': 'ミ', 'mu': 'ム',
                          'me': 'メ', 'mo': 'モ', 'ya': 'ヤ', 'yu': 'ユ', 'yo': 'ヨ', 'ra': 'ラ', 'ri': 'リ', 'ru': 'ル',
                          're': 'レ', 'ro': 'ロ', 'wa': 'ワ', 'wo': 'ヲ', 'n': 'ン', 'ga': 'ガ', 'gi': 'ギ', 'gu': 'グ',
                          'ge': 'ゲ', 'go': 'ゴ', 'za': 'ザ', 'ji': 'ジ', 'zu': 'ズ', 'ze': 'ゼ', 'zo': 'ゾ', 'da': 'ダ',
                          'ji(di)': 'ヂ', 'zu(du)': 'ヅ', 'de': 'デ', 'do': 'ド', 'ba': 'バ', 'bi': 'ビ', 'bu': 'ブ',
                          'be': 'ベ', 'bo': 'ボ', 'pa': 'パ', 'pi': 'ピ', 'pu': 'プ', 'pe': 'ペ', 'po': 'ポ'}

        self.words_count = len(self.word_dict.keys())
        self.log_dir = "./logs/katakana.log"


class RomajiDict(AbstractDict):
    def __init__(self):
        self.hiragana = HiraganaDict()
        self.katakana = KatakanaDict()
        self.word_dict = dict_merge(self.hiragana.word_dict, self.katakana.word_dict)
        self.words_count = len(self.word_dict.keys())
        self.log_dir = "./logs/romaji.log"

    def recite_words(self, n, mode):
        assert 0 < n <= self.words_count
        eng_jpn = self.__get_n_words__(n)
        assert mode in mode_list  # ["eng","jpn","single_hira","single_kata"]
        if mode == "eng":

            return self.__dict_maker__(eng_jpn[0], eng_jpn[1])
        elif mode == "jpn":

            return self.__dict_maker__(eng_jpn[1], eng_jpn[0])
        else:
            pass
        return self.__get_n_words__(n)

    def show_error_log(self):
        pass

    def __get_n_words__(self, n):
        keys_pick = random.sample(list(self.word_dict.keys()), n)
        words_pick = [self.word_dict.get(i) for i in keys_pick]
        return keys_pick, words_pick

    def __dict_maker__(self, key_list, value_list):
        result_dict = {}
        for k, v in zip(key_list, value_list):
            result_dict.update({k: v})
        return result_dict
