import win32process
import win32ui

import option as gameOp


class Game:
    name = ''
    options_list = []

    def __init__(self, name):
        self.name = name
        self.options_list = Game._options(name)

    def enable(self):
        hwnd = win32ui.FindWindow(None, self.name).GetSafeHwnd()
        tid, pid = win32process.GetWindowThreadProcessId(hwnd)

    @staticmethod
    def _options(name):
        if name == 'ShellShock Live':
            return Game._ssl_options()

    @staticmethod
    def _ssl_options():
        all_options = list()

        # Option1: Change Angle ang Power
        description, type_option, hot_key = 'Change Angle ang Power', 'static address', 'ctrl+F1'
        all_options.append(gameOp.GameOption(description, type_option, hot_key))
        value = all_options[-1].logic.enable()
        # отобразить value на экране игры



        return all_options
