import tkinter as tk

from tkinter import (ttk, filedialog as fd)

class MainView:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.fd = fd

        self.root.title('LinkedIn Learning Notes')

        self.select_file_label = ttk.Label(self.root, text='Select a file:')
        self.select_file_label.grid(column=0, row=0)

        self.selected_file_label = ttk.Label(self.root, text='')
        self.selected_file_label.grid(column=1, row=0)

        self.select_file_button = ttk.Button(self.root, text='Attach...', command=self.controller.import_file)
        self.select_file_button.grid(column=2, row=0)

        self.select_language_label = ttk.Label(self.root, text='Select a language:')
        self.select_language_label.grid(column=0, row=1)

        language_options = ['en_us', 'pt_br']
        language = tk.StringVar(self.root)
        self.select_language = tk.OptionMenu(self.root, language, *language_options, command=self.set_language)
        self.select_language.grid(column=2, row=1)

        self.select_destination_label = ttk.Label(self.root, text='Select a destination:')
        self.select_destination_label.grid(column=0, row=2)

        destination_options = ['File']
        destination = tk.StringVar(self.root)
        self.select_destination = tk.OptionMenu(self.root, destination, *destination_options, command=self.set_destination)
        self.select_destination.grid(column=2, row=2)
        
        self.cancel_button = ttk.Button(self.root, text='Cancel', command=self.cancel)
        self.cancel_button.grid(column=1, row=3)

        self.export_button = ttk.Button(self.root, text='Export', command=self.export_file)
        self.export_button.grid(column=2, row=3)

    def export_file(self):
        output_file = fd.asksaveasfilename(
            defaultextension='.json',
            filetypes=[
                ('JSON files', '*.json'),
                ('Markdown files', '*.md'), 
            ]),
        self.controller.set_output_file(output_file[0])
        self.controller.export_file()

    def cancel(self):
        self.root.destroy()

    def open(self):
        self.root.mainloop()

    def set_language(self, language):
        self.controller.set_language(language)
    
    def set_destination(self, destination):
        self.controller.set_destination(destination)
