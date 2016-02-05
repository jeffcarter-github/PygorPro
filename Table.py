import wx
import wx.grid


class Table(wx.Frame):
    def __init__(self, parent, dataFrame_object):
        self.parent = parent
        self.name = dataFrame_object.name
        wx.Frame.__init__(self, parent, title=self.name, pos=(100, 50), size=(1200, 500))

        self.max_rows = 5000
        self.nrows, self.ncols =\
            dataFrame_object.n_rows, dataFrame_object.n_columns
        self.labels = dataFrame_object.get_keys()

        self.data_table = wx.grid.Grid(self)
        if self.nrows > self.max_rows:
            self.nrows = self.max_rows
        self.data_table.CreateGrid(self.nrows, self.ncols)
        self.data_table.EnableEditing(False)
        self.data_table.SetDefaultCellAlignment(vert=wx.ALIGN_CENTER,
                                                horiz=wx.ALIGN_RIGHT)
        for i, key in enumerate(self.labels):
            self.set_label(i, key)
        self.set_values(dataFrame_object)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.data_table, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self.data_table.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK,
                             self.on_user_column_selection)

        self.Show(True)

    def set_label(self, pos, label):
        self.data_table.SetColLabelValue(pos, label)

    def get_label(self, pos):
        return self.data_table.GetColLabelValue(pos)

    def set_values(self, dataFrame):
        for col in range(self.ncols):
            key = self.data_table.GetColLabelValue(col)
            for row in range(self.nrows):
                data_value = str(dataFrame.get_point(key, row))
                self.data_table.SetCellValue(row, col, data_value)
        self.data_table.ForceRefresh()

    def on_user_column_selection(self, event):
        column_selection = event.GetCol()
        if column_selection is not None:
            column_name = self.get_label(column_selection)
            self.parent.report_statistics(self.name, column_name)
