import fabric
from fabric import Application
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.widgets.label import Label
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.datetime import DateTime
from fabric.system_tray.widgets import SystemTray
from fabric.utils import get_relative_path


class StatusBar(Window):
    def __init__(self):
        super().__init__(
            monitor = 0,
            name = 'status-bar',
            layer = "top",
            exclusivity= "auto",
            anchor = "left top right",
            margin = '10px -5px 0px 12px'
        )
        self.seperator = Label(
            '|',
            justification = 'center',


        )

        self.clock = DateTime(
            name = 'clock',
        )

        self.system_tray = SystemTray(
            name = 'sys-tray'
        )

        self.children = CenterBox(
            name = 'center',
            size=[55, 55],
            center_children=[self.clock, self.seperator, self.system_tray],
        )

if __name__ == '__main__':
    bar = StatusBar()
    app = Application('status-bar', bar)
    app.set_stylesheet_from_file(get_relative_path("./style.css"))
    app.run()