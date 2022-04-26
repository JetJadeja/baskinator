from rich.panel import Panel

from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget


class Hover(Widget):

    mouse_over = Reactive(False)

    def __init__(self, text: str, widget: Hover, next_question: str): 
        super().__init__()
        self.text = text

    def render(self) -> Panel:
        return Panel(self.text, style=("on red" if self.mouse_over else ""))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def change_text(self, text):
        self.text = text

class Yes(Widget):
    def __init__(self, text: str, widget: Hover, next_question: str):
        super().__init__(text)
        self.text = text
        self.widget = Hover
        self.next_question = next_question

    def on_click(self) -> None:
        self.widget.change_text(self.next_question)

    
