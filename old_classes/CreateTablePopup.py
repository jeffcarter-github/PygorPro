import wx


class CreateTablePopUp(wx.Frame):
    def __init__(self, parent, current_dataFrames):
        self.parent = parent
        self.current_dataFrames = current_dataFrames
        self.dataFrame_selection = None

        title = 'Select DataFrame to Display in Table...'
        wx.Frame.__init__(self, None, title=title, size=(350, 75))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.choice = wx.Choice(self, -1, choices=self.current_dataFrames)
        self.Bind(wx.EVT_CHOICE, self.on_choice, self.choice)

        cancel_button = wx.Button(self, -1, label='Cancel')
        ok_button = wx.Button(self, -1, label='Ok')

        cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)
        ok_button.Bind(wx.EVT_BUTTON, self.on_ok)

        sizer.Add(self.choice, 0, wx.ALIGN_LEFT | wx.EXPAND)

        sub_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sub_sizer.Add(cancel_button, 1, wx.ALIGN_LEFT)
        sub_sizer.Add(ok_button, 1, wx.ALIGN_RIGHT)

        sizer.Add(sub_sizer, 0, wx.ALIGN_BOTTOM)
        self.SetSizer(sizer)

        self.Show(True)

    def on_choice(self, event):
        self.dataFrame_selection = event.GetSelection()

    def on_cancel(self, event):
        self.Destroy()

    def on_ok(self, event):
        if self.dataFrame_selection is not None:
            current_dataFrame =\
                self.current_dataFrames[self.dataFrame_selection]
            self.parent.df_selection_for_table(current_dataFrame)
        self.Destroy()
