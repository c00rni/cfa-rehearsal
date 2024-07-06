from textual.widgets import Label, Static
from TimeDisplay import TimeDisyplay

class ExamTimer(Static):

   def compose(self) -> ComposeResult:
       yield Label("Time: ")
       yield TimeDisplay()

