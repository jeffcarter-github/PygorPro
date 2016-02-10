import wx


class GUI_Selection_Plot(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"New 2D Graph", pos=wx.DefaultPosition, size=wx.Size(400, 525), style=wx.CAPTION | wx.FRAME_FLOAT_ON_PARENT)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.main_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,-1), 0)
        self.main_panel.SetBackgroundColour(wx.Colour(219, 219, 219))
        self.main_panel.SetToolTipString(u"tooltip...")

        main_panel_sizer = wx.BoxSizer(wx.VERTICAL)

        series_selection_sizer = wx.BoxSizer(wx.VERTICAL)

        series_selection_sub_fg_sizer = wx.FlexGridSizer(5, 2, 0, 0)
        series_selection_sub_fg_sizer.SetFlexibleDirection(wx.BOTH)
        series_selection_sub_fg_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.y_axis_staticTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"Y Series", wx.DefaultPosition, wx.DefaultSize, 0)
        self.y_axis_staticTxt.Wrap(-1)
        self.y_axis_staticTxt.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        series_selection_sub_fg_sizer.Add(self.y_axis_staticTxt, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.x_axis_staticText = wx.StaticText(self.main_panel, wx.ID_ANY, u"X Series", wx.DefaultPosition, wx.DefaultSize, 0)
        self.x_axis_staticText.Wrap(-1)
        series_selection_sub_fg_sizer.Add(self.x_axis_staticText, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        y_DataFrame_ChoiceBoxChoices = []
        self.y_DataFrame_ChoiceBox = wx.Choice(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, y_DataFrame_ChoiceBoxChoices, 0)
        self.y_DataFrame_ChoiceBox.SetSelection(0)
        series_selection_sub_fg_sizer.Add(self.y_DataFrame_ChoiceBox, 0, wx.ALL, 5)

        x_DataFrame_ChoiceBoxChoices = []
        self.x_DataFrame_ChoiceBox = wx.Choice(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, x_DataFrame_ChoiceBoxChoices, 0)
        self.x_DataFrame_ChoiceBox.SetSelection(0)
        series_selection_sub_fg_sizer.Add(self.x_DataFrame_ChoiceBox, 0, wx.ALL, 5)

        y_Series_ListBoxChoices = []
        self.y_Series_ListBox = wx.ListBox(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, y_Series_ListBoxChoices, wx.LB_HSCROLL | wx.LB_NEEDED_SB | wx.LB_SINGLE | wx.LB_SORT)
        self.y_Series_ListBox.SetMinSize(wx.Size(-1,150))
        self.y_Series_ListBox.SetMaxSize(wx.Size(-1,150))

        series_selection_sub_fg_sizer.Add(self.y_Series_ListBox, 0, wx.ALL | wx.EXPAND, 5)

        x_Series_ListBoxChoices = []
        self.x_Series_ListBox = wx.ListBox(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, x_Series_ListBoxChoices, wx.LB_HSCROLL | wx.LB_MULTIPLE | wx.LB_NEEDED_SB | wx.LB_SORT)
        self.x_Series_ListBox.SetMinSize(wx.Size(-1,150))
        self.x_Series_ListBox.SetMaxSize(wx.Size(-1,150))

        series_selection_sub_fg_sizer.Add(self.x_Series_ListBox, 0, wx.ALL | wx.EXPAND, 5)

        sub_sizer_left = wx.BoxSizer(wx.HORIZONTAL)

        self.y_axis_label_StaticTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"Axis: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.y_axis_label_StaticTxt.Wrap(-1)
        sub_sizer_left.Add(self.y_axis_label_StaticTxt, 0, wx.ALL, 5)

        y_axis_ChoiceBoxChoices = [ u"Left", u"Right" ]
        self.y_axis_ChoiceBox = wx.Choice(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(100,-1), y_axis_ChoiceBoxChoices, 0)
        self.y_axis_ChoiceBox.SetSelection(0)
        sub_sizer_left.Add(self.y_axis_ChoiceBox, 0, wx.ALL, 5)

        series_selection_sub_fg_sizer.Add(sub_sizer_left, 1, wx.EXPAND, 5)

        sub_sizer_right = wx.BoxSizer(wx.HORIZONTAL)

        self.x_axis_label_StaticTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"Axis: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.x_axis_label_StaticTxt.Wrap(-1)
        sub_sizer_right.Add(self.x_axis_label_StaticTxt, 0, wx.ALL, 5)

        x_axis_ChoiceBoxChoices = [ u"Bottom", u"Top" ]
        self.x_axis_ChoiceBox = wx.Choice(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(100,-1), x_axis_ChoiceBoxChoices, 0)
        self.x_axis_ChoiceBox.SetSelection(0)
        sub_sizer_right.Add(self.x_axis_ChoiceBox, 0, wx.ALL, 5)

        series_selection_sub_fg_sizer.Add(sub_sizer_right, 1, wx.EXPAND, 5)

        series_selection_sizer.Add(series_selection_sub_fg_sizer, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        main_panel_sizer.Add(series_selection_sizer, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        add_option_sizer = wx.BoxSizer(wx.VERTICAL)

        self.add_button = wx.Button(self.main_panel, wx.ID_ANY, u"Add...", wx.DefaultPosition, wx.DefaultSize, 0)
        add_option_sizer.Add(self.add_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        main_panel_sizer.Add(add_option_sizer, 0, wx.EXPAND, 5)

        plot_options_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.plot_title_StaticTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"Title: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.plot_title_StaticTxt.Wrap(-1)
        plot_options_sizer.Add(self.plot_title_StaticTxt, 0, wx.ALL, 5)

        self.plot_title_TxtCtrl = wx.TextCtrl(self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        plot_options_sizer.Add(self.plot_title_TxtCtrl, 0, wx.ALL, 5)

        self.plot_style_StaticTxt = wx.StaticText(self.main_panel, wx.ID_ANY, u"Style: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.plot_style_StaticTxt.Wrap(-1)
        plot_options_sizer.Add(self.plot_style_StaticTxt, 0, wx.ALL, 5)

        plot_style_TxtCtrlChoices = [ u"Line", u"Scatter" ]
        self.plot_style_TxtCtrl = wx.Choice(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, plot_style_TxtCtrlChoices, 0)
        self.plot_style_TxtCtrl.SetSelection(0)
        plot_options_sizer.Add(self.plot_style_TxtCtrl, 0, wx.ALL, 5)

        main_panel_sizer.Add(plot_options_sizer, 0, wx.EXPAND, 5)

        dialog_box_sizer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText50 = wx.StaticText(self.main_panel, wx.ID_ANY, u"Display:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText50.Wrap(-1)
        dialog_box_sizer.Add(self.m_staticText50, 0, wx.ALL, 5)

        self.dialog_TxtCtrl = wx.TextCtrl(self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1,100), wx.HSCROLL | wx.TE_READONLY | wx.VSCROLL)
        self.dialog_TxtCtrl.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        dialog_box_sizer.Add(self.dialog_TxtCtrl, 0, wx.ALL | wx.EXPAND, 5)

        main_panel_sizer.Add(dialog_box_sizer, 0, wx.ALIGN_TOP | wx.EXPAND, 5)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        button_sub_sizer = wx.StdDialogButtonSizer()
        self.button_sub_sizerOK = wx.Button(self.main_panel, wx.ID_OK)
        button_sub_sizer.AddButton(self.button_sub_sizerOK)
        self.button_sub_sizerCancel = wx.Button(self.main_panel, wx.ID_CANCEL)
        button_sub_sizer.AddButton(self.button_sub_sizerCancel)
        button_sub_sizer.Realize()
        button_sizer.Add(button_sub_sizer, 1, wx.ALL, 5)

        main_panel_sizer.Add(button_sizer, 0, wx.EXPAND, 5)

        self.main_panel.SetSizer(main_panel_sizer)
        self.main_panel.Layout()
        main_panel_sizer.Fit(self.main_panel)
        main_sizer.Add(self.main_panel, 1, wx.EXPAND, 5)

        self.SetSizer(main_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.y_DataFrame_ChoiceBox.Bind(wx.EVT_CHOICE, self.on_choice_ySeries_dataFrame)
        self.y_DataFrame_ChoiceBox.Bind(wx.EVT_LEAVE_WINDOW, self.calculate_ySeries_options)
        self.x_DataFrame_ChoiceBox.Bind(wx.EVT_CHOICE, self.on_choice_xSeries_dataFrame)
        self.x_DataFrame_ChoiceBox.Bind(wx.EVT_LEAVE_WINDOW, self.calculate_xSeries_options)
        self.y_Series_ListBox.Bind(wx.EVT_LISTBOX_DCLICK, self.on_choice_ySeries)
        self.x_Series_ListBox.Bind(wx.EVT_LISTBOX_DCLICK, self.on_choice_xSeries)
        self.y_axis_ChoiceBox.Bind(wx.EVT_CHOICE, self.on_choice_y_axis_position)
        self.x_axis_ChoiceBox.Bind(wx.EVT_CHOICE, self.on_choice_x_axis_position)
        self.add_button.Bind(wx.EVT_BUTTON, self.on_add_series_pair)
        self.plot_style_TxtCtrl.Bind(wx.EVT_CHOICE, self.on_choice_plot_style)
        self.button_sub_sizerCancel.Bind(wx.EVT_BUTTON, self.on_click_Cancel)
        self.button_sub_sizerOK.Bind(wx.EVT_BUTTON, self.on_click_OK)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_choice_ySeries_dataFrame(self, event):
        pass

    def calculate_ySeries_options(self, event):
        pass

    def on_choice_xSeries_dataFrame(self, event):
        pass

    def calculate_xSeries_options(self, event):
        pass

    def on_choice_ySeries(self, event):
        pass

    def on_choice_xSeries(self, event):
        pass

    def on_choice_y_axis_position(self, event):
        pass

    def on_choice_x_axis_position(self, event):
        pass

    def on_add_series_pair(self, event):
        pass

    def on_choice_plot_style(self, event):
        pass

    def on_click_Cancel(self, event):
        pass

    def on_click_OK(self, event):
        pass
