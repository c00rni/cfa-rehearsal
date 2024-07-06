from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, TabPane, Static, TabbedContent, Label, Button, ProgressBar, Markdown, OptionList
from textual.widgets.option_list import Option, Separator
from textual.containers import VerticalScroll, Horizontal, Center, Middle
from textual.reactive import reactive
from time import monotonic

class SideMenu(VerticalScroll):
   """Custom side menu widget"""

   def compose(self):
      yield Button("Mock Exam", variant="success", id="exam")

class TimeDisplay(Static):

   start_time = reactive(monotonic)
   time = reactive(0.0)

   def on_mount(self) -> None:
      """ Event handler called when widget is added to the app """
      self.set_interval(1 / 60, self.update_time)

   def update_time(self) -> None:
      self.time = monotonic() - self.start_time

   def watch_time(self, time: float) -> None:
      minutes, seconds = divmod(time, 60)
      hours, minutes = divmod(minutes, 60)
      minutes = 59 if minutes == 0 else 59 - minutes
      seconds = 60 - seconds
      self.update(f"{int(hours)}:{minutes:02.0f}:{seconds:02.2f}")

class MockExam(VerticalScroll):
   """ Custom widget for Questions of a full mock exam """

   markdown_text = """
# Question

This is an example of Textual's `Markdown` widget ?

| Aligné à gauche  | Centré          | Aligné à droite |
| :--------------- |:---------------:| -----:|
| Aligné à gauche  |   ce texte        |  Aligné à droite |
| Aligné à gauche  | est             |   Aligné à droite |
| Aligné à gauche  | centré          |    Aligné à droite |
   """

   def compose(self) -> ComposeResult:
      #with Horizontal():
      #   yield Label("Prgress: ")
      #   yield ProgressBar(total=180, show_eta=False)
      #  yield TimeDisplay()
      with VerticalScroll():
         yield Markdown(self.markdown_text)
         yield OptionList(
            Option("A: Bonjour"),
            Separator(),
            Option("B: Aurevoire"),
            Separator(),
            Option("C: Merci"),
         )
         yield Button("Next question", variant="success")


class ExamTimer(Static):

   def compose(self) -> ComposeResult:
      with Center():
         with Middle():
            yield Label("Time: ")
            yield TimeDisplay()


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
