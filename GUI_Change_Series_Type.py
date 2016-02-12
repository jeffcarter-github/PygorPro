import wx


class GUI_Change_Series_Type(wx.Frame):

    def __init__(self, lst_of_dataFrames):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=u"Change Series Type", pos=wx.DefaultPosition, size=wx.Size(400, 430), style=wx.CAPTION | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.main_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.main_panel.SetBackgroundColour(wx.Colour(219, 219, 219))

        main_panel_sizer = wx.BoxSizer(wx.VERTICAL)

        sub_panel_sizer_0 = wx.BoxSizer(wx.HORIZONTAL)

        self.dataFrame_StaticTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"DataFrame: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataFrame_StaticTxt.Wrap(-1)
        sub_panel_sizer_0.Add(self.dataFrame_StaticTxt, 0, wx.ALL, 5)

        dataFrame_ChoiceBoxChoices = lst_of_dataFrames
        self.dataFrame_ChoiceBox = wx.Choice(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(225, -1), dataFrame_ChoiceBoxChoices, 0)
        self.dataFrame_ChoiceBox.SetSelection(0)
        sub_panel_sizer_0.Add(self.dataFrame_ChoiceBox, 0, wx.ALL, 5)

        main_panel_sizer.Add(sub_panel_sizer_0, 0, wx.EXPAND, 5)

        sub_panel_sizer_1 = wx.FlexGridSizer(3, 2, 0, 0)
        sub_panel_sizer_1.SetFlexibleDirection(wx.BOTH)
        sub_panel_sizer_1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Series_StaticsTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"Series: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Series_StaticsTxt.Wrap(-1)
        sub_panel_sizer_1.Add(self.Series_StaticsTxt, 0, wx.ALL, 5)

        self.m_staticText20 = wx.StaticText(self.main_panel, wx.ID_ANY, u"Current Data Type:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)
        sub_panel_sizer_1.Add(self.m_staticText20, 0, wx.ALL, 5)

        Series_ListBoxChoices = []
        self.Series_ListBox = wx.ListBox(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), Series_ListBoxChoices, wx.LB_EXTENDED | wx.LB_HSCROLL | wx.LB_SORT)
        self.Series_ListBox.SetMinSize(wx.Size(200, -1))

        sub_panel_sizer_1.Add(self.Series_ListBox, 0, wx.ALL | wx.EXPAND, 5)

        m_listBox6Choices = []
        self.m_listBox6 = wx.ListBox(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox6Choices, wx.LB_SORT)
        self.m_listBox6.SetMinSize(wx.Size(150, -1))

        sub_panel_sizer_1.Add(self.m_listBox6, 0, wx.ALL, 5)

        main_panel_sizer.Add(sub_panel_sizer_1, 0, wx.ALL | wx.EXPAND, 5)

        sub_panel_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)

        self.add_button = wx.Button(self.main_panel, wx.ID_ANY, u"Add...", wx.DefaultPosition, wx.DefaultSize, 0)
        sub_panel_sizer_2.Add(self.add_button, 0, wx.ALL, 5)

        main_panel_sizer.Add(sub_panel_sizer_2, 0, wx.ALIGN_CENTER, 5)

        sub_panel_sizer_3 = wx.BoxSizer(wx.VERTICAL)

        sub_label_sizer = wx.FlexGridSizer(1, 3, 0, 0)
        sub_label_sizer.SetFlexibleDirection(wx.BOTH)
        sub_label_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.series_StaticTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"Series:", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.series_StaticTxt.Wrap(-1)
        self.series_StaticTxt.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.series_StaticTxt.SetMinSize(wx.Size(165, -1))

        sub_label_sizer.Add(self.series_StaticTxt, 0, wx.ALL, 5)

        self.current_StaticTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"Current Type:", wx.DefaultPosition, wx.Size(100, -1), 0)
        self.current_StaticTxt.Wrap(-1)
        self.current_StaticTxt.SetMinSize(wx.Size(100, -1))

        sub_label_sizer.Add(self.current_StaticTxt, 0, wx.ALL, 5)

        self.new_StaticTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"New Type:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.new_StaticTxt.Wrap(-1)
        self.new_StaticTxt.SetMinSize(wx.Size(100, -1))

        sub_label_sizer.Add(self.new_StaticTxt, 0, wx.ALL, 5)

        sub_panel_sizer_3.Add(sub_label_sizer, 0, wx.EXPAND, 5)

        flexGrid_sizer = wx.FlexGridSizer(5, 3, 0, 0)
        flexGrid_sizer.SetFlexibleDirection(wx.BOTH)
        flexGrid_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.name_TxtCtrl_0 = wx.TextCtrl(self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1,-1), wx.TE_READONLY)
        self.name_TxtCtrl_0.SetMinSize(wx.Size(165, -1))

        flexGrid_sizer.Add(self.name_TxtCtrl_0, 0, wx.ALL, 5)

        self.current_TxtCtrl_0 = wx.TextCtrl(self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        self.current_TxtCtrl_0.SetMinSize(wx.Size(100, -1))

        flexGrid_sizer.Add(self.current_TxtCtrl_0, 0, wx.ALL, 5)

        new_ChoiceBox_0Choices = [ u"none", u"float", u"int", u"string", u"boolean" ]
        self.new_ChoiceBox_0 = wx.Choice(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, new_ChoiceBox_0Choices, 0)
        self.new_ChoiceBox_0.SetSelection(0)
        self.new_ChoiceBox_0.SetMinSize(wx.Size(100, -1))

        flexGrid_sizer.Add(self.new_ChoiceBox_0, 0, wx.ALL, 5)

        self.name_TxtCtrl_1 = wx.TextCtrl(self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), wx.TE_READONLY | wx.TE_RICH)
        self.name_TxtCtrl_1.SetMinSize(wx.Size(165, -1))

        flexGrid_sizer.Add(self.name_TxtCtrl_1, 0, wx.ALL, 5)

        self.current_TxtCtrl_1 = wx.TextCtrl(self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        flexGrid_sizer.Add(self.current_TxtCtrl_1, 0, wx.ALL, 5)

        new_ChoiceBox_1Choices = [u"none", u"float", u"int", u"string", u"boolean"]
        self.new_ChoiceBox_1 = wx.Choice(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, new_ChoiceBox_1Choices, 0)
        self.new_ChoiceBox_1.SetSelection(0)
        self.new_ChoiceBox_1.SetMinSize(wx.Size(100, -1))

        flexGrid_sizer.Add(self.new_ChoiceBox_1, 0, wx.ALL, 5)

        self.name_TxtCtrl_2 = wx.TextCtrl(self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), wx.TE_READONLY)
        self.name_TxtCtrl_2.SetMinSize(wx.Size(165, -1))

        flexGrid_sizer.Add(self.name_TxtCtrl_2, 0, wx.ALL, 5)

        self.current_TxtCtrl_2 = wx.TextCtrl(self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        flexGrid_sizer.Add(self.current_TxtCtrl_2, 0, wx.ALL, 5)

        new_ChoiceBox_2Choices = [u"none", u"float", u"int", u"string", u"boolean"]
        self.new_ChoiceBox_2 = wx.Choice(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, new_ChoiceBox_2Choices, 0)
        self.new_ChoiceBox_2.SetSelection(0)
        self.new_ChoiceBox_2.SetMinSize(wx.Size(100, -1))

        flexGrid_sizer.Add(self.new_ChoiceBox_2, 0, wx.ALL, 5)

        self.name_TxtCtrl_3 = wx.TextCtrl(self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), wx.TE_READONLY)
        self.name_TxtCtrl_3.SetMinSize(wx.Size(165, -1))

        flexGrid_sizer.Add(self.name_TxtCtrl_3, 0, wx.ALL, 5)

        self.current_TxtCtrl_3 = wx.TextCtrl(self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        flexGrid_sizer.Add(self.current_TxtCtrl_3, 0, wx.ALL, 5)

        new_ChoiceBox_3Choices = [ u"none", u"float", u"int", u"string", u"boolean" ]
        self.new_ChoiceBox_3 = wx.Choice(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, new_ChoiceBox_3Choices, 0)
        self.new_ChoiceBox_3.SetSelection(0)
        self.new_ChoiceBox_3.SetMinSize(wx.Size(100, -1))

        flexGrid_sizer.Add(self.new_ChoiceBox_3, 0, wx.ALL, 5)

        self.name_TxtCtrl_4 = wx.TextCtrl(self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), wx.TE_READONLY)
        self.name_TxtCtrl_4.SetMinSize(wx.Size(165, -1))

        flexGrid_sizer.Add(self.name_TxtCtrl_4, 0, wx.ALL, 5)

        self.current_TxtCtrl_4 = wx.TextCtrl(self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        flexGrid_sizer.Add(self.current_TxtCtrl_4, 0, wx.ALL, 5)

        new_ChoiceBox_4Choices = [ u"none", u"float", u"int", u"string", u"boolean" ]
        self.new_ChoiceBox_4 = wx.Choice(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, new_ChoiceBox_4Choices, 0)
        self.new_ChoiceBox_4.SetSelection(0)
        self.new_ChoiceBox_4.SetMinSize(wx.Size(100, -1))

        flexGrid_sizer.Add(self.new_ChoiceBox_4, 0, wx.ALL, 5)

        sub_panel_sizer_3.Add(flexGrid_sizer, 1, wx.EXPAND, 5)

        main_panel_sizer.Add(sub_panel_sizer_3, 0, wx.EXPAND, 5)

        bSizer24 = wx.BoxSizer(wx.VERTICAL)

        m_sdbSizer3 = wx.StdDialogButtonSizer()
        self.m_sdbSizer3OK = wx.Button(self.main_panel, wx.ID_OK)
        m_sdbSizer3.AddButton(self.m_sdbSizer3OK)
        self.m_sdbSizer3Cancel = wx.Button(self.main_panel, wx.ID_CANCEL)
        m_sdbSizer3.AddButton(self.m_sdbSizer3Cancel)
        m_sdbSizer3.Realize()
        bSizer24.Add(m_sdbSizer3, 1, wx.ALL | wx.EXPAND, 5)

        main_panel_sizer.Add(bSizer24, 1, wx.EXPAND, 5)

        self.main_panel.SetSizer(main_panel_sizer)
        self.main_panel.Layout()
        main_panel_sizer.Fit(self.main_panel)
        main_sizer.Add(self.main_panel, 1, wx.EXPAND, 5)

        self.SetSizer(main_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.dataFrame_ChoiceBox.Bind(wx.EVT_CHOICE, self.on_dataFrame_choice)
        self.Series_ListBox.Bind(wx.EVT_LISTBOX, self.on_series_selection)
        self.add_button.Bind(wx.EVT_BUTTON, self.add_selections_to_gui)
        self.m_sdbSizer3Cancel.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.m_sdbSizer3OK.Bind(wx.EVT_BUTTON, self.on_ok)

        self.Show(True)

    # Virtual event handlers, overide them in your derived class
    def on_dataFrame_choice(self, event):
        pass

    def on_series_selection(self, event):
        pass

    def add_selections_to_gui(self, event):
        pass

    def on_cancel(self, event):
        pass

    def on_ok(self, event):
        pass
