import tkinter as tk

from tkinter import (ttk, filedialog as fd)

class MainView:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title('LinkedIn Learning Notes')

        self.select_file_label = ttk.Label(self.root, text='Select a file:')
        self.select_file_label.grid(column=0, row=0)

        self.greeting = ttk.Label(self.root, text='')
        self.greeting.grid(column=1, row=0)

        self.select_file_button = ttk.Button(self.root, text='Attach...', command=self.open_file)
        self.select_file_button.grid(column=2, row=0)

        self.cancel_button = ttk.Button(self.root, text='Cancel', command=self.cancel)
        self.cancel_button.grid(column=1, row=1)

        self.export_button = ttk.Button(self.root, text='Export', command=self.save_file)
        self.export_button.grid(column=2, row=1)

    def open_file(self):
        self.filename = fd.askopenfilename()
        self.greeting.config(text=self.filename.split('/')[-1])

    def save_file(self):
        if not self.filename:
            return
        self.filename = fd.asksaveasfilename()
        with open(self.filename, 'w') as file:
            file.write('Hello, world!')

    def cancel(self):
        self.root.destroy()

    def open(self):
        self.root.mainloop()
