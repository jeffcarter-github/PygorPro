import wx


class HistoryFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title='History', pos=(100, 600), size=(1200, 200))

        self.log_window =\
            wx.TextCtrl(self, wx.ID_ANY,
                        style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.VSCROLL)
        self.welcome()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.log_window, 1, wx.EXPAND)

        self.Show(True)

    def log_message(self, message):
        message += '\n'
        self.log_window.WriteText(message)

    def welcome(self):
        message = 'Welcome to PygorPro...'
        self.log_message(message)

    def log_new_project(self):
        self.log_message('New untitled project created...')

    def log_project_saved(self, project_name, file_path):
        self.log_message('%s has been saved...\t%s' % (project_name, file_path))

    def log_new_dataFrame(self, dataFrame_path):
        self.log_message('New dataFrame open...\t%s' % dataFrame_path)

    def log_already_exists(self, dataFrame_path):
        self.log_message('...dataFrame already exists in project...%s' % dataFrame_path)

    def log_new_table(self, table_name):
        self.log_message('New table created in project...\t%s' % table_name)

    def log_delete_table(self, table_name):
        self.log_message('Table deleted from project...\t%s' % table_name)

    def log_delete_dataFrame(self, dataFrame_name):
        self.log_message('DataFrame deleted from project...\t%s' % dataFrame_name)