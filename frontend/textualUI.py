from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, TabPane, Static, TabbedContent, Label, Button
from textual.containers import VerticalScroll, Horizontal
from textual import on

class SideMenu(VerticalScroll):
   """Custom side menu widget"""

   def compose(self):
      yield Button("Mock Exam", variant="success", id="exam")

class MockExam(VerticalScroll):

   def compose(self) -> ComposeResult:
      with Horizontal():
         yield Label("Question 1") 

class CfaPrepApp(App):
   BINDINGS = [
      ("q", "quit", "Quit the app"),
   ]

   CSS_PATH = "menu.tcss" 

   def compose(self):
      yield Header()
      yield Footer()
      yield MockExam(id="mockExam")
      yield MainMenu(id="mainMenu")

class MainMenu(Horizontal):
   """ Landing menu for the CFA prep mock exam """

   def on_button_pressed(self, event: Button.Pressed) -> None:
      """Event bandler called when a button is pressed"""
      self.add_class("examStarted")

   def action_toggle_dark_mode(self):
      self.dark = not self.dark

   def compose(self):
      with TabbedContent():
         with TabPane("Dashboard", id="one"):
            with Horizontal():
               yield SideMenu()
               yield Label("LOOOOOng story I couldn't feet here if I would like")

if __name__ == "__main__":
   app = CfaPrepApp()
   app.run()
