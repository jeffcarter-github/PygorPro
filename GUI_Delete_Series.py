import wx


class GUI_Delete_Series (wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Delete Series", pos=wx.DefaultPosition, size=wx.Size(350, 225), style=wx.CAPTION | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.main_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.main_panel.SetBackgroundColour(wx.Colour(219, 219, 219))

        main_panel_sizer = wx.BoxSizer(wx.VERTICAL)

        sub_panel_sizer_1 = wx.FlexGridSizer(2, 2, 0, 0)
        sub_panel_sizer_1.SetFlexibleDirection(wx.BOTH)
        sub_panel_sizer_1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.dataFrame_StaticTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"DataFrame: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataFrame_StaticTxt.Wrap(-1)
        sub_panel_sizer_1.Add(self.dataFrame_StaticTxt, 0, wx.ALL, 5)

        dataFrame_ChoiceBoxChoices = []
        self.dataFrame_ChoiceBox = wx.Choice(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(225, -1), dataFrame_ChoiceBoxChoices, 0)
        self.dataFrame_ChoiceBox.SetSelection(0)
        sub_panel_sizer_1.Add(self.dataFrame_ChoiceBox, 0, wx.ALL, 5)

        self.Series_StaticsTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"Series: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Series_StaticsTxt.Wrap(-1)
        sub_panel_sizer_1.Add(self.Series_StaticsTxt, 0, wx.ALL, 5)

        Series_ListBoxChoices = []
        self.Series_ListBox = wx.ListBox(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(225, -1), Series_ListBoxChoices, wx.LB_EXTENDED | wx.LB_HSCROLL)
        sub_panel_sizer_1.Add(self.Series_ListBox, 0, wx.ALL | wx.EXPAND, 5)

        main_panel_sizer.Add(sub_panel_sizer_1, 0, wx.ALL | wx.EXPAND, 5)

        sub_panel_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText27 = wx.StaticText(self.main_panel, wx.ID_ANY, u"Delete Selected Series: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText27.Wrap(-1)
        sub_panel_sizer_2.Add(self.m_staticText27, 0, wx.ALL, 5)

        self.delete_button = wx.Button(self.main_panel, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)
        sub_panel_sizer_2.Add(self.delete_button, 0, wx.ALL | wx.EXPAND, 5)

        main_panel_sizer.Add(sub_panel_sizer_2, 1, wx.ALIGN_CENTER | wx.EXPAND, 5)

        sub_panel_sizer_3 = wx.BoxSizer(wx.VERTICAL)

        m_sdbSizer3 = wx.StdDialogButtonSizer()
        self.m_sdbSizer3OK = wx.Button(self.main_panel, wx.ID_OK)
        m_sdbSizer3.AddButton(self.m_sdbSizer3OK)
        self.m_sdbSizer3Cancel = wx.Button(self.main_panel, wx.ID_CANCEL)
        m_sdbSizer3.AddButton(self.m_sdbSizer3Cancel)
        m_sdbSizer3.Realize()
        sub_panel_sizer_3.Add(m_sdbSizer3, 1, wx.ALL | wx.EXPAND, 5)

        main_panel_sizer.Add(sub_panel_sizer_3, 1, wx.EXPAND, 5)

        self.main_panel.SetSizer(main_panel_sizer)
        self.main_panel.Layout()
        main_panel_sizer.Fit(self.main_panel)
        main_sizer.Add(self.main_panel, 1, wx.EXPAND, 5)

        self.SetSizer(main_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.dataFrame_ChoiceBox.Bind(wx.EVT_CHOICE, self.on_dataFrame_choice)
        self.delete_button.Bind(wx.EVT_BUTTON, self.delete_selections)
        self.m_sdbSizer3Cancel.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.m_sdbSizer3OK.Bind(wx.EVT_BUTTON, self.on_ok)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_dataFrame_choice(self, event):
        pass

    def delete_selections(self, event):
        pass

    def on_cancel(self, event):
        pass

    def on_ok(self, event):
        pass
