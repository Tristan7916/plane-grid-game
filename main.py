from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class PlaneGridApp(App):
    def build(self):
        root = BoxLayout(orientation='horizontal')
        self.grid = GridLayout(cols=26, rows=30, spacing=1, size_hint=(0.8,1))
        self.cells = {}
        for row in range(30,0,-1):
            for col in range(26):
                coord = chr(65+col)+str(row)
                lbl = Label(text=coord, font_size=10)
                self.cells[coord] = lbl
                self.grid.add_widget(lbl)
        control = BoxLayout(orientation='vertical', size_hint=(0.2,1))
        self.input_box = TextInput(hint_text="Enter coords", size_hint_y=0.1)
        self.input_box.bind(on_text_validate=self.on_enter)
        control.add_widget(self.input_box)
        control.add_widget(Label(text="Hit Enter to play!", size_hint_y=0.1))
        root.add_widget(self.grid)
        root.add_widget(control)
        self.current = None
        return root

    def on_enter(self, instance):
        text = instance.text.upper().replace(" ","")
        instance.text = ""
        if text in self.cells:
            if self.current:
                self.cells[self.current].color = (1,1,1,1)
            self.cells[text].color = (1,0,0,1)
            self.current = text

if __name__ == "__main__":
    PlaneGridApp().run()
