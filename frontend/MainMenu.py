from textual.widgets import TabPane,  TabbedContent, Label, Button, Static
from textual.containers import VerticalScroll, Horizontal

class SideMenu(VerticalScroll):
   """Custom side menu widget"""

   def compose(self):
      yield Button("Mock Exam", variant="success", id="exam")

class MainMenu(Static):
   """ Landing menu for the CFA prep mock exam """

   def on_button_pressed(self, event: Button.Pressed) -> None:
      """Event bandler called when a button is pressed"""
      self.add_class("examStarted")

   def compose(self):
      with TabbedContent():
         with TabPane("Dashboard", id="one"):
            with Horizontal():
               yield SideMenu()
               yield Label("LOOOOOng story I couldn't feet here if I would like")


