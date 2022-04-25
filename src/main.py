from rich.panel import Panel

from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget


class Hover(Widget):

    mouse_over = Reactive(False)

    def __init__(self, text="Hello World"): 
        super().__init__()
        self.text = text

    def render(self) -> Panel:
        return Panel(self.text, style=("on red" if self.mouse_over else ""))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def on_click(self) -> None:
        exit()

    def change_text(self, text):
        self.text = text


# class HoverApp(App):
#     """Demonstrates custom widgets"""

#     async def on_mount(self) -> None:
#         hovers = (Hover(), Hover())
#         await self.view.dock(*hovers, edge="top")


class GridTest(App):
    async def on_mount(self) -> None:
        """Make a simple grid arrangement."""

        grid = await self.view.dock_grid(edge="left", name="left")

        grid.add_column(fraction=1, name="left", min_size=20)
        grid.add_column(size=100, name="center")
        grid.add_column(fraction=1, name="right")

        grid.add_row(fraction=2, name="top", min_size=2)
        grid.add_row(fraction=1, name="middle-top")
        grid.add_row(fraction=2, name="middle-bot")
        grid.add_row(fraction=2, name="bottom")

        grid.add_areas(
            area1="left-start|right-end,top",
            area2="left-start|right-end,middle-top",
            area3="center,middle-bot",
            area4="center,bottom",
        )

        grid.place(
            area1=Hover("""
$$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$\ $$\   $$\  $$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |\_$$  _|$$$\  $$ |$$  __$$\\__$$  __|$$  __$$\ $$  __$$\ 
$$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  /   $$ |  $$$$\ $$ |$$ /  $$ |  $$ |   $$ /  $$ |$$ |  $$ |
$$$$$$$\ |$$$$$$$$ |\$$$$$$\  $$$$$  /    $$ |  $$ $$\$$ |$$$$$$$$ |  $$ |   $$ |  $$ |$$$$$$$  |
$$  __$$\ $$  __$$ | \____$$\ $$  $$<     $$ |  $$ \$$$$ |$$  __$$ |  $$ |   $$ |  $$ |$$  __$$< 
$$ |  $$ |$$ |  $$ |$$\   $$ |$$ |\$$\    $$ |  $$ |\$$$ |$$ |  $$ |  $$ |   $$ |  $$ |$$ |  $$ |
$$$$$$$  |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$\ $$ | \$$ |$$ |  $$ |  $$ |    $$$$$$  |$$ |  $$ |
\_______/ \__|  \__| \______/ \__|  \__|\______|\__|  \__|\__|  \__|  \__|    \______/ \__|  \__|                                                                                             
"""),
            area2=Hover("Do you have a basketball player in mind?"),
            area3=Hover("""
                                                    
────────────────────────────────────────────────────
─████████──████████──██████████████──██████████████─
─██░░░░██──██░░░░██──██░░░░░░░░░░██──██░░░░░░░░░░██─
─████░░██──██░░████──██░░██████████──██░░██████████─
───██░░░░██░░░░██────██░░██──────────██░░██─────────
───████░░░░░░████────██░░██████████──██░░██████████─
─────████░░████──────██░░░░░░░░░░██──██░░░░░░░░░░██─
───────██░░██────────██░░██████████──██████████░░██─
───────██░░██────────██░░██──────────────────██░░██─
───────██░░██────────██░░██████████──██████████░░██─
───────██░░██────────██░░░░░░░░░░██──██░░░░░░░░░░██─
───────██████────────██████████████──██████████████─
────────────────────────────────────────────────────
            """),
            area4=Hover("""
███╗░░██╗░█████╗░
████╗░██║██╔══██╗
██╔██╗██║██║░░██║
██║╚████║██║░░██║
██║░╚███║╚█████╔╝
╚═╝░░╚══╝░╚════╝░
            """),
        )


GridTest.run(title="Grid Test", log="textual.log")


HoverApp.run(title="Baskinator", log="textual.log")