'''blah'''
import wx

from GUI_Selection_Plot import GUI_Selection_Plot


class DataSelectionForPlot(GUI_Selection_Plot):
    def __init__(self, main_frame, lst_of_dataFram_names):
        GUI_Selection_Plot.__init__(self, None, lst_of_dataFram_names)
        self.main_frame = main_frame

    def on_choice_ySeries_dataFrame(self, event):
        selection = self.y_DataFrame_ChoiceBox.GetSelection()
        data_frame_name = self.y_DataFrame_ChoiceBox.GetString(selection)
        lst_of_series_names =\
            self.main_frame.project.get_series_names(data_frame_name)
        self.y_Series_ListBox.SetItems(lst_of_series_names)

    def calculate_ySeries_options(self, event):
        pass

    def on_choice_xSeries_dataFrame(self, event):
        selection = self.x_DataFrame_ChoiceBox.GetSelection()
        data_frame_name = self.x_DataFrame_ChoiceBox.GetString(selection)
        lst_of_series_names =\
            self.main_frame.project.get_series_names(data_frame_name)
        self.x_Series_ListBox.SetItems(lst_of_series_names)

    def calculate_xSeries_options(self, event):
        pass

    def on_choice_ySeries(self, event):
        pass

    def on_choice_xSeries(self, event):
        pass

    def on_choice_y_axis_position(self, event):
        pass

    def on_choice_x_axis_position(self, event):
        pass

    def on_add_series_pair(self, event):
        pass

    def on_choice_plot_style(self, event):
        pass

    def on_click_Cancel(self, event):
        self.Destroy()

    def on_click_OK(self, event):
        pass


if __name__ == '__main__':
    '''main loop only for checking the GUI style'''

    def MainFrame():
        dlg = DataSelectionForPlot(None, ['A', 'B', 'C'])

    app = wx.App()
    MainFrame()
    app.MainLoop()
