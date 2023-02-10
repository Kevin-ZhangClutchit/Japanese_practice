# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import JpDict

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a="アイウエオ" \
    "カキクケコ" \
    "サシスセソ" \
    "タチツテト" \
    "ナニヌネノ" \
    "ハヒフヘホ" \
    "マミムメモ" \
    "ヤユヨ" \
    "ラリルレロ" \
    "ワヲン"
    b=["a","i","u","e","o","ka","ki","ku","ke","ko","sa","shi","su","se","so"
       ,"ta","chi","tsu","te","to","na","ni","nu","ne","no","ha","hi","fu","he","ho",
       "ma","mi","mu","me","mo","ya","yu","yo","ra","ri","ru","re","ro","wa","wo","n"]

    c=JpDict.HiraganaDict()
    d=JpDict.KatakanaDict()
    print(d.recite_words(3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
