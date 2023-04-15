from FileManagerV1 import FileManager
import tkinter as tk
from tkinter import filedialog, messagebox

class FileManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("File Manager")
        
        # Variables for file manager
        self.dest_dir = tk.StringVar()
        self.src_dir = tk.StringVar()
        self.ext = tk.StringVar()
        self.keyword = tk.StringVar()
        self.new_dest_dir = tk.StringVar()
        
        # File manager widgets
        tk.Label(self.master, text="Destination directory:").grid(row=0, column=0, sticky="w")
        tk.Entry(self.master, textvariable=self.dest_dir).grid(row=0, column=1)
        tk.Button(self.master, text="Browse", command=self.browse_dest_dir).grid(row=0, column=2)
        
        tk.Label(self.master, text="Source directory:").grid(row=1, column=0, sticky="w")
        tk.Entry(self.master, textvariable=self.src_dir).grid(row=1, column=1)
        tk.Button(self.master, text="Browse", command=self.browse_src_dir).grid(row=1, column=2)
        
        tk.Label(self.master, text="File extension:").grid(row=2, column=0, sticky="w")
        tk.Entry(self.master, textvariable=self.ext).grid(row=2, column=1)
        
        tk.Label(self.master, text="File keyword:").grid(row=3, column=0, sticky="w")
        tk.Entry(self.master, textvariable=self.keyword).grid(row=3, column=1)
        
        tk.Label(self.master, text="New destination directory (optional):").grid(row=4, column=0, sticky="w")
        tk.Entry(self.master, textvariable=self.new_dest_dir).grid(row=4, column=1)
        tk.Button(self.master, text="Browse", command=self.browse_new_dest_dir).grid(row=4, column=2)
        
        tk.Button(self.master, text="Move Files", command=self.move_files).grid(row=5, column=1)
        
    def browse_dest_dir(self):
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            self.dest_dir.set(selected_dir)
        
    def browse_src_dir(self):
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            self.src_dir.set(selected_dir)
        
    def browse_new_dest_dir(self):
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            self.new_dest_dir.set(selected_dir)
    
    def move_files(self):
        fm = FileManager(self.dest_dir.get(), self.src_dir.get(), self.ext.get(), self.keyword.get(), self.new_dest_dir.get())
        try:
            fm.move_files()
            messagebox.showinfo("Success", "Files moved successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    FileManagerGUI(root)
    root.mainloop()
