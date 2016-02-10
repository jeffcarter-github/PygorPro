import wx


class GUI_Curve_Fitting (wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Curve Fitting", pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.CAPTION | wx.TAB_TRAVERSAL)
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(219, 219, 219))
        
        bSizer33 = wx.BoxSizer(wx.VERTICAL)
        
        self.curve_fitting_notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.function_data_panel = wx.Panel(self.curve_fitting_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer64 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer65 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer68 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText39 = wx.StaticText(self.function_data_panel, wx.ID_ANY, u"Function", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText39.Wrap(-1)
        bSizer68.Add(self.m_staticText39, 0, wx.ALL, 5)
        
        self.m_panel22 = wx.Panel(self.function_data_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer71 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer72 = wx.BoxSizer(wx.VERTICAL)
        
        m_choice27Choices = [ u"Line", u"Polynomial 2", u"Polynomial 3", u"Polynomial 4", u"Polynomial 5", u"Polynomial 6", u"Guassian", u"Exponential", u"Double Exponential", u"Lorentzen", u"Sigmoidal", u"Sinusoidal", u"Power", u"LogNormal" ]
        self.m_choice27 = wx.Choice(self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice27Choices, 0)
        self.m_choice27.SetSelection(0)
        self.m_choice27.SetMinSize(wx.Size(150,-1))
        
        bSizer72.Add(self.m_choice27, 0, wx.ALL, 5)
        
        bSizer71.Add(bSizer72, 1, wx.EXPAND, 5)
        
        self.m_panel22.SetSizer(bSizer71)
        self.m_panel22.Layout()
        bSizer71.Fit(self.m_panel22)
        bSizer68.Add(self.m_panel22, 0, wx.EXPAND | wx.ALL, 5)
        
        bSizer65.Add(bSizer68, 0, wx.EXPAND, 5)
        
        bSizer69 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText40 = wx.StaticText(self.function_data_panel, wx.ID_ANY, u"Y Data", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText40.Wrap(-1)
        bSizer69.Add(self.m_staticText40, 0, wx.ALL, 5)
        
        bSizer77 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel24 = wx.Panel(self.function_data_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer79 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer80 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText43 = wx.StaticText(self.m_panel24, wx.ID_ANY, u"DataFrame", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText43.Wrap(-1)
        self.m_staticText43.SetMinSize(wx.Size(75,-1))
        
        bSizer80.Add(self.m_staticText43, 0, wx.ALL, 5)
        
        m_choice28Choices = []
        self.m_choice28 = wx.Choice(self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice28Choices, 0)
        self.m_choice28.SetSelection(0)
        bSizer80.Add(self.m_choice28, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer79.Add(bSizer80, 0, wx.EXPAND, 5)
        
        bSizer81 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText45 = wx.StaticText(self.m_panel24, wx.ID_ANY, u"Series", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText45.Wrap(-1)
        self.m_staticText45.SetMinSize(wx.Size(75,-1))
        
        bSizer81.Add(self.m_staticText45, 0, wx.ALL, 5)
        
        m_choice29Choices = []
        self.m_choice29 = wx.Choice(self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice29Choices, 0)
        self.m_choice29.SetSelection(0)
        bSizer81.Add(self.m_choice29, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer79.Add(bSizer81, 0, wx.EXPAND, 5)
        
        self.m_panel24.SetSizer(bSizer79)
        self.m_panel24.Layout()
        bSizer79.Fit(self.m_panel24)
        bSizer77.Add(self.m_panel24, 0, wx.EXPAND  | wx.ALL, 5)
        
        bSizer69.Add(bSizer77, 0, wx.EXPAND, 5)
        
        self.m_staticText42 = wx.StaticText(self.function_data_panel, wx.ID_ANY, u"X Data", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText42.Wrap(-1)
        bSizer69.Add(self.m_staticText42, 0, wx.ALL, 5)
        
        bSizer78 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel23 = wx.Panel(self.function_data_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer82 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer83 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText47 = wx.StaticText(self.m_panel23, wx.ID_ANY, u"DataFrame", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText47.Wrap(-1)
        self.m_staticText47.SetMinSize(wx.Size(75,-1))
        
        bSizer83.Add(self.m_staticText47, 0, wx.ALL, 5)
        
        m_choice31Choices = []
        self.m_choice31 = wx.Choice(self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice31Choices, 0)
        self.m_choice31.SetSelection(0)
        bSizer83.Add(self.m_choice31, 0, wx.ALL, 5)
        
        bSizer82.Add(bSizer83, 1, wx.EXPAND, 5)
        
        bSizer84 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText46 = wx.StaticText(self.m_panel23, wx.ID_ANY, u"Series", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText46.Wrap(-1)
        self.m_staticText46.SetMinSize(wx.Size(75,-1))
        
        bSizer84.Add(self.m_staticText46, 0, wx.ALL, 5)
        
        m_choice32Choices = []
        self.m_choice32 = wx.Choice(self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice32Choices, 0)
        self.m_choice32.SetSelection(0)
        bSizer84.Add(self.m_choice32, 0, wx.ALL, 5)
        
        bSizer82.Add(bSizer84, 1, wx.EXPAND, 5)
        
        self.m_panel23.SetSizer(bSizer82)
        self.m_panel23.Layout()
        bSizer82.Fit(self.m_panel23)
        bSizer78.Add(self.m_panel23, 1, wx.EXPAND  | wx.ALL, 5)
        
        bSizer69.Add(bSizer78, 1, wx.EXPAND, 5)
        
        bSizer65.Add(bSizer69, 1, wx.EXPAND, 5)
        
        bSizer70 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText48 = wx.StaticText(self.function_data_panel, wx.ID_ANY, u"Equation", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText48.Wrap(-1)
        bSizer70.Add(self.m_staticText48, 0, wx.ALL, 5)
        
        self.m_panel25 = wx.Panel(self.function_data_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer85 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_textCtrl67 = wx.TextCtrl(self.m_panel25, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        self.m_textCtrl67.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        
        bSizer85.Add(self.m_textCtrl67, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_panel25.SetSizer(bSizer85)
        self.m_panel25.Layout()
        bSizer85.Fit(self.m_panel25)
        bSizer70.Add(self.m_panel25, 0, wx.EXPAND  | wx.ALL, 5)
        
        bSizer65.Add(bSizer70, 1, wx.EXPAND, 5)
        
        bSizer64.Add(bSizer65, 0, wx.EXPAND, 5)
        
        bSizer66 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer64.Add(bSizer66, 1, wx.EXPAND, 5)
        
        bSizer67 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer64.Add(bSizer67, 1, wx.EXPAND, 5)
        
        self.function_data_panel.SetSizer(bSizer64)
        self.function_data_panel.Layout()
        bSizer64.Fit(self.function_data_panel)
        self.curve_fitting_notebook.AddPage(self.function_data_panel, u"Function and Data", False)
        self.data_options_panel = wx.Panel(self.curve_fitting_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer34 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer36 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer35 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText30 = wx.StaticText(self.data_options_panel, wx.ID_ANY, u"Range", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        bSizer35.Add(self.m_staticText30, 0, wx.ALL, 5)
        
        self.m_panel12 = wx.Panel(self.data_options_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer40 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel16 = wx.Panel(self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer42 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel17 = wx.Panel(self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer43 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer44 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText31 = wx.StaticText(self.m_panel17, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        self.m_staticText31.SetMinSize(wx.Size(75,-1))
        
        bSizer44.Add(self.m_staticText31, 0, wx.ALL, 5)
        
        self.m_staticText32 = wx.StaticText(self.m_panel17, wx.ID_ANY, u"End", wx.DefaultPosition, wx.Size(-1,-1), 0)
        self.m_staticText32.Wrap(-1)
        self.m_staticText32.SetMinSize(wx.Size(75,-1))
        
        bSizer44.Add(self.m_staticText32, 0, wx.ALL, 5)
        
        bSizer43.Add(bSizer44, 0, wx.EXPAND, 5)
        
        bSizer45 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_textCtrl62 = wx.TextCtrl(self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl62.SetMinSize(wx.Size(75,-1))
        
        bSizer45.Add(self.m_textCtrl62, 0, wx.ALL, 5)
        
        self.m_textCtrl63 = wx.TextCtrl(self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl63.SetMinSize(wx.Size(75,-1))
        
        bSizer45.Add(self.m_textCtrl63, 0, wx.ALL, 5)
        
        bSizer43.Add(bSizer45, 0, wx.EXPAND, 5)
        
        self.m_panel17.SetSizer(bSizer43)
        self.m_panel17.Layout()
        bSizer43.Fit(self.m_panel17)
        bSizer42.Add(self.m_panel17, 0, wx.EXPAND  | wx.ALL, 5)
        
        self.m_panel16.SetSizer(bSizer42)
        self.m_panel16.Layout()
        bSizer42.Fit(self.m_panel16)
        bSizer40.Add(self.m_panel16, 0, wx.EXPAND  | wx.ALL, 5)
        
        bSizer41 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_button7 = wx.Button(self.m_panel12, wx.ID_ANY, u"Cursors", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer41.Add(self.m_button7, 0, wx.ALL, 5)
        
        self.m_button8 = wx.Button(self.m_panel12, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer41.Add(self.m_button8, 0, wx.ALL, 5)
        
        bSizer40.Add(bSizer41, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        
        self.m_panel12.SetSizer(bSizer40)
        self.m_panel12.Layout()
        bSizer40.Fit(self.m_panel12)
        bSizer35.Add(self.m_panel12, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer36.Add(bSizer35, 1, wx.EXPAND, 5)
        
        bSizer37 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel14 = wx.Panel(self.data_options_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer46 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText33 = wx.StaticText(self.m_panel14, wx.ID_ANY, u"Weighting", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText33.Wrap(-1)
        bSizer46.Add(self.m_staticText33, 0, wx.ALL, 5)
        
        bSizer47 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel18 = wx.Panel(self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer48 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer49 = wx.BoxSizer(wx.VERTICAL)
        
        m_choice24Choices = [ u"_none_" ]
        self.m_choice24 = wx.Choice(self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice24Choices, 0)
        self.m_choice24.SetSelection(0)
        bSizer49.Add(self.m_choice24, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer48.Add(bSizer49, 0, wx.EXPAND, 5)
        
        bSizer50 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer51 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText34 = wx.StaticText(self.m_panel18, wx.ID_ANY, u"Series Contains:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)
        bSizer51.Add(self.m_staticText34, 0, wx.ALL, 5)
        
        bSizer50.Add(bSizer51, 0, wx.EXPAND, 5)
        
        bSizer52 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel19 = wx.Panel(self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer53 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_radioBtn1 = wx.RadioButton(self.m_panel19, wx.ID_ANY, u"Standard Deviation", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_radioBtn1.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        
        bSizer53.Add(self.m_radioBtn1, 0, wx.LEFT | wx.TOP, 5)
        
        self.m_radioBtn2 = wx.RadioButton(self.m_panel19, wx.ID_ANY, u"1/Standard Deviation", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_radioBtn2.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        
        bSizer53.Add(self.m_radioBtn2, 0, wx.ALL, 5)
        
        self.m_panel19.SetSizer(bSizer53)
        self.m_panel19.Layout()
        bSizer53.Fit(self.m_panel19)
        bSizer52.Add(self.m_panel19, 0, wx.EXPAND, 5)
        
        bSizer50.Add(bSizer52, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer48.Add(bSizer50, 1, wx.EXPAND, 5)
        
        self.m_panel18.SetSizer(bSizer48)
        self.m_panel18.Layout()
        bSizer48.Fit(self.m_panel18)
        bSizer47.Add(self.m_panel18, 0, wx.EXPAND  | wx.ALL, 5)
        
        bSizer46.Add(bSizer47, 0, wx.EXPAND, 5)
        
        self.m_panel14.SetSizer(bSizer46)
        self.m_panel14.Layout()
        bSizer46.Fit(self.m_panel14)
        bSizer37.Add(self.m_panel14, 1, wx.EXPAND  | wx.ALL, 5)
        
        bSizer36.Add(bSizer37, 1, wx.EXPAND, 5)
        
        bSizer39 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer61 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText38 = wx.StaticText(self.data_options_panel, wx.ID_ANY, u"Data Mask", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText38.Wrap(-1)
        bSizer61.Add(self.m_staticText38, 0, wx.ALL, 5)
        
        bSizer39.Add(bSizer61, 0, wx.EXPAND, 5)
        
        bSizer62 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel21 = wx.Panel(self.data_options_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer63 = wx.BoxSizer(wx.VERTICAL)
        
        m_choice26Choices = [ u"_none_" ]
        self.m_choice26 = wx.Choice(self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice26Choices, 0)
        self.m_choice26.SetSelection(0)
        bSizer63.Add(self.m_choice26, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_panel21.SetSizer(bSizer63)
        self.m_panel21.Layout()
        bSizer63.Fit(self.m_panel21)
        bSizer62.Add(self.m_panel21, 0, wx.EXPAND  | wx.ALL, 5)
        
        bSizer39.Add(bSizer62, 1, wx.EXPAND, 5)
        
        bSizer36.Add(bSizer39, 1, wx.EXPAND, 5)
        
        bSizer34.Add(bSizer36, 1, wx.EXPAND, 5)
        
        self.data_options_panel.SetSizer(bSizer34)
        self.data_options_panel.Layout()
        bSizer34.Fit(self.data_options_panel)
        self.curve_fitting_notebook.AddPage(self.data_options_panel, u"Data Options", False)
        self.coefficients_panel = wx.Panel(self.curve_fitting_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer74 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer75 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_button13 = wx.Button(self.coefficients_panel, wx.ID_ANY, u"Graph Now", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer75.Add(self.m_button13, 0, wx.ALL, 5)
        
        bSizer74.Add(bSizer75, 0, wx.ALIGN_CENTER, 5)
        
        self.m_staticline1 = wx.StaticLine(self.coefficients_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer74.Add(self.m_staticline1, 0, wx.EXPAND  | wx.ALL, 5)
        
        bSizer76 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer801 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer851 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText421 = wx.StaticText(self.coefficients_panel, wx.ID_ANY, u"Coefficient Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText421.Wrap(-1)
        bSizer851.Add(self.m_staticText421, 0, wx.ALL, 5)
        
        bSizer801.Add(bSizer851, 1, wx.EXPAND, 5)
        
        bSizer861 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText431 = wx.StaticText(self.coefficients_panel, wx.ID_ANY, u"Initial Value", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText431.Wrap(-1)
        self.m_staticText431.SetMinSize(wx.Size(150,-1))
        
        bSizer861.Add(self.m_staticText431, 0, wx.ALL, 5)
        
        bSizer801.Add(bSizer861, 1, wx.EXPAND, 5)
        
        bSizer87 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText44 = wx.StaticText(self.coefficients_panel, wx.ID_ANY, u"Hold Constant", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText44.Wrap(-1)
        self.m_staticText44.SetMinSize(wx.Size(150,-1))
        
        bSizer87.Add(self.m_staticText44, 0, wx.ALL, 5)
        
        bSizer801.Add(bSizer87, 1, wx.EXPAND, 5)
        
        bSizer881 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText451 = wx.StaticText(self.coefficients_panel, wx.ID_ANY, u"Constraints", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText451.Wrap(-1)
        self.m_staticText451.SetMinSize(wx.Size(150,-1))
        
        bSizer881.Add(self.m_staticText451, 0, wx.ALL, 5)
        
        bSizer801.Add(bSizer881, 1, wx.EXPAND, 5)
        
        bSizer76.Add(bSizer801, 1, wx.EXPAND, 5)
        
        self.m_panel221 = wx.Panel(self.coefficients_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,-1), wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        self.m_panel221.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_panel221.SetMinSize(wx.Size(-1,150))
        
        gSizer2 = wx.GridSizer(5, 4, 0, 0)
        
        bSizer841 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText381 = wx.StaticText(self.m_panel221, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText381.Wrap(-1)
        bSizer841.Add(self.m_staticText381, 0, wx.ALL, 5)
        
        gSizer2.Add(bSizer841, 0, wx.EXPAND, 5)
        
        bSizer811 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_textCtrl27 = wx.TextCtrl(self.m_panel221, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer811.Add(self.m_textCtrl27, 0, wx.ALL, 5)
        
        gSizer2.Add(bSizer811, 0, wx.EXPAND, 5)
        
        bSizer87 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText481 = wx.StaticText(self.m_panel221, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText481.Wrap(-1)
        bSizer87.Add(self.m_staticText481, 0, wx.ALL, 5)
        
        self.m_checkBox3 = wx.CheckBox(self.m_panel221, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer87.Add(self.m_checkBox3, 0, wx.ALL, 5)
        
        gSizer2.Add(bSizer87, 1, wx.EXPAND, 5)
        
        bSizer831 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_textCtrl29 = wx.TextCtrl(self.m_panel221, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1,-1), 0)
        self.m_textCtrl29.SetMinSize(wx.Size(50,-1))
        
        bSizer831.Add(self.m_textCtrl29, 0, wx.ALL, 5)
        
        self.m_staticText461 = wx.StaticText(self.m_panel221, wx.ID_ANY, u"< __ <", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText461.Wrap(-1)
        bSizer831.Add(self.m_staticText461, 0, wx.ALL, 5)
        
        self.m_textCtrl30 = wx.TextCtrl(self.m_panel221, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl30.SetMinSize(wx.Size(50,-1))
        
        bSizer831.Add(self.m_textCtrl30, 0, wx.ALL, 5)
        
        gSizer2.Add(bSizer831, 0, wx.EXPAND, 5)
        
        self.m_staticText41 = wx.StaticText(self.m_panel221, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText41.Wrap(-1)
        gSizer2.Add(self.m_staticText41, 0, wx.ALL, 5)
        
        bSizer821 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_textCtrl28 = wx.TextCtrl(self.m_panel221, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer821.Add(self.m_textCtrl28, 0, wx.ALL, 5)
        
        gSizer2.Add(bSizer821, 0, wx.EXPAND, 5)
        
        bSizer88 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText49 = wx.StaticText(self.m_panel221, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText49.Wrap(-1)
        bSizer88.Add(self.m_staticText49, 0, wx.ALL, 5)
        
        self.m_checkBox2 = wx.CheckBox(self.m_panel221, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer88.Add(self.m_checkBox2, 1, wx.ALL, 5)
        
        gSizer2.Add(bSizer88, 1, wx.EXPAND, 5)
        
        bSizer862 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_textCtrl37 = wx.TextCtrl(self.m_panel221, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl37.SetMinSize(wx.Size(50,-1))
        
        bSizer862.Add(self.m_textCtrl37, 0, wx.ALL, 5)
        
        self.m_staticText471 = wx.StaticText(self.m_panel221, wx.ID_ANY, u"< __ <", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText471.Wrap(-1)
        bSizer862.Add(self.m_staticText471, 0, wx.ALL, 5)
        
        self.m_textCtrl38 = wx.TextCtrl(self.m_panel221, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl38.SetMinSize(wx.Size(50,-1))
        
        bSizer862.Add(self.m_textCtrl38, 0, wx.ALL, 5)
        
        gSizer2.Add(bSizer862, 1, wx.EXPAND, 5)
        
        self.m_panel221.SetSizer(gSizer2)
        self.m_panel221.Layout()
        gSizer2.Fit(self.m_panel221)
        bSizer76.Add(self.m_panel221, 0, wx.EXPAND  | wx.ALL, 5)
        
        bSizer74.Add(bSizer76, 0, wx.EXPAND, 5)
        
        self.coefficients_panel.SetSizer(bSizer74)
        self.coefficients_panel.Layout()
        bSizer74.Fit(self.coefficients_panel)
        self.curve_fitting_notebook.AddPage(self.coefficients_panel, u"Coefficients", False)
        self.output_panel = wx.Panel(self.curve_fitting_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer89 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel231 = wx.Panel(self.output_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer90 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer91 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel241 = wx.Panel(self.m_panel231, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer93 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer94 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer99 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText50 = wx.StaticText(self.m_panel241, wx.ID_ANY, u"Output Series", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText50.Wrap(-1)
        bSizer99.Add(self.m_staticText50, 0, wx.ALL, 5)
        
        bSizer94.Add(bSizer99, 1, wx.EXPAND, 5)
        
        bSizer97 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_textCtrl39 = wx.TextCtrl(self.m_panel241, wx.ID_ANY, u"_none_", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer97.Add(self.m_textCtrl39, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer94.Add(bSizer97, 1, wx.EXPAND, 5)
        
        bSizer93.Add(bSizer94, 0, wx.EXPAND, 5)
        
        bSizer95 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer100 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText51 = wx.StaticText(self.m_panel241, wx.ID_ANY, u"Residual Series: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        bSizer100.Add(self.m_staticText51, 0, wx.ALL, 5)
        
        bSizer95.Add(bSizer100, 1, wx.EXPAND, 5)
        
        bSizer98 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_textCtrl40 = wx.TextCtrl(self.m_panel241, wx.ID_ANY, u"_none_", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer98.Add(self.m_textCtrl40, 0, wx.ALL | wx.EXPAND, 5)
        
        bSizer95.Add(bSizer98, 1, wx.EXPAND, 5)
        
        bSizer93.Add(bSizer95, 0, wx.EXPAND, 5)
        
        bSizer96 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer93.Add(bSizer96, 0, wx.EXPAND, 5)
        
        self.m_panel241.SetSizer(bSizer93)
        self.m_panel241.Layout()
        bSizer93.Fit(self.m_panel241)
        bSizer91.Add(self.m_panel241, 1, wx.EXPAND  | wx.ALL, 5)
        
        bSizer90.Add(bSizer91, 0, wx.EXPAND, 5)
        
        bSizer92 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel251 = wx.Panel(self.m_panel231, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer101 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer102 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_checkBox8 = wx.CheckBox(self.m_panel251, wx.ID_ANY, u"Error Analysis", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer102.Add(self.m_checkBox8, 0, wx.ALL, 5)
        
        bSizer101.Add(bSizer102, 0, wx.EXPAND, 5)
        
        bSizer103 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel26 = wx.Panel(self.m_panel251, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer104 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer105 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText52 = wx.StaticText(self.m_panel26, wx.ID_ANY, u"Confidence Interval: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText52.Wrap(-1)
        bSizer105.Add(self.m_staticText52, 0, wx.ALL, 5)
        
        m_comboBox1Choices = [ u"99.73", u"99.00", u"95.40", u"90.00", u"68.30" ]
        self.m_comboBox1 = wx.ComboBox(self.m_panel26, wx.ID_ANY, u"95", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, wx.CB_SORT)
        bSizer105.Add(self.m_comboBox1, 0, wx.ALL, 5)
        
        bSizer104.Add(bSizer105, 0, wx.EXPAND, 5)
        
        bSizer106 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer1061 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText511 = wx.StaticText(self.m_panel26, wx.ID_ANY, u"Include:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText511.Wrap(-1)
        bSizer1061.Add(self.m_staticText511, 0, wx.ALL, 5)
        
        bSizer106.Add(bSizer1061, 0, wx.EXPAND, 5)
        
        bSizer107 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel27 = wx.Panel(self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer108 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer111 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_checkBox4 = wx.CheckBox(self.m_panel27, wx.ID_ANY, u"Confidence Interval for Fit Coefficients", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer111.Add(self.m_checkBox4, 0, wx.ALL, 5)
        
        bSizer108.Add(bSizer111, 1, wx.EXPAND, 5)
        
        bSizer112 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_checkBox5 = wx.CheckBox(self.m_panel27, wx.ID_ANY, u"Confidence Bands", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer112.Add(self.m_checkBox5, 0, wx.ALL, 5)
        
        bSizer108.Add(bSizer112, 1, wx.EXPAND, 5)
        
        bSizer113 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_checkBox6 = wx.CheckBox(self.m_panel27, wx.ID_ANY, u"Prediction Bands", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer113.Add(self.m_checkBox6, 0, wx.ALL, 5)
        
        bSizer108.Add(bSizer113, 1, wx.EXPAND, 5)
        
        self.m_panel27.SetSizer(bSizer108)
        self.m_panel27.Layout()
        bSizer108.Fit(self.m_panel27)
        bSizer107.Add(self.m_panel27, 1, wx.EXPAND  | wx.ALL, 5)
        
        bSizer106.Add(bSizer107, 1, wx.EXPAND, 5)
        
        bSizer104.Add(bSizer106, 0, wx.EXPAND, 5)
        
        self.m_panel26.SetSizer(bSizer104)
        self.m_panel26.Layout()
        bSizer104.Fit(self.m_panel26)
        bSizer103.Add(self.m_panel26, 0, wx.EXPAND  | wx.ALL, 5)
        
        bSizer101.Add(bSizer103, 0, wx.EXPAND, 5)
        
        self.m_panel251.SetSizer(bSizer101)
        self.m_panel251.Layout()
        bSizer101.Fit(self.m_panel251)
        bSizer92.Add(self.m_panel251, 1, wx.EXPAND  | wx.ALL, 5)
        
        bSizer90.Add(bSizer92, 1, wx.EXPAND, 5)
        
        self.m_panel231.SetSizer(bSizer90)
        self.m_panel231.Layout()
        bSizer90.Fit(self.m_panel231)
        bSizer89.Add(self.m_panel231, 1, wx.EXPAND  | wx.ALL, 5)
        
        self.output_panel.SetSizer(bSizer89)
        self.output_panel.Layout()
        bSizer89.Fit(self.output_panel)
        self.curve_fitting_notebook.AddPage(self.output_panel, u"Output Options", False)
        
        bSizer33.Add(self.curve_fitting_notebook, 0, wx.EXPAND  | wx.ALL, 5)
        
        bSizer88 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_panel211 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bSizer73 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText37 = wx.StaticText(self.m_panel211, wx.ID_ANY, u"Dialog:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText37.Wrap(-1)
        bSizer73.Add(self.m_staticText37, 0, wx.ALL, 5)
        
        self.m_textCtrl26 = wx.TextCtrl(self.m_panel211, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, 75), wx.HSCROLL | wx.TE_READONLY | wx.TE_WORDWRAP)
        self.m_textCtrl26.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        
        bSizer73.Add(self.m_textCtrl26, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_panel211.SetSizer(bSizer73)
        self.m_panel211.Layout()
        bSizer73.Fit(self.m_panel211)
        bSizer88.Add(self.m_panel211, 1, wx.ALL | wx.EXPAND, 5)
        
        bSizer33.Add(bSizer88, 0, wx.EXPAND, 5)
        
        bSizer86 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_button16 = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer86.Add(self.m_button16, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        
        self.m_button17 = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer86.Add(self.m_button17, 0, wx.ALL, 5)
        
        bSizer33.Add(bSizer86, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)
        
        self.SetSizer(bSizer33)
        self.Layout()
        bSizer33.Fit(self)
        
        self.Centre(wx.BOTH)
    
    def __del__(self):
        pass
    

