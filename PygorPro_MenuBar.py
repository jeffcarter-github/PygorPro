import wx

from BrowseDataFrames import BrowseDataFrames
from DataFrame import DataFrame
from DataSelectionForTable import DataSelectionForTable
from DataSelectionForPlot import DataSelectionForPlot
from GUI_PygorPro_MenuBar import GUI_PygorPro_MenuBar
from ChangeSeries import ChangeSeries
from Table import Table
from Plot import Plot


class PygorPro_MenuBar(GUI_PygorPro_MenuBar):
    def __init__(self, parent):
        self.parent = parent
        GUI_PygorPro_MenuBar.__init__(self)

    def on_new_project(self, event):
        pass

    def on_open_project(self, event):
        pass

    def on_save_project(self, event):
        pass

    def on_save_as_project(self, event):
        pass

    def on_load_csv(self, event):
        '''loads data from csv file into pandas dataFrame object'''
        dlg = wx.FileDialog(self, 'Select File to Open', '', '', '*.csv', wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            csv_file_path = dlg.GetPath()

            new_dataFrame = DataFrame()
            new_dataFrame.from_csv(csv_file_path)

            if self.parent.project.add_dataFrame(new_dataFrame):
                self.parent.history.log_new_dataFrame(new_dataFrame.source)
            else:
                self.parent.history.log_already_exists(new_dataFrame.source)

    def on_load_txt(self, event):
        pass

    def on_load_h5(self, event):
        pass

    def on_load_dataFrame(self, event):
        pass

    def on_browse_dataFrames(self, event):
        dataFrame_lst = self.parent.project.get_dataFrame_names()
        if dataFrame_lst != []:
            dlg = BrowseDataFrames(dataFrame_lst, self.delete_dataFrames)

    def on_change_dataSeries_type(self, event):
        dataFrame_lst = self.parent.project.get_dataFrame_names()
        if dataFrame_lst != []:
            dlg = ChangeSeries(dataFrame_lst)

    def on_rename_dataSeries(self, event):
        pass

    def on_delete_dataSeries(self, event):
        pass

    def on_export_dataFrame_as_csv(self, event):
        pass

    def on_export_dataFrame_as_h5(self, event):
        pass

    def on_pickle_dataFrame(self, event):
        pass

    def on_curve_fitting(self, event):
        pass

    def on_quickfit_line(self, event):
        pass

    def on_quickfit_poly2(self, event):
        pass

    def on_quickfit_poly3(self, event):
        pass

    def on_quickfit_poly4(self, event):
        pass

    def on_quickfit_poly5(self, event):
        pass

    def on_quickfit_poly6(self, event):
        pass

    def on_quickfit_poly7(self, event):
        pass

    def on_quickfit_poly8(self, event):
        pass

    def on_quickfit_gaussian(self, event):
        pass

    def on_quickfit_lorentzen(self, event):
        pass

    def on_quickfit_exponential(self, event):
        pass

    def on_quickfit_sinusoidal(self, event):
        pass

    def on_quickfit_sigmoidal(self, event):
        pass

    def on_quickfit_power(self, event):
        pass

    def on_quickfit_lognormal(self, event):
        pass

    def on_fit_between_points(self, event):
        pass

    def on_statistics_1D(self, event):
        pass

    def on_histogram(self, event):
        pass

    def on_check_data_quality(self, event):
        pass

    def on_create_new_2D_plot(self, event):
        current_dataFrame_names =\
            self.parent.project.get_dataFrame_names()
        if current_dataFrame_names != []:
            dlg =\
                DataSelectionForPlot(self.parent,
                                     current_dataFrame_names,
                                     self.generate_2D_plots)

    def generate_2D_plots(self, data_dictionary):
        '''callback function... data_dictionary is a dictionary of
        data_set dictionaries. The data_set keys are x_dataFrame,
        y_dataFrame, x_series, y_series, x_axis, y_axis, title, style...'''
        for key in data_dictionary:
            idx = self.parent.project.get_next_figure_index()
            self.parent.project.add_figure(
                Plot(idx, data_dictionary[key]))

    def on_create_new_3D_plot(self, event):
        pass

    def on_export_graphic(self, event):
        pass

    def on_create_table(self, event):
        # get list of current dataFrames for current project
        current_dataFrame_names =\
            self.parent.project.get_dataFrame_names()
        if current_dataFrame_names != []:
            # if only one dataFrame is loaded, create table without dialog box
            if len(current_dataFrame_names) == 1:
                self.create_tables(current_dataFrame_names)
            # else, open dialog gui for dataFrame selection
            else:
                data_selection =\
                    DataSelectionForTable(self, current_dataFrame_names, self.create_tables)

    def on_append_dataSeries_to_table(self, event):
        pass

    def on_delete_dataSeries_from_table(self, event):
        pass

    def on_export_table(self, event):
        pass

    def create_tables(self, lst_of_dataFrames):
        for dataFrame in lst_of_dataFrames:
            # create table object
            table = Table(self.parent, self.parent.project.get_dataFrame(dataFrame))
            # add table object to project table dictionary
            if self.parent.project.add_table(table):
                # report process to history bar
                self.parent.history.log_new_table(table.name)
            else:
                # ADD LOG FAILURE...
                pass

    def delete_dataFrames(self, lst_of_dataFrame_names):
        for dataFrame_name in lst_of_dataFrame_names:
            # remove from project dataFrame list
            self.parent.project.remove_dataFrame(dataFrame_name)
            self.parent.history.log_delete_dataFrame(dataFrame_name)
