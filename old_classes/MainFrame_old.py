import wx
from CreateTablePopUp import CreateTablePopUp
from DataFrame import DataFrame
from HistoryFrame import HistoryFrame
from Plot import Plot
from Project import Project
from LoadFile import LoadFile
from Table import Table


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        self.create_menu_bar()

        self.history_frame = HistoryFrame(self)
        self.current_project = Project()
        self.history_frame.log_new_project()

        self.dataFrame_selection = None

    def create_menu_bar(self):
        menu_bar = wx.MenuBar()

        app_menu = wx.Menu()
        exit_option = app_menu.Append(wx.ID_ANY, '&Exit', 'Exit')
        self.Bind(wx.EVT_MENU, self.on_exit_option, exit_option)

        file_menu = wx.Menu()
        new_option = file_menu.Append(wx.ID_NEW, '&New Project', 'Create New Project')
        self.Bind(wx.EVT_MENU, self.on_new_option, new_option)
        open_option = file_menu.Append(wx.ID_OPEN, '&Open...', 'Open Existing Project')
        self.Bind(wx.EVT_MENU, self.on_open_option, open_option)
        save_option = file_menu.Append(wx.ID_SAVE, '&Save...', 'Save Project to File')
        self.Bind(wx.EVT_MENU, self.on_save_option, save_option)
        save_as_option = file_menu.Append(wx.ID_ANY, '&Save As...', 'Save Project As')
        self.Bind(wx.EVT_MENU, self.on_save_as_option, save_as_option)

        load_menu = wx.Menu()
        load_dataFrame_option = load_menu.Append(wx.ID_ANY, '&Load DataFrame...', 'Load Existing DataFrame')
        self.Bind(wx.EVT_MENU, self.on_load_dataFrame, load_dataFrame_option)
        load_binary_option = load_menu.Append(wx.ID_ANY, '&Load Binary Data...', 'Load Binary Data into DataFrame')
        self.Bind(wx.EVT_MENU, self.on_load_binary, load_binary_option)
        load_text_option = load_menu.Append(wx.ID_ANY, '&Load Text File...', 'Load Text File into DataFrame')
        self.Bind(wx.EVT_MENU, self.on_load_text, load_text_option)
        load_csv_option = load_menu.Append(wx.ID_ANY, '&Load CSV File...', 'Load Text File into DataFrame')
        self.Bind(wx.EVT_MENU, self.on_load_csv, load_csv_option)
        
        data_menu = wx.Menu()
        load_option = data_menu.AppendMenu(wx.ID_ANY, '&Load DataFrame', load_menu)
        data_menu.AppendSeparator()
        select_option = data_menu.Append(wx.ID_ANY, '&Select DataFrame...', 'Select DataFrame to make active')
        self.Bind(wx.EVT_MENU, self.on_activate_data, select_option)
        load_delete_option = data_menu.Append(wx.ID_ANY, '&Delete DataFrame...', 'Delete DataFrame from Project')
        self.Bind(wx.EVT_MENU, self.on_delete_data, load_delete_option)

        new_3D_plot_menu = wx.Menu()

        new_window_menu = wx.Menu()
        create_table_option = new_window_menu.Append(wx.ID_ANY, '&Create Table...', 'Create Table from DataFrame')
        self.Bind(wx.EVT_MENU, self.on_create_table_option, create_table_option)
        create_2D_plot_option = new_window_menu.Append(wx.ID_ANY, '&Create 2D Plot...', 'Create an Interactive Plot')
        self.Bind(wx.EVT_MENU, self.on_create_2D_plot_option, create_2D_plot_option)
        create_3D_plot_option = new_window_menu.AppendMenu(wx.ID_ANY, '&Create 3D Plot...', new_3D_plot_menu)
        new_window_menu.AppendSeparator()
        export_graph_option = new_window_menu.Append(wx.ID_ANY, '&Export Plot...', 'Export Plot to File')
        self.Bind(wx.EVT_MENU, self.on_export_graph, export_graph_option)

        quick_fit_menu = wx.Menu()
        stats_menu = wx.Menu()

        analysis_menu = wx.Menu()
        curve_fitting_option = analysis_menu.Append(wx.ID_ANY, '&Curve Fitting...', 'Curve Fitting')
        self.Bind(wx.EVT_MENU, self.on_curve_fitting, curve_fitting_option)
        analysis_menu.AppendMenu(wx.ID_ANY, '&Quick Curve Fitting...', quick_fit_menu)
        analysis_menu.AppendSeparator()
        correlate_option = analysis_menu.Append(wx.ID_ANY, '&Correlate...', 'Correlation Menu')
        self.Bind(wx.EVT_MENU, self.on_correlate, correlate_option)
        descriptive_statistics_option = analysis_menu.Append(wx.ID_ANY, '&Descriptive Statistics...', 'Descriptive Statistics')
        self.Bind(wx.EVT_MENU, self.on_describe, descriptive_statistics_option)
        analysis_menu.AppendMenu(wx.ID_ANY, '&Statistics', stats_menu)


        menu_bar.Append(app_menu, '&PygorPro')
        menu_bar.Append(file_menu, '&Project')
        menu_bar.Append(data_menu, '&DataFrame')
        menu_bar.Append(new_window_menu, '&Window')
        menu_bar.Append(analysis_menu, '&Analysis')

        self.SetMenuBar(menu_bar)

    def on_exit_option(self, event):
        self.Destroy()

    def on_new_option(self, event):
        pass

    def on_open_option(self, event):
        pass

    def on_save_option(self, event):
        if self.current_project.previously_saved:
            self.current_project.save_project()
        else:
            self.current_project.save_as_project()

    def on_save_as_option(self, event):
        self.current_project.save_as_project()

    def on_load_dataFrame(self, event):
        pass

    def on_load_binary(self, event):
        pass

    def on_load_text(self, event):
        text_file = None
        new_dataFrame = dataFrame().from_text(text_file)
        self.current_project.add_DataFrame_to_project()

    def on_load_csv(self, event):
        '''loads data from csv file into pandas dataFrame object'''
        dlg = wx.FileDialog(self, 'Select File to Open', '', '', '*.csv', wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            csv_file_path = dlg.GetPath()

            new_dataFrame = DataFrame()
            new_dataFrame.from_csv(csv_file_path)

            self.current_project.add_dataFrame_to_project(new_dataFrame)
            self.history_frame.log_new_dataFrame(new_dataFrame.source)

    def on_delete_data(self, event):
        '''pop up to delete a given data set...'''
        pass

    def on_activate_data(self, event):
        '''pop up to choice dataFrame to make active '''
        pass

    def on_create_table_option(self, event):
        current_dataFrames = self.current_project.get_dataFrame_names()
        if current_dataFrames != []:
            if len(current_dataFrames) == 1:
                self.df_selection_for_table(current_dataFrames[0])
            else:
                pop_up = CreateTablePopUp(self, current_dataFrames)

    def df_selection_for_table(self, current_dataFrame):
        table = Table(self, self.current_project
                                .get_dataFrame(current_dataFrame))

    def on_create_2D_plot_option(self, event):
        self.create_2D_plot_window()

    def create_2D_plot_window(self):
        import numpy as np
        x = np.random.random(50)
        y = np.random.random(50)
        next_index = len(self.current_project.project_figures)
        self.current_project.add_figure_to_project(
            Plot(next_index, x, y, 'x stuff', 'y_stuff'))

    def on_export_graph(self, event):
        pass

    def on_curve_fitting(self, event):
        pass

    def on_correlate(self, event):
        pass

    def on_describe(self, event):
        pass

    def report_statistics(self, dataFrame_name, dataSeries_name):
        dataSeries = self.current_project\
                         .get_dataFrame(dataFrame_name)\
                         .get_series(dataSeries_name)
        self.history_frame.log_dictionary(dataSeries.name, dataSeries.describe())
