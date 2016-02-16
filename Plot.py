import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
import matplotlib.pyplot as plt
import numpy as np


class Plot(wx.Frame):
    '''Plot Class generates Plots... Input: index (int) and data_set (dic).
    data_set is a dictionary with the following keys: x_data, y_data, x_axis,
    y_axis, x_label, y_label, title, style'''
    def __init__(self, index, data_set):
        if data_set['title'] is '':
            self.title = 'Plot: ' + str(index)
        else:
            self.title = data_set['title']

        wx.Frame.__init__(self, None, title=self.title, pos=(200, 100), size=(500, 500))

        self.plot_index = index
        self.x = data_set['x_data']
        self.y = data_set['y_data']
        self.max_idx = len(self.x)-1

        self.selection = None
        self.selection_object = None
        self.actively_fitting = False

        self.x_extrema = (min(self.x), max(self.x))
        self.y_extrema = (min(self.y), max(self.y))

        self.label_x = data_set['x_label']
        self.label_y = data_set['y_label']

        if data_set['style'] == 'Line':
            self.style = 'b'
        elif data_set['style'] == 'Scatter':
            self.style = 'bo'

        self.canvas = None
        self.cid = None
        self.fig = None
        self.plot = None
        self.mlp_connect_not_ready_flag = None

        self.font_size = 8

        self.generate_plot()
        self.setup_canvas()
        self.setup_mpl_connect()
        self.generate_status_bar()

        self.Show(True)

    def setup_canvas(self):
        self.canvas = FigCanvas(self, -1, self.fig)
        self.canvas.draw()

    def generate_plot(self):
        self.fig = plt.figure(dpi=100, facecolor='white', frameon=True)
        self.axes = self.fig.add_subplot(111)
        self.axes.plot(self.x, self.y, self.style)
        self.axes.set_xlabel(self.label_x, size=self.font_size)
        self.axes.set_ylabel(self.label_y, size=self.font_size)
        self.axes.tick_params(axis='both', which='major', labelsize=self.font_size)
        self.axes.grid(axis='both', which='both')

    def setup_mpl_connect(self):
        self.on_click_cid =\
            self.canvas.mpl_connect('button_press_event', self.on_click)
        self.motion_cid =\
            self.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.key_cid =\
            self.canvas.mpl_connect('key_press_event', self.on_key)

    def on_click(self, event):
        if not self.actively_fitting:
            if event.xdata is not None or event.ydata is not None:
                self.calculate_nearest_datapoint(event.xdata, event.ydata)
                self.report_data_point_to_status_bar()
                self.highlight_selection()
            else:
                self.report_no_data_point_to_status_bar()

    def on_motion(self, event):
        if not self.mlp_connect_not_ready_flag:
            if event.xdata is not None or event.ydata is not None:
                self.report_position_to_status_bar(event.xdata, event.ydata)

    def on_key(self, event):
        if self.selection is not None:
            if event.key == 'left' and self.selection != 0:
                self.selection -= 1
            elif event.key == 'right' and self.selection != self.max_idx:
                self.selection += 1
        self.highlight_selection()
        self.report_data_point_to_status_bar()

    def generate_status_bar(self):
        number_of_areas = 4
        self.CreateStatusBar(number_of_areas)
        self.SetStatusWidths([-2, -6, -2, -6])
        self.SetSize = (500, -1)
        self.initialize_status_bar()

    def highlight_selection(self):
        idx = self.selection
        if self.selection_object is not None:
            try:
                self.selection_object.pop(0).remove()
            except TypeError:
                pass
        self.selection_object =\
            self.axes.plot(self.x[idx], self.y[idx], 'or', alpha=0.25, ms=6)
        self.canvas.draw()

    def report_position_to_status_bar(self, event_xdata, event_ydata):
        try:
            self.SetStatusText('(%f, %f)' % (event_xdata, event_ydata), 1)
        except TypeError:
            pass

    def report_data_point_to_status_bar(self):
        idx = self.selection
        self.SetStatusText('Data Point: ', 2)
        self.SetStatusText('%i (%f,%f)' % (idx, self.x[idx], self.y[idx]), 3)

    def report_no_data_point_to_status_bar(self):
        self.SetStatusText('', 2)
        self.SetStatusText('', 3)

    def initialize_status_bar(self):
        self.SetStatusText('(x, y)', 0)

    def calculate_nearest_datapoint(self, event_xdata, event_ydata):
        min_distance = sum(self.x_extrema) + sum(self.y_extrema)
        min_distance_point = None
        for i, x_i in enumerate(self.x):
            dist_value = distance(x_i, self.y[i], event_xdata, event_ydata)
            if dist_value < min_distance:
                min_distance = dist_value
                min_distance_point = i
        self.selection = min_distance_point

    def delete_plot(self):
        self.Destroy()


def distance(x1, y1, x2, y2):
    try:
        return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    except TypeError:
        return None
