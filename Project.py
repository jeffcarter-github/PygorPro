import matplotlib as mpl
import pandas as pd


class Project():
    def __init__(self, project_name='untitled', project_path=None):
        self.project_name = project_name
        self.project_path = project_path
        self.previously_saved = False

        self.project_dataFrames = {}
        self.project_tables = {}
        self.project_figures = {}

        self.project_active_dataFrame = None
        self.project_active_table = None
        self.project_active_figure = None

    def save_project(self):
        pass

    def save_as_project(self):
        self.previously_saved = True

    def add_dataFrame_to_project(self, new_dataFrame):
        key = new_dataFrame.name
        if key not in self.project_dataFrames.keys():
            self.project_dataFrames[key] = new_dataFrame

    def add_table_to_project(self, new_table):
        key = new_table.name
        self.project_tables[key] = new_table

    def remove_table_from_project(self, closed_table):
        print 'table removed...%s' % closed_table.name

    def add_figure_to_project(self, new_figure):
        self.project_figures[new_figure.plot_index] = new_figure

    def get_dataFrame_names(self):
        return self.project_dataFrames.keys()

    def get_dataFrame(self, name):
        return self.project_dataFrames[name]

    def get_table_names(self):
        return self.project_tables.keys()

    def get_figure_names(self, print_flag=False):
        if print_flag:
            print self.project_figures
        return self.project_figures

    def set_active(self, selected_object):
        if isinstantance(selected_object, pd.core.frame.DataFrame):
            self.project_active_dataFrame = selected_dataFrame
        elif isinstantance(selected_object, Table):
            self.project_active_table = selected_object
        elif isinstantance(selected_object, mpl.figure.Figure):
            self.project_active_figure = selected_object
