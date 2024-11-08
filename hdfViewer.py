import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import h5py
import pandas as pd

'''
Opens a GUI for the user to select a H5 file to view
Archaic tree is displayed so I highly recommend the terminal viewer
'''

class HDF5Viewer(tk.Tk):
    file_path = "/"
    def __init__(self):
        super().__init__()
        self.title("HDF5 Viewer")
        self.geometry("800x600")

        # Treeview for displaying the structure
        self.tree = ttk.Treeview(self)
        self.tree.pack(side='left', expand=True, fill='both')

        # Scrollbar for the treeview
        self.tree_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree_scroll.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=self.tree_scroll.set)

        self.tree.bind("<Double-1>", self.on_item_double_click)

        # Menu for opening files
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)

    def open_file(self):
        self.file_path = filedialog.askopenfilename(title="Open HDF5 file", filetypes=[("HDF5 files", "*.h5 *.hdf5")])
        if self.file_path:
            self.display_hdf5(self.file_path)

    def display_hdf5(self, file_path):
        try:
            self.tree.delete(*self.tree.get_children())  # Clear the treeview
            with h5py.File(file_path, 'r') as hdf:
                self._recursively_display(hdf, self.tree, '')
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _recursively_display(self, hdf, parent, path):
        for key in hdf.keys():
            full_path = f"{path}/{key}" if path else key
            item_id = parent.insert(parent='', index='end', iid=full_path, text=key)
            if isinstance(hdf[key], h5py.Group):
                self._recursively_display(hdf[key], parent, full_path)

    def on_item_double_click(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_path = selected_item[0]
            self.display_table(item_path)

    def display_table(self, path):
        try:
            with h5py.File(self.file_path, 'r') as hdf:
                dataset = hdf[path]
                if isinstance(dataset, h5py.Dataset):
                    df = pd.DataFrame(dataset[...])  # Load data into DataFrame
                    self.show_data_frame(df)
                else:
                    messagebox.showinfo("Info", f"{path} is not a dataset.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_data_frame(self, df):
        new_window = tk.Toplevel(self)
        new_window.title("Data Table")

        frame = ttk.Frame(new_window)
        frame.pack(fill='both', expand=True)

        table = ttk.Treeview(frame, columns=list(df.columns), show='headings')
        table.pack(side='left', fill='both', expand=True)

        # Add headings
        for col in df.columns:
            table.heading(col, text=col)
            table.column(col, anchor="center")

        # Add scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=table.yview)
        scrollbar.pack(side='right', fill='y')
        table.configure(yscrollcommand=scrollbar.set)

        # Insert data into the table
        for _, row in df.iterrows():
            table.insert("", "end", values=list(row))

if __name__ == "__main__":
    viewer = HDF5Viewer()
    viewer.mainloop()