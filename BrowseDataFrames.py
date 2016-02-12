from GUI_Browse_DataFrames import GUI_Browse_DataFrames


class BrowseDataFrames(GUI_Browse_DataFrames):
    def __init__(self, dataFrame_lst, call_back_func):
        GUI_Browse_DataFrames.__init__(self, dataFrame_lst)
        self.dataFrame_lst = dataFrame_lst
        self.call_back_func = call_back_func
        self.selections = None
        self.delete_lst = []

    def on_add_to_list(self, event):
        self.selections = [self.dataFrame_ListBox.GetString(idx) for idx in self.dataFrame_ListBox.GetSelections()]
        for selection in self.selections:
            if selection not in self.delete_lst:
                self.delete_lst.append(selection)
        self.list_for_deletion.Set(self.delete_lst)

    def on_cancel_click(self, event):
        self.Destroy()

    def on_ok_click(self, event):
        self.call_back_func(self.delete_lst)
        self.Destroy()
