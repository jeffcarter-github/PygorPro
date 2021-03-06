import wx

from PygorPro_MenuBar import PygorPro_MenuBar
from HistoryFrame import HistoryFrame
from Project import Project


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        self.menu_bar = PygorPro_MenuBar(self)
        self.SetMenuBar(self.menu_bar)

        self.history = HistoryFrame(self)
        self.project = Project()
        self.history.log_new_project()
