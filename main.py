main.py

from kivy.app import App from kivy.uix.gridlayout import GridLayout from kivy.uix.label import Label from kivy.uix.textinput import TextInput from kivy.uix.button import Button from kivy.uix.image import Image from kivy.core.window import Window from kivy.uix.boxlayout import BoxLayout

Set fixed window size for consistency on Android

Window.size = (800, 1200)

class PlaneGame(App): def build(self): self.grid_width = 26 self.grid_height = 30

layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

    self.grid = GridLayout(cols=self.grid_width, spacing=2, size_hint_y=0.85)
    self.labels = {}

    for y in range(1, self.grid_height+1):
        for x in range(self.grid_width):
            label = Label(text='', size_hint=(None, None), size=(30, 30))
            coord = f"{chr(65 + x)}{y}"
            self.labels[coord] = label
            self.grid.add_widget(label)

    layout.add_widget(self.grid)

    self.plane = Image(source='plane.png', size_hint=(None, None), size=(30, 30))
    self.grid.add_widget(self.plane)

    self.input_box = TextInput(hint_text='Enter coordinate (e.g. A1)', multiline=False, size_hint_y=None, height=50)
    self.input_box.bind(on_text_validate=self.move_plane)
    layout.add_widget(self.input_box)

    self.status = Label(text='Hit enter to play', size_hint_y=None, height=40)
    layout.add_widget(self.status)

    return layout

def move_plane(self, instance):
    coord = self.input_box.text.strip().upper()
    self.status.text = ''

    if coord in self.labels:
        for label in self.labels.values():
            label.canvas.clear()

        target_label = self.labels[coord]
        target_label.canvas.add(self.plane.canvas)
        self.status.text = f"Plane moved to {coord}"
    else:
        self.status.text = 'Invalid coordinate!'

    self.input_box.text = ''

if name == 'main': PlaneGame().run()

