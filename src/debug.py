from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ScrollViewApp(App):
    def build(self):
        # ScrollViewの設定
        self.scroll_view = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), size=(400, 400))
        
        # GridLayoutの設定
        self.grid_layout = GridLayout(cols=1, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        
        # 追加ボタンの設定
        add_button = Button(text='ラベルを追加', size_hint_y=None, height=50)
        add_button.bind(on_press=self.add_label)
        
        # GridLayoutにボタンを追加
        self.grid_layout.add_widget(add_button)
        
        # ScrollViewにGridLayoutを追加
        self.scroll_view.add_widget(self.grid_layout)
        
        return self.scroll_view

    def add_label(self, instance):
        # 新しいラベルをGridLayoutに追加
        new_label = Label(text='新しいラベル', size_hint_y=None, height=50)
        self.grid_layout.add_widget(new_label, index=len(self.grid_layout.children))

if __name__ == '__main__':
    ScrollViewApp().run()