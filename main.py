from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class PlaneGame(App):
    def build(self):
        root = BoxLayout(orientation='horizontal')
        self.grid = GridLayout(cols=26, rows=30, spacing=1, size_hint=(0.8, 1))
        self.buttons = {}

        for row in range(30, 0, -1):
            for col in range(26):
                name = chr(ord('A') + col) + str(row)
                btn = Button(text=name, font_size=10)
                self.buttons[name.upper()] = btn
                self.grid.add_widget(btn)

        control = BoxLayout(orientation='vertical', size_hint=(0.2, 1))
        self.input_box = TextInput(hint_text="Enter coordinates", size_hint=(1, 0.1))
        self.input_box.bind(on_text_validate=self.on_enter)
        control.add_widget(self.input_box)

        root.add_widget(self.grid)
        root.add_widget(control)

        self.plane_pos = 'A1'
        self.mark_plane(self.plane_pos)

        return root

    def mark_plane(self, pos):
        for btn in self.buttons.values():
            btn.background_color = (1, 1, 1, 1)
        if pos in self.buttons:
            self.buttons[pos].background_color = (1, 0, 0, 1)

    def move_plane(self, pos_list):
        if not pos_list:
            return
        next_pos = pos_list.pop(0)
        self.mark_plane(next_pos)
        Clock.schedule_once(lambda dt: self.move_plane(pos_list), 0.2)

    def on_enter(self, instance):
        cmd = self.input_box.text.upper().replace(" ", "")
        if ',' in cmd:
            path = cmd.split(',')
        else:
            path = self.get_path(self.plane_pos, cmd)
        self.move_plane(path)
        self.plane_pos = path[-1]
        self.input_box.text = ''

    def get_path(self, start, end):
        sx, sy = ord(start[0]) - 65, int(start[1:]) - 1
        ex, ey = ord(end[0]) - 65, int(end[1:]) - 1
        path = []
        while sx != ex or sy != ey:
            if sx < ex: sx += 1
            elif sx > ex: sx -= 1
            if sy < ey: sy += 1
            elif sy > ey: sy -= 1
            pos = chr(65 + sx) + str(sy + 1)
            path.append(pos)
        return path
