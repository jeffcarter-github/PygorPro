from GUI_Change_Series_Type import GUI_Change_Series_Type


class ChangeSeries(GUI_Change_Series_Type):
    def __init__(self, lst_of_dataFrames):
        GUI_Change_Series_Type.__init__(self, lst_of_dataFrames)
        self.series_names = []

    def on_dataFrame_choice(self, event):
        pass

    def on_series_selection(self, event):
        pass

    def add_selections_to_gui(self, event):
        pass

    def on_cancel(self, event):
        self.Destroy()

    def on_ok(self, event):
        self.Destroy()