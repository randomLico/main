from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
<ItemLabel@Label>:
    font_size:"10sp"
    halign:"left"
    valign:"middle"
    text_size: self.size

<Container>:
    rows: 3

    text_input: text_input
    byte: byte
    kbyte: kbyte
    gbyte: gbyte
    tbyte: tbyte
    pbyte: pbyte

    AnchorLayout:
        size_hint: 0.23, 0.15

        TextInput:
            id: text_input
            font_size: "5sp"
            multiline: False
            input_type: "number"
            input_filter: "int"
    GridLayout:
        cols: 2

        BoxLayout:
            orientation: "vertical"
            padding:[10,0,10,0]

            ItemLabel:
                text: "byte"

            ItemLabel:
                text: "kbyte"

            ItemLabel:
                text: "gbyte"

            ItemLabel:
                text: "tbyte"

            ItemLabel:
                text: "pbyte"

        BoxLayout:
            orientation: "vertical"
            size_hint: 1, 1

            ItemLabel:
                id: byte
                text:"0"

            ItemLabel:
                id:kbyte
                text:"0"

            ItemLabel:
                id:gbyte
                text:"0"

            ItemLabel:
                id:tbyte
                text:"0"

            ItemLabel:
                id:pbyte
                text:"0"
        BoxLayout:
            size_hint: 0.9, 0.15
            padding: [10, 5, 30, 0]

            Button:
                text: "Рассчитать?"
                font_size: 40

                on_release:
                    root.calculate()""")

Window.size = (1080,2135)

from kivy.config import Config

Config.set('kivy','keyboard-mode', 'systemanddock')

def get_ingridients(m):
    byte = str( m * 1048576)
    kbyte = str(  m * 1024)
    gbyte = str( m / 1024)
    tbyte = str( m / 1048576)
    pbyte = str(m / 1073741824)

    return{"byte": byte, "kbyte": kbyte, "gbyte": gbyte, "tbyte": tbyte, "pbyte": pbyte}


class Container(BoxLayout):

    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0

        ingridients = get_ingridients(mass)

        self.byte.text = ingridients.get("byte")
        self.kbyte.text = ingridients.get("kbyte")
        self.gbyte.text = ingridients.get("gbyte")
        self.tbyte.text = ingridients.get("tbyte")
        self.pbyte.text = ingridients.get("pbyte")


class MyApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    MyApp().run()