from textual.app import ComposeResult
from textual.widgets import Button, Label, ProgressBar, Markdown, OptionList, Static
from textual.widgets.option_list import Option, Separator
from textual.containers import VerticalScroll, Horizontal, Container, Middle, Center
from TimeDisplay import TimeDisplay

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
      with Horizontal(id="topBar"):
         with Middle(id="progress"):
            yield Label("Prgress: ")
            yield ProgressBar(total=180, show_eta=False)
         with Middle(id="time"):
            yield Label("Time: ")
            yield TimeDisplay()

      with Static(id="questionSection"):
         with VerticalScroll(id="question"):
            yield Markdown(self.markdown_text)
            yield OptionList(
               Option("A: Bonjour"),
               Separator(),
               Option("B: Aurevoire"),
               Separator(),
               Option("C: Merci"),
            )
            with Center():
               yield Button("Next question", variant="success", id="buttonNext")

