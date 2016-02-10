import wx


class GUI_Select_DataFrame_for_Table (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"DataFrame Selection", pos=wx.DefaultPosition, size=wx.Size(400, -1), style=wx.CAPTION | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(219, 219, 219))

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.main_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.main_panel.SetBackgroundColour(wx.Colour(219, 219, 219))

        main_panel_sizer = wx.BoxSizer(wx.VERTICAL)

        sub_panel_sizer_h1 = wx.BoxSizer(wx.HORIZONTAL)

        sub_panel_sizer_v1 = wx.BoxSizer(wx.VERTICAL)

        self.loaded_frames_StaticText = wx.StaticText(self.main_panel, wx.ID_ANY, u"Loaded DataFrames: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.loaded_frames_StaticText.Wrap(-1)
        sub_panel_sizer_v1.Add(self.loaded_frames_StaticText, 0, wx.ALL, 5)

        dataFrame_ListBoxChoices = []
        self.dataFrame_ListBox = wx.ListBox(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, dataFrame_ListBoxChoices, wx.LB_EXTENDED | wx.LB_HSCROLL | wx.LB_SORT)
        self.dataFrame_ListBox.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        sub_panel_sizer_v1.Add(self.dataFrame_ListBox, 0, wx.ALL | wx.EXPAND, 5)

        sub_panel_sizer_h1.Add(sub_panel_sizer_v1, 1, wx.EXPAND, 5)

        main_panel_sizer.Add(sub_panel_sizer_h1, 0, wx.EXPAND, 5)

        bSizer122 = wx.BoxSizer(wx.VERTICAL)

        self.delete_StaticTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"Display Selected DataFrame in Table: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.delete_StaticTxt.Wrap(-1)
        bSizer122.Add(self.delete_StaticTxt, 0, wx.ALL, 5)

        m_sdbSizer8 = wx.StdDialogButtonSizer()
        self.m_sdbSizer8OK = wx.Button(self.main_panel, wx.ID_OK)
        m_sdbSizer8.AddButton(self.m_sdbSizer8OK)
        self.m_sdbSizer8Cancel = wx.Button(self.main_panel, wx.ID_CANCEL)
        m_sdbSizer8.AddButton(self.m_sdbSizer8Cancel)
        m_sdbSizer8.Realize()
        bSizer122.Add(m_sdbSizer8, 1, wx.ALL | wx.EXPAND, 5)

        main_panel_sizer.Add(bSizer122, 0, wx.ALL | wx.EXPAND, 5)

        self.main_panel.SetSizer(main_panel_sizer)
        self.main_panel.Layout()
        main_panel_sizer.Fit(self.main_panel)
        main_sizer.Add(self.main_panel, 1, wx.EXPAND, 5)

        self.SetSizer(main_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.dataFrame_ListBox.Bind(wx.EVT_LISTBOX, self.create_tables)
        self.m_sdbSizer8Cancel.Bind(wx.EVT_BUTTON, self.ok_cancel)
        self.m_sdbSizer8OK.Bind(wx.EVT_BUTTON, self.on_ok)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def create_tables(self, event):
        pass

    def ok_cancel(self, event):
        pass

    def on_ok(self, event):
        pass
