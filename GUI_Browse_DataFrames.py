import wx


class GUI_Browse_DataFrames (wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"DataFrame Browser", pos=wx.DefaultPosition, size=wx.Size(400,215), style=wx.CAPTION | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)

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

        sub_panel_sizer_h2 = wx.BoxSizer(wx.HORIZONTAL)

        self.delete_StaticTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"Delete Selected DataFrame(s): ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.delete_StaticTxt.Wrap(-1)
        sub_panel_sizer_h2.Add(self.delete_StaticTxt, 0, wx.ALL, 5)

        self.delete_button = wx.Button(self.main_panel, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)
        sub_panel_sizer_h2.Add(self.delete_button, 0, wx.ALL, 5)

        main_panel_sizer.Add(sub_panel_sizer_h2, 0, wx.ALL | wx.EXPAND, 5)

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

        # Connect Events
        self.dataFrame_ListBox.Bind(wx.EVT_LISTBOX, self.add_selections_to_delete_list)
        self.delete_button.Bind(wx.EVT_BUTTON, self.on_delete)
        self.panel_ok_cancel_sizerCancel.Bind(wx.EVT_BUTTON, self.on_cancel_click)
        self.panel_ok_cancel_sizerOK.Bind(wx.EVT_BUTTON, self.on_ok_click)

    def __del__(self):
        pass

    def add_selections_to_delete_list(self, event):
        pass

    def on_delete(self, event):
        pass

    def on_cancel_click(self, event):
        pass

    def on_ok_click(self, event):
        pass
