import os
import sys
import kivy
from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.factory import Factory
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Line

from checkInput import checkInput
from generateWord import GenerateRandomHiragana
# Builder.load_file("kv/kvMain.kv")
# Builder.load_file("kvMain.kv")

RED = [1, 0, 0, 1]
GREEN = [0, 1, 0, 1]
BLUE = [0, 0, 1, 1]
YELLOW = [1, 1, 0, 1]
WHITE = [1, 1, 1, 1]

class KvCharInfo:
    def __init__(self, char, color = WHITE):
        self.char = char
        self.color = color

# リザルト画面
class ResultScreen(Screen):
    pass

# ホーム画面
class HomeScreen(Screen):
    pass

# 遊び方画面
class HowToPlayScreen(Screen):
    pass

# 五十音リスト
kanaList = ['　', 'わ', 'ら', 'や', 'ま', 'は', 'な', 'た', 'さ', 'か', 'あ',
            '　', '　', 'り', '　', 'み', 'ひ', 'に', 'ち', 'し', 'き', 'い',
            '決定', 'を', 'る', 'ゆ', 'む', 'ふ', 'ぬ', 'つ', 'す', 'く', 'う',
            '削除', '　', 'れ', '　', 'め', 'へ', 'ね', 'て', 'せ', 'け', 'え',
            '切替', 'ん', 'ろ', 'よ', 'も', 'ほ', 'の', 'と', 'そ', 'こ', 'お' ]
# 濁音、半濁音リスト
dakuList = ['　', 'ぱ', 'ば', 'だ', 'ざ', 'が',
            '　', 'ぴ', 'び', 'ぢ', 'じ', 'ぎ',
            '決定', 'ぷ', 'ぶ', 'づ', 'ず', 'ぐ',
            '削除', 'ぺ', 'べ', 'で', 'ぜ', 'げ',
            '切替', 'ぽ', 'ぼ', 'ど', 'ぞ', 'ご']

# ゲーム画面
class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        # 現在フォーカスしている行
        self.focusLine = 1
        # 
        self.targetLabel = 1
        # 問題の文字数
        self.correctWordLen = 5
        # 正解文字列
        self.correctWord = "こんにちは"
        self.correctWordArray = (self.correctWord)
        # 入力文字
        self.inputWord = ""
        # 確認回数
        self.roopCount = 1

    def on_pre_leave(self):
        # self.clear_widgets()
        for child in self.ids.scrollview.children:
            self.ids.scrollview.remove_widget(child)
        

    def on_pre_enter(self, *args):
        # 初期値設定
        self.focusLine = 1
        self.targetLabel = 1
        self.correctWordLen = 5
        # self.correctWord = "こんにちは"
        self.correctWord = GenerateRandomHiragana(self.correctWordLen)
        self.correctWordArray = (self.correctWord)
        self.inputWord = ""
        self.roopCount = 1

        # 五十音表を追加
        kana_grid = GridLayout(cols=11, rows=5, size_hint=(0.4, 0.4), pos_hint={"center_x": 0.5, "center_y": 0.25})
        kana_grid.name = "五十音表"
        for char in kanaList:
            btn = Factory.KanaButton(text=char)
            if char == '切替':
                btn.bind(on_press=self.change_button)
            elif char == '削除':
                btn.bind(on_press=self.delete_label)
            elif char == '決定':
                btn.bind(on_press=self.decide_button)
            elif char == '　':
                pass
            else:
                btn.bind(on_press=self.print_button)
            kana_grid.add_widget(btn)

        self.add_widget(kana_grid)

        # 入力ラベルを追加
        input_grid = GridLayout(cols=1, size_hint=(1, None), height=300, pos_hint={"center_x": 0.5, "center_y": 0.5})
        input_grid.bind(minimum_height=input_grid.setter('height'))
        input_grid.name = "入力ラベル"

        box_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50, pos_hint={"center_x": 0.5, "center_y": 0.5}, spacing=5, padding=5)
        for i in range(5):
            label = Factory.InputLabel(pos_hint={"center_x": 0.5, "center_y": 0.5})
            label.name = "{0}_{1}".format(self.focusLine, i+1)
            box_layout.add_widget(label)
        # ゲーム画面に追加
        # self.add_widget(input_grid)
        input_grid.add_widget(box_layout)
        self.ids.scrollview.add_widget(input_grid)

    def print_button(self, instance):
        self.input_label(instance.text)

    def change_button(self, instance):
        if instance.parent.name == "五十音表":
            # 五十音表削除
            self.remove_widget(instance.parent)

            # 濁音、半濁音表追加
            daku_grid = GridLayout(cols=6, rows=5, size_hint_y=None, size_hint_x=None, size_hint=(0.4, 0.4), pos_hint={"center_x": 0.5, "center_y": 0.25})
            daku_grid.name = "濁音半濁音表"
            for char in dakuList:
                btn = Factory.KanaButton(text=char)
                if char == '切替':
                    btn.bind(on_press=self.change_button)
                elif char == '削除':
                    btn.bind(on_press=self.delete_label)
                elif char == '決定':
                    btn.bind(on_press=self.decide_button)
                elif char == '　':
                    pass
                else:
                    btn.bind(on_press=self.print_button)
                daku_grid.add_widget(btn)

            self.add_widget(daku_grid)
        else:
            # 濁音、半濁音表削除
            self.remove_widget(instance.parent)
            
            # 五十音表を追加
            kana_grid = GridLayout(cols=11, rows=5, size_hint_y=None, size_hint_x=None, size_hint=(0.4, 0.4), pos_hint={"center_x": 0.5, "center_y": 0.25})
            kana_grid.name = "五十音表"
            for char in kanaList:
                btn = Factory.KanaButton(text=char)
                if char == '切替':
                    btn.bind(on_press=self.change_button)
                elif char == '削除':
                    btn.bind(on_press=self.delete_label)
                elif char == '決定':
                    btn.bind(on_press=self.decide_button)
                elif char == '　':
                    pass
                else:
                    btn.bind(on_press=self.print_button)
                kana_grid.add_widget(btn)

            self.add_widget(kana_grid)
        
    def input_label(self, char):
        for child in self.ids.scrollview.children:
            for grandChild in child.children:
                for greatGrandChild in grandChild.children:
                    # 現在フォーカスしている行であるかチェック
                    if "{0}_".format(self.focusLine) in greatGrandChild.name:
                        if greatGrandChild.name == "{0}_{1}".format(self.focusLine, self.targetLabel) and greatGrandChild.text == "":
                            greatGrandChild.text = char
                            self.inputWord += greatGrandChild.text
                            self.targetLabel += 1
                            break
    
    def delete_label(self, instance):
        for child in self.ids.scrollview.children:
            for grandChild in child.children:
                for greatGrandChild in grandChild.children:
                    # 現在フォーカスしている行であるかチェック
                    if "{0}_".format(self.focusLine) in greatGrandChild.name:
                        if greatGrandChild.name == "{0}_{1}".format(self.focusLine, self.targetLabel - 1) and greatGrandChild.text != "":
                            greatGrandChild.text = ""
                            self.inputWord = self.inputWord[:-1]
                            self.targetLabel -= 1
                            break
    
    def decide_button(self, instance):
        print("決定ボタン押下", self.inputWord)
        # 文字数をチェック
        ret, message = checkInput(self.inputWord)
        if ret:
            # 文字の正解チェック
            inputWordArray = []
            for c in self.inputWord:
                inputWordArray.append(KvCharInfo(c))
            
            # 文字と位置が一致するものをチェック
            for i, charInfo in enumerate(inputWordArray):
                if charInfo.char == self.correctWord[i]:
                    print(charInfo.char)
                    inputWordArray[i].color = GREEN
                else:
                    pass
                    inputWordArray[i].color = WHITE
                
            tmpCorrectWordArray = []
            for i, char in enumerate(self.correctWordArray):
                # 緑文字（正解文字）はあらかじめ別の文字に置き換えておく
                if inputWordArray[i].color == GREEN:
                    tmpCorrectWordArray.append("")
                else:
                    tmpCorrectWordArray.append(char)
            # 位置不一致、文字一致するものをチェック
            for i, charInfo in enumerate(inputWordArray):
                if charInfo.char in tmpCorrectWordArray:
                    inputWordArray[i].color = YELLOW
            
            if all(charInfo.color == GREEN for charInfo in inputWordArray):
                # 全文字完全一致
                # print("{0}回目、結果：".format(self.roopCount), end="")
                print("{0}回目".format(self.roopCount))

                # 文字の色を変える
                # child: Gridlayout, child.childlen: InputLabel
                for child in self.ids.scrollview.children:
                    for grandChild in child.children:
                        for i, greadGrandChild in enumerate(reversed(grandChild.children)):
                            i = i % self.correctWordLen
                            # 現在フォーカスしている行であるかチェック
                            if "{0}_".format(self.focusLine) in greadGrandChild.name:
                                greadGrandChild.color = (inputWordArray[i].color[0], inputWordArray[i].color[1], inputWordArray[i].color[2], inputWordArray[i].color[3])

                # リザルト画面へ遷移
                self.manager.current = 'Result'
            else:
                # print("{0}回目、結果：".format(self.roopCount), end="")
                print("{0}回目".format(self.roopCount))

                # 文字の色を変える
                # child: Gridlayout, child.childlen: InputLabel
                for child in self.ids.scrollview.children:
                    for grandChild in child.children:
                        for i, greadGrandChild in enumerate(reversed(grandChild.children)):
                            i = i % self.correctWordLen
                            # 現在フォーカスしている行であるかチェック
                            if "{0}_".format(self.focusLine) in greadGrandChild.name:
                                greadGrandChild.color = (inputWordArray[i].color[0], inputWordArray[i].color[1], inputWordArray[i].color[2], inputWordArray[i].color[3])

                # 初期状態に戻す
                self.targetLabel = 1
                self.focusLine += 1
                self.inputWord = ""
                self.add_rows()
            self.roopCount += 1
        else:
            # エラー
            print(message)
            self.ids.errorlabel.text = message
            self.ids.errorlabel.opacity = 1

            Clock.schedule_once(self.hideWidget, 3)

    def hideWidget(self, duration):
        self.ids.errorlabel.opacity = 0

    # 行を追加する
    def add_rows(self):
        # 入力ラベルを追加
        box_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50, pos_hint={"center_x": 0.5, "center_y": 0.5}, spacing=5, padding=5)
        for i in range(5):
            label = Factory.InputLabel(pos_hint={"center_x": 0.5, "center_y": 0.5})
            label.name = "{0}_{1}".format(self.focusLine, i+1)
            box_layout.add_widget(label)
        self.ids.scrollview.children[0].add_widget(box_layout)

# ScreenManagerの定義
class MyScreenManager(ScreenManager):
    pass

class WordPuzzleGuessApp(App):
    def build(self):
        sm = ScreenManager()
        sm.transition = NoTransition()
        sm.add_widget(HomeScreen(name='Home'))
        sm.add_widget(HowToPlayScreen(name='HowToPlay'))
        sm.add_widget(GameScreen(name='Game'))
        sm.add_widget(ResultScreen(name='Result'))
        return sm

def resourcePath():
    '''Returns path containing content - either locally or in pyinstaller tmp file'''
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS)
    return os.path.join(os.path.abspath("src"))

if __name__ == '__main__':
    kivy.resources.resource_add_path(resourcePath())
    WordPuzzleGuessApp().run()