import tkinter as tk

from tkinter import (ttk, filedialog as fd)

class MainView:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title('LinkedIn Learning Notes')

        self.select_file_label = ttk.Label(self.root, text='Select a file:')
        self.select_file_label.grid(column=0, row=0)

        self.selected_file_label = ttk.Label(self.root, text='')
        self.selected_file_label.grid(column=1, row=0)

        self.select_file_button = ttk.Button(self.root, text='Attach...', command=self.import_file)
        self.select_file_button.grid(column=2, row=0)

        self.cancel_button = ttk.Button(self.root, text='Cancel', command=self.cancel)
        self.cancel_button.grid(column=1, row=1)

        self.export_button = ttk.Button(self.root, text='Export', command=self.save_file)
        self.export_button.grid(column=2, row=1)

    def import_file(self):
        input_file = fd.askopenfilename()
        self.controller.set_input_file(input_file)
        self.selected_file_label.config(text=input_file.split('/')[-1])

    def export_file(self):
        output_file = fd.asksaveasfilename(
            filetypes=[
                ('JSON files (.json)', '*.json'),
                ('Markdown files (.md)', '*.md'), 
                ('Text files (.txt)', '*.txt'), 
            ]),
        self.controller.set_output_file(output_file)

    def cancel(self):
        self.root.destroy()

    def open(self):
        self.root.mainloop()

    def set_language(self, language):
        self.controller.set_language(language)
    
    def set_destination(self, destination):
        self.controller.set_destination(destination)
