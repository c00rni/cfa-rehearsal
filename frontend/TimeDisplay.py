from textual.widgets import Static
from textual.reactive import reactive
from time import monotonic

class TimeDisplay(Static):

   start_time = reactive(monotonic() + 60 * 60 * 4)
   time = reactive(0.0)

   def on_mount(self) -> None:
      """ Event handler called when widget is added to the app """
      self.set_interval(1 / 60, self.update_time)

   def update_time(self) -> None:
      self.time = self.start_time - monotonic()

   def watch_time(self, time: float) -> None:
      minutes, seconds = divmod(time, 60)
      hours, minutes = divmod(minutes, 60)
      self.update(f"{int(hours):02.0f}:{minutes:02.0f}:{seconds:02.0f}")


