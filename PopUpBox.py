import wx


class PopUpBox(wx.Dialog):
    def __init__(self, message):
        wx.Dialog.__init__ (self, None, id = wx.ID_ANY, title = u"Error Message", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.Size(200,-1), wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        bSizer131 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel29 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer132 = wx.BoxSizer(wx.VERTICAL)

        bSizer134 = wx.BoxSizer(wx.VERTICAL)

        bSizer136 = wx.BoxSizer(wx.VERTICAL)

        static_text = 'Error:\t%s\n\nClick \'OK\' to Continue...' % message
        self.message = wx.StaticText(self.m_panel29, wx.ID_ANY, static_text, wx.DefaultPosition, wx.DefaultSize, 0)
        self.message.Wrap(-1)
        bSizer136.Add(self.message, 0, wx.ALL, 5)

        bSizer134.Add(bSizer136, 0, wx.EXPAND, 5)

        bSizer133 = wx.BoxSizer(wx.VERTICAL)

        self.m_button11 = wx.Button(self.m_panel29, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer133.Add(self.m_button11, 0, wx.ALL, 5)

        bSizer134.Add(bSizer133, 0, wx.ALIGN_CENTER, 5)

        bSizer132.Add(bSizer134, 1, wx.EXPAND, 5)

        self.m_panel29.SetSizer(bSizer132)
        self.m_panel29.Layout()
        bSizer132.Fit(self.m_panel29)
        bSizer131.Add(self.m_panel29, 1, wx.ALIGN_CENTER | wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer131)
        self.Layout()
        bSizer131.Fit(self)

        self.Centre(wx.BOTH)
        self.Show(True)

        # Connect Events
        self.m_button11.Bind(wx.EVT_BUTTON, self.on_ok)

    def __del__(self):
        pass

    def on_ok(self, event):
        self.Destroy()
