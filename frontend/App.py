from textual.app import App
from textual.widgets import Header, Footer
from textual.containers import ScrollableContainer
from MockExam import MockExam
from MainMenu import MainMenu

class CfaPrepApp(App):
   BINDINGS = [
      ("q", "quit", "Quit the app"),
      ("s", "launch_exam", "Start a full exam"),
      ("x", "stop_exam", "Stop a full exam"),
   ]

   CSS_PATH = "menu.tcss" 

   def compose(self):
      yield Header()
      yield ScrollableContainer(id="screen")
      yield Footer()

   def action_launch_exam(self) -> None:
      """Called to start a full cfa mock exams """
      new_exam = MockExam([["""
This is an example of Textual's `Markdown` widget ?

| Aligné à gauche  | Centré          | Aligné à droite |
| :--------------- |:---------------:| -----:|
| Aligné à gauche  |   ce texte        |  Aligné à droite |
| Aligné à gauche  | est             |   Aligné à droite |
| Aligné à gauche  | centré          |    Aligné à droite |
   """, ["Bonjour","Merci","Aurevoir"], 0],["La seconde lettre de l'alphabet ?", ["A","B","C"], 1]])
      self.query_one("#screen").mount(new_exam)

   def action_stop_exam(self) -> None:
      """ Called to stop an exam"""
      exams = self.query("MockExam")
      if exams:
         exams.last().remove()

if __name__ == "__main__":
   app = CfaPrepApp()
   app.run()
