from textual.app import ComposeResult
from textual.widgets import Button, Label, ProgressBar, Markdown, OptionList
from textual.widgets.option_list import Option, Separator
from textual.containers import VerticalScroll, Horizontal
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
      with Horizontal():
         yield Label("Prgress: ")
         yield ProgressBar(total=180, show_eta=False)
         yield TimeDisplay()
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


