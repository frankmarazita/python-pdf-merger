import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog

import merge

root = tk.Tk()

root.title('PDF Merger')

# Window
window_width = 230
window_height = 240
root.geometry(str(window_width) + "x" + str(window_height))

# Menu
# menu = tk.Menu(root)
# root.config(menu=menu)
# file_menu = tk.Menu(menu)
# menu.add_cascade(label='File', menu=file_menu)
# file_menu.add_command(label='New')
# file_menu.add_command(label='Open...')
# file_menu.add_separator()
# file_menu.add_command(label='Exit', command=root.quit)

# Content
label_file_name = tk.Label(root, text='Output File Name').grid(row=0, column=0)
field_file_name = tk.Entry(root)
field_file_name.grid(row=0, column=1)

# label_file_dir = tk.Label(root, text='Output File Location').grid(row=1, column=0)
# field_file_dir = tk.Entry(root)
# field_file_dir.grid(row=1, column=1)

files = []
lb_files = tk.Listbox(root, width=37)
lb_files.grid(row=2, columnspan=2)

def browse_file(files):
    file_dialog = filedialog.askopenfile(mode='r', filetypes=[('PDF Files', '*.pdf')])
    files.append(file_dialog.name)
    lb_files.insert(len(files) - 1, file_dialog.name)

button_browse = tk.Button(root, text='Browse', command=lambda:browse_file(files), width=30)
button_browse.grid(row=3, columnspan=2)

button_merge = tk.Button(root, text='Merge', command=lambda:merge.merge(files, field_file_name.get()), width=30)
button_merge.grid(row=4, columnspan=2)

root.mainloop()
