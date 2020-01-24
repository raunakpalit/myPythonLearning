class Pycharm():
    def execute(self):
        print("Compiling")
        print("Running")


class VisualCode():
    def execute(self):
        print("Check indentation")
        print("Check Spelling")
        print("Compiling")
        print("Running")


class Laptop():
    def editor(self, ide):
        ide.execute()


ide = VisualCode()


lap1 = Laptop()
lap1.editor(ide)