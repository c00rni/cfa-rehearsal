from textual.app import ComposeResult
from textual.widgets import Button, Label, ProgressBar, Markdown, OptionList, Static, DataTable
from textual.widgets.option_list import Option, Separator
from textual.containers import VerticalScroll, Horizontal, Container, Middle, Center, ScrollableContainer
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
         selector = self.query_one("#options")
         if self.curr_question_index < len(self.questions) - 1:
            self.curr_question_index += 1
         else:
            self.add_class("examEnded")
            topics = [("Ethical and Professional Standards",0.15),
               ("Quantitative Methods",0.12),
               ("Economics",0.12),
               ("Financial Statement Analysis",0.16),
               ("Corporate Issuers",0.08),
               ("Portfolio Management",0.1),
               ("Equity Investments",0.1),
               ("Fixed Income",0.05),
               ("Derivatives",0.05),
               ("Alternative Investments",0.07)]
            result = {}
            for question in self.questions:
               topic = question["topic"]
               if result.get(topic, None):
                  t, score, total = result[topic]
                  result[topic] = [t, score, total + 1]
               else:
                  result[topic] = [topic, 0, 1]

               if question.get("user_choice", None) != None and question["awnser"] == question["user_choice"]:
                  result[topic][1] += 1


            ROWS = [("#", "Topic", "Score")] + [(res[0], topics[res[0]][0], str(res[1]/res[2]*100)+"%") for res in result.values()]
            table = self.query_one("#scoreTable")
            table.clear()
            table.add_columns(*ROWS[0])
            table.add_rows(ROWS[1:])

      if event.button.id == "buttonBack":
         self.remove_class("examEnded")


   def on_option_list_option_selected(self, message: OptionList.OptionSelected) -> None:
      curr_question = self.questions[self.curr_question_index] 
      curr_question["user_choice"] = message.option_index


   def watch_curr_question_index(self, curr_question_index: int) -> None:
      curr_question = self.questions[curr_question_index]
      statementViewer = self.query_one("#statementViewer")
      statementViewer.update(curr_question["statement"])

      options = self.query_one("#options") 
      options.clear_options()
      options.add_options(curr_question["candidates"])

      progress_bar = self.query_one("#progressBar")
      progress_bar.advance(1)

   def compose(self) -> ComposeResult:
      with Horizontal(id="topBar"):
         with Middle(id="progress"):
            yield Label("Prgress: ")
            yield ProgressBar(total=len(self.questions), show_eta=False, id="progressBar")
         with Middle(id="time"):
            yield Label("Time: ")
            yield TimeDisplay()

      with Static(id="questionSection"):
         with VerticalScroll(id="question"):
            yield Markdown(id="statementViewer")
            yield OptionList(id="options")
            with Center():
               yield Button("Next question", variant="success", id="buttonNext")
      with Center(id="scoreScreen"):
         yield DataTable(id="scoreTable")
