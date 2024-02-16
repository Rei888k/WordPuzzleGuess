import random

# 拗音
# yohonList =["きゃ",     "きゅ",     "きょ",
#             "しゃ",     "しゅ",     "しょ",
#             "ちゃ",     "ちゅ",     "ちょ",
#             "にゃ",     "にゅ",     "にょ",
#             "ひゃ",     "ひゅ",     "ひょ",
#             "みゃ",     "みゅ",     "みょ",
#             "りゃ",     "りゅ",     "りょ",
#             "ぎゃ",     "ぎゅ",     "ぎょ",
#             "じゃ",     "じゅ",     "じょ",
#             "びゃ",     "びゅ",     "びょ",
#             "ぴゃ",     "ぴゅ",     "ぴょ"]


# ひらがなの範囲
hiragana = [chr(i) for i in range(12353, 12436)]

# ランダムなひらがな文字列を生成する関数
def GenerateRandomHiragana(length):
    return ''.join(random.choice(hiragana) for _ in range(length))