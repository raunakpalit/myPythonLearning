import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    name = ObjectProperty(None)
    lastName = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print("Name: {}, LastName: {}, Email: {}".format(self.name.text, self.lastName.text, self.email.text))
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()