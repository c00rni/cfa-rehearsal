from textual.widgets import Static
from textual.reactive import reactive
from time import monotonic

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
      hours = int(3 - hours)
      minutes = 59 if minutes == 0 else 59 - minutes
      seconds = int(60 - seconds)
      self.update(f"{int(hours)}:{minutes:02.0f}:{seconds}")


