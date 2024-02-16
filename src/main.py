
from checkInput import checkInput
from generateWord import GenerateRandomHiragana

class CharInfo:
    def __init__(self, char, color = "\033[0m"):
        self.char = char
        self.color = color

# 簡易確認用のコンソールモード
def consoleMode():
    # correctWord = "こんにちは"
    correctWordLen = 5
    correctWord = GenerateRandomHiragana(correctWordLen)
    correctWordArray = (correctWord)

    # 改行
    print()

    roopCount = 1
    while True:
        inputWord = input("文字を入力してね\n")

        # 文字数をチェック
        if not checkInput(inputWord):
            continue
            
        # 文字の正解チェック
        inputWordArray = []
        for c in inputWord:
            inputWordArray.append(CharInfo(c))

        # 文字と位置が一致するものをチェック
        for i, charInfo in enumerate(inputWordArray):
            if charInfo.char == correctWord[i]:
                inputWordArray[i].color = "\033[32m" # 緑
            else:
                inputWordArray[i].color = "\033[37m" # 白
        
        # for i, charInfo in enumerate(inputWordArray):
        #     print(f"{charInfo.color}{charInfo.char}\033[0m", end="")
        # print()

        tmpCorrectWordArray = []
        for i, char in enumerate(correctWordArray):
            # 緑文字（正解文字）はあらかじめ別の文字に置き換えておく
            if inputWordArray[i].color == "\033[32m":
                tmpCorrectWordArray.append("")
            else:
                tmpCorrectWordArray.append(char)
        # 位置不一致、文字一致するものをチェック
        for i, charInfo in enumerate(inputWordArray):
            if charInfo.char in tmpCorrectWordArray:
                inputWordArray[i].color = "\033[33m" # 黄
        
        
        # for i, charInfo in enumerate(inputWordArray):
        #     print(f"{charInfo.color}{charInfo.char}\033[0m", end="")
        # print()

        if all(charInfo.color == "\033[32m" for charInfo in inputWordArray):
            # 全文字完全一致
            print("{0}回目、結果：".format(roopCount), end="")
            for i, charInfo in enumerate(inputWordArray):
                print(f"{charInfo.color}{charInfo.char}\033[0m", end="")
            # 改行
            print()

            break
        else:
            print("{0}回目、結果：".format(roopCount), end="")
            for i, charInfo in enumerate(inputWordArray):
                print(f"{charInfo.color}{charInfo.char}\033[0m", end="")
            # 改行
            print()
        
        roopCount += 1
    
    print("---------------")
    print("クリア～～～")
    print("正解は：", correctWord)

def main():
    consoleMode()


# メイン関数
if __name__ == '__main__':
    # 引数を受け取る
    # arg = parser()
    main()
