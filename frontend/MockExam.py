from textual.app import ComposeResult
from textual.widgets import Button, Label, ProgressBar, Markdown, OptionList, Static
from textual.widgets.option_list import Option, Separator
from textual.containers import VerticalScroll, Horizontal, Container, Middle, Center
from TimeDisplay import TimeDisplay
from textual.reactive import reactive

class MockExam(VerticalScroll):
   """ Custom widget for Questions of a full mock exam """

   curr_question_index = reactive(0)

   def __init__(self, questions):
      super().__init__()
      self.questions = questions

   def on_button_pressed(self, event: Button.Pressed) -> None:
      if event.button.id == "buttonNext":
         if self.curr_question_index < len(self.questions) - 1:
            self.curr_question_index += 1
         else:
            self.add_class("examEnded")

   def watch_curr_question_index(self, curr_question_index: int) -> None:
      question, candidates, awnser_index = self.questions[curr_question_index]
      statementViewer = self.query_one("#statementViewer")
      statementViewer.update(question)

      options = self.query_one("#options") 
      options.clear_options()
      options.add_options(candidates)

   def compose(self) -> ComposeResult:
      with Horizontal(id="topBar"):
         with Middle(id="progress"):
            yield Label("Prgress: ")
            yield ProgressBar(total=len(self.questions), show_eta=False)
         with Middle(id="time"):
            yield Label("Time: ")
            yield TimeDisplay()

      with Static(id="questionSection"):
         with VerticalScroll(id="question"):
            yield Markdown(id="statementViewer")
            yield OptionList(id="options")
            with Center():
               yield Button("Next question", variant="success", id="buttonNext")

