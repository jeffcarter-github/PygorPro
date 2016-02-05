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

    def welcome(self):
        message = 'Welcome to PygorPro...'
        self.log_message(message)

    def log_new_project(self):
        self.log_message('New untitled project created...')

    def log_new_dataFrame(self, dataFrame_path):
        self.log_message('New dataFrame open from:')
        self.log_message('...' + dataFrame_path)

    def log_message(self, message):
        message += '\n'
        self.log_window.WriteText(message)

    def log_dictionary(self, series, dictionary):
        self.log_message('Data Series: ' + series)
        for key in dictionary.keys():
            message = '\t%s\t\t %12.8f' % (str(key), dictionary[key])
            self.log_message(message)
