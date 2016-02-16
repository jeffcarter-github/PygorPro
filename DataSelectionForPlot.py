'''blah'''
import wx
from GUI_Selection_Plot import GUI_Selection_Plot
from PopUpBox import PopUpBox


class DataSelectionForPlot(GUI_Selection_Plot):
    def __init__(self, main_frame, lst_of_dataFram_names, plot_callBack):
        GUI_Selection_Plot.__init__(self, None, lst_of_dataFram_names)
        self.main_frame = main_frame
        self.plot_callBack = plot_callBack
        self.data_for_plots = {}

    def on_choice_ySeries_dataFrame(self, event):
        data_frame_name = self.y_DataFrame_ChoiceBox.GetStringSelection()
        lst_of_series_names =\
            self.main_frame.project.get_series_names(data_frame_name)
        self.y_Series_ListBox.SetItems(lst_of_series_names)

    def calculate_ySeries_options(self, event):
        pass

    def on_choice_xSeries_dataFrame(self, event):
        data_frame_name = self.x_DataFrame_ChoiceBox.GetStringSelection()
        lst_of_series_names =\
            self.main_frame.project.get_series_names(data_frame_name)
        self.x_Series_ListBox.SetItems(lst_of_series_names)

    def calculate_xSeries_options(self, event):
        pass

    def on_choice_ySeries(self, event):
        print self.y_Series_ListBox.GetSelection()

    def on_choice_xSeries(self, event):
        pass

    def on_choice_y_axis_position(self, event):
        pass

    def on_choice_x_axis_position(self, event):
        pass

    def on_add_series_pair(self, event):
        x_dataFrame_name = self.y_DataFrame_ChoiceBox.GetStringSelection()
        y_dataFrame_name = self.y_DataFrame_ChoiceBox.GetStringSelection()
        x_series_name = self.x_Series_ListBox.GetStringSelection()
        y_series_name = self.y_Series_ListBox.GetStringSelection()
        try:
            x_data =\
                self.main_frame.project.get_series(x_dataFrame_name, x_series_name)
            y_data =\
                self.main_frame.project.get_series(y_dataFrame_name, y_series_name)

            if len(x_data) != len(y_data):
                dlg = PopUpBox('x and y must have same dimension')
            elif isinstance(x_data.dtype, [object, str]) or isinstance(y_data.dtype, [object, str]):


                dic_key =\
                    x_dataFrame_name + x_series_name + y_dataFrame_name + y_series_name

                if dic_key not in self.data_for_plots:
                    x_axis = self.x_axis_ChoiceBox.GetStringSelection()
                    y_axis = self.y_axis_ChoiceBox.GetStringSelection()
                    title = self.plot_title_TxtCtrl.GetLineText(0)
                    style = self.plot_style_ChoiceBox.GetStringSelection()
                    self.data_for_plots[dic_key] = {'x_data': x_data,
                                                    'y_data': y_data,
                                                    'x_axis': x_axis,
                                                    'y_axis': y_axis,
                                                    'x_label': x_series_name,
                                                    'y_label': y_series_name,
                                                    'title': title,
                                                    'style': style}

                    # write to dialog
                    self.dialog_TxtCtrl.WriteText('%s Plot:\n %s::%s \\%s vs %s::%s \\%s\n' %
                        (style, y_dataFrame_name, y_series_name, y_axis, x_dataFrame_name, x_series_name, x_axis))
        except KeyError:
            pass

    def on_choice_plot_style(self, event):
        pass

    def on_click_Cancel(self, event):
        self.Destroy()

    def on_click_OK(self, event):
        self.plot_callBack(self.data_for_plots)
        self.Destroy()


if __name__ == '__main__':
    '''main loop only for checking the GUI style'''

    def MainFrame():
        dlg = DataSelectionForPlot(None, ['A', 'B', 'C'])

    app = wx.App()
    MainFrame()
    app.MainLoop()
