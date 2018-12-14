import tkinter as tk
import matplotlib as mpl
import matplotlib.pyplot as plt
# from tkinter import  Label, Button
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.set_window_init()

        # self.label = tk.Label(self.master, text="This is our first GUI!")
        # self.label.pack()

        # self.file_button = tk.Button(self.top_panel, text="Load File", command=self.greet)
        # self.image_button = tk.Button(self.top_panel, text="Load Image", command=self.greet)
        # self.file_button.pack(side=tk.LEFT)
        # self.image_button.pack(side=tk.LEFT)

    def set_window_init(self):
        # self.master.geometry(f"{self.width}x{self.height}")  # You want the size of the app to be 500x500 :TODO: nicer setup
        # self.master.resizable(0, 0)  # Don't allow resizing in the x or y direction
        self.master.title("Parse Routes")

        self.master_panel = tk.Frame(self.master, borderwidth=2, bg='white')
        self.master_panel.grid(padx=10, pady=10, sticky=tk.W + tk.E + tk.N + tk.S)

        self.file_button = tk.Button(self.master_panel, text="Load File", command=self.draw_image,
                                     width=10, height=1, bg='white', font=("Arial", 11))
        self.file_button.config(font=("Arial", 11))
        self.file_button.grid()
        self.file_entry = tk.Entry(self.master_panel, width=20)
        # self.file_entry.config(font=("Arial", 11))
        self.file_entry.grid(row=0, column=1, padx=(5, 0))

        self.image_button = tk.Button(self.master_panel, text="Load Image", command=self.draw_image,
                                      width=10, height=1, bg='white', font=("Arial", 11))
        self.image_button.grid(row=0, column=2, padx=(10, 0))
        # self.image_button.config(font=("Arial", 11))
        self.img_entry = tk.Entry(self.master_panel, width=20)
        self.img_entry.config(font=("Arial", 11))
        self.img_entry.grid(row=0, column=3, padx=(5, 0))

        self.draw_image()
        self.draw_filters()

        self.status_message = tk.Message(self.master_panel, text="Program Output", bg='white', borderwidth=5,width=200,
                                         highlightbackground="black", highlightthickness=1, font=("Arial", 14)).grid(
            sticky=tk.W + tk.E + tk.N + tk.S, row=19, column=0, columnspan=4,rowspan=2)

    def draw_image(self):
        image = plt.imread('paths0.png')  # TODO call to defualt image
        fig = plt.figure()  # figsize=(5, 4)
        im = plt.imshow(image)  # later use a.set_data(new_data)

        # add numbers
        # ax = plt.gca()
        # ax.set_xticklabels([])
        # ax.set_yticklabels([])
        plt.subplots_adjust(top=0.9, bottom=0.3, right=0.9, left=0.1,
                            hspace=0, wspace=0)

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(fig, master=self.master_panel)
        canvas.draw()
        # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, rowspan=20, sticky=tk.W + tk.E + tk.N + tk.S,
                                    padx=(10, 10), pady=(10, 10))

    def draw_filters(self):
        # self.active_filters = dict({'area': False, 'hour': False, 'date': False, 'block': False})
        self.active_filters = {"area": tk.IntVar(), "hour": tk.IntVar(), "date": tk.IntVar(), "block": tk.IntVar()}
        self.label_filters = tk.Label(self.master_panel, text="Filters:", bg='white', font=("Arial", 14)).grid(
            row=1, column=4, columnspan=2, sticky=tk.W)

        # area filter ======================================
        self.area_checkbox = tk.Checkbutton(self.master_panel, text="Filter by Area",
                                            variable=self.active_filters['area'], bg='white', font=("Arial", 11))
        self.area_checkbox.grid(row=2, column=4, sticky=tk.W)
        tk.Label(self.master_panel, text="Insert x1,x2,x3,x4 :", bg='white', font=("Arial", 9)).grid(
            sticky=tk.W, row=3, column=4)
        self.area_filter = tk.Entry(self.master_panel, width=25, bg='white')
        self.area_filter.grid(row=3, column=5)

        # hour filter ======================================
        self.hour_checkbox = tk.Checkbutton(self.master_panel, text="Filter by Time",
                                            variable=self.active_filters['hour'], bg='white', font=("Arial", 11))

        self.hour_checkbox.grid(row=4, column=4, sticky=tk.W)
        tk.Label(self.master_panel, text="Insert 00:00:00,:", bg='white', font=("Arial", 9)).grid(
            sticky=tk.W, row=5, column=4)
        self.hour_filter = tk.Entry(self.master_panel, width=25, bg='white')
        self.hour_filter.grid(row=5, column=5)

        # date filter ======================================
        self.date_checkbox = tk.Checkbutton(self.master_panel, text="Filter by Date",
                                            variable=self.active_filters['date'], bg='white', font=("Arial", 11))
        self.date_checkbox.grid(row=6, column=4, sticky=tk.W)
        tk.Label(self.master_panel, text="Insert 1970-01-01,time :", bg='white', font=("Arial", 9)).grid(
            sticky=tk.W, row=7, column=4)

        self.date_filter = tk.Entry(self.master_panel, width=25, bg='white')
        self.date_filter.grid(row=7, column=5)

        self.block_checkbox = tk.Checkbutton(self.master_panel, text="Filter by Block",
                                             variable=self.active_filters['block'], bg='white', font=("Arial", 11))
        self.block_checkbox.grid(row=8, column=4, sticky=tk.W)
        tk.Label(self.master_panel, text="Insert 1,2,5,6,89 :", bg='white', font=("Arial", 9)).grid(
            sticky=tk.W, row=9, column=4)
        self.block_filter = tk.Entry(self.master_panel, width=25, bg='white')
        self.block_filter.grid(row=9, column=5)

        self.filters_button = tk.Button(self.master_panel, text="Load Filters", command=self.draw_image,
                                       height=1,width=30, bg='white', font=("Arial", 11))
        self.filters_button.grid(row=10, column=4,columnspan=2)


root = tk.Tk()
my_gui = MyFirstGUI(root)
# my_gui.draw_image()
root.mainloop()
