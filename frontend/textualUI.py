from textual.app import App
from textual.widgets import Header, Footer
from textual.containers import ScrollableContainer
from frontend.MockExam import MockExam


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

      new_exam = MockExam()
      self.query_one("#screen").mount(new_exam)

   def action_stop_exam(self) -> None:
      """ Called to stop an exam"""
      exams = self.query("MockExam")
      if exams:
         exams.last().remove()

