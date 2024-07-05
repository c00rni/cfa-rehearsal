from textual.app import App
from textual.widgets import Footer, Header

class MainMenu(App):
   """ Landing menu for the CFA prep mock exam """
   
   def compose(self):
      yield Header()
      yield Footer()

if __name__ == "__main__":
   app = MainMenu()
   app.run()
