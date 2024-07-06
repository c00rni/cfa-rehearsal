from textual.app import App
from textual.widgets import Header, Footer
from MockExam import MockExam
from MainMenu import MainMenu

class CfaPrepApp(App):
   BINDINGS = [
      ("q", "quit", "Quit the app"),
   ]

   CSS_PATH = "menu.tcss" 

   def compose(self):
      yield Header()
      yield MockExam(id="mockExam")
      yield MainMenu(id="mainMenu")
      yield Footer()

if __name__ == "__main__":
   app = CfaPrepApp()
   app.run()
