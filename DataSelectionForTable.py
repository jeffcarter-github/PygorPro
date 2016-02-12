import wx
from GUI_SelectDataFrameForTable import GUI_SelectDataFrameForTable
from Table import Table


class DataSelectionForTable(GUI_SelectDataFrameForTable):
    def __init__(self, parent, dataFrame_names, call_back_func):
        GUI_SelectDataFrameForTable.__init__(self, dataFrame_names)

        self.names = dataFrame_names
        self.call_back_func = call_back_func
        self.selections = None

    def ok_cancel(self, event):
        self.Destroy()

    def on_ok(self, event):
        self.selections = [self.dataFrame_ListBox.GetString(idx) for idx in self.dataFrame_ListBox.GetSelections()]
        self.call_back_func(self.selections)
        self.Destroy()
