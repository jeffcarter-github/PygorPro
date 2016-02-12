import wx


class GUI_Browse_DataFrames(wx.Frame):
    def __init__(self, dataFrame_lst):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=u"DataFrame Browser", size=wx.Size(400, 325), style=wx.CAPTION  |  wx.FRAME_FLOAT_ON_PARENT  |  wx.TAB_TRAVERSAL)

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

        dataFrame_ListBoxChoices = dataFrame_lst
        self.dataFrame_ListBox = wx.ListBox(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, dataFrame_ListBoxChoices, wx.LB_EXTENDED | wx.LB_HSCROLL | wx.LB_NEEDED_SB | wx.LB_SORT)
        self.dataFrame_ListBox.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        sub_panel_sizer_v1.Add(self.dataFrame_ListBox, 0, wx.ALL | wx.EXPAND, 5)

        sub_panel_sizer_h1.Add(sub_panel_sizer_v1, 1, wx.EXPAND, 5)

        main_panel_sizer.Add(sub_panel_sizer_h1, 0, wx.EXPAND, 5)

        sub_panel_sizer_h2 = wx.BoxSizer(wx.HORIZONTAL)

        self.delete_button = wx.Button(self.main_panel, wx.ID_ANY, u"Add to List for Deletion...", wx.DefaultPosition, wx.DefaultSize, 0)
        sub_panel_sizer_h2.Add(self.delete_button, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        main_panel_sizer.Add(sub_panel_sizer_h2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer117 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText54 = wx.StaticText(self.main_panel, wx.ID_ANY, u"List for Deletion: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText54.Wrap(-1)
        bSizer117.Add(self.m_staticText54, 0, wx.ALL, 5)

        list_for_deletionChoices = []
        self.list_for_deletion = wx.ListBox(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_for_deletionChoices, wx.LB_HSCROLL | wx.LB_NEEDED_SB)
        self.list_for_deletion.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        bSizer117.Add(self.list_for_deletion, 0, wx.ALL | wx.EXPAND, 5)

        main_panel_sizer.Add(bSizer117, 0, wx.EXPAND, 5)

        panel_ok_cancel_sizer = wx.StdDialogButtonSizer()
        self.panel_ok_cancel_sizerOK = wx.Button(self.main_panel, wx.ID_OK)
        panel_ok_cancel_sizer.AddButton(self.panel_ok_cancel_sizerOK)
        self.panel_ok_cancel_sizerCancel = wx.Button(self.main_panel, wx.ID_CANCEL)
        panel_ok_cancel_sizer.AddButton(self.panel_ok_cancel_sizerCancel)
        panel_ok_cancel_sizer.Realize()
        main_panel_sizer.Add(panel_ok_cancel_sizer, 1, wx.EXPAND, 5)

        self.main_panel.SetSizer(main_panel_sizer)
        self.main_panel.Layout()
        main_panel_sizer.Fit(self.main_panel)
        main_sizer.Add(self.main_panel, 1, wx.EXPAND, 5)

        self.SetSizer(main_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        self.delete_button.Bind(wx.EVT_BUTTON, self.on_add_to_list)
        self.panel_ok_cancel_sizerCancel.Bind(wx.EVT_BUTTON, self.on_cancel_click)
        self.panel_ok_cancel_sizerOK.Bind(wx.EVT_BUTTON, self.on_ok_click)

        self.Show(True)

    # Virtual event handlers, overide them in your derived class
    def on_add_to_list(self, event):
        pass

    def on_cancel_click(self, event):
        pass

    def on_ok_click(self, event):
        pass
