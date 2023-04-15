import os
import shutil

class FileManager:
    def __init__(self, dest_dir, src_dir, ext, keyword, new_dest_dir=None):
        self.dest_dir = os.path.abspath(dest_dir)
        self.src_dir = os.path.abspath(src_dir)
        self.ext = ext
        self.keyword = keyword.lower()
        if new_dest_dir is not None:
            self.new_dest_dir = os.path.abspath(new_dest_dir)
        else:
            self.new_dest_dir = None
    
    def create_dest_dir(self):
        if not os.path.exists(self.dest_dir):
            os.makedirs(self.dest_dir)
            print(f"Created directory {self.dest_dir}")
    
    def move_files(self):
        if self.new_dest_dir is not None and self.new_dest_dir != self.src_dir:
            self.dest_dir = os.path.join(self.new_dest_dir, os.path.basename(self.dest_dir))
            self.create_dest_dir()
        else:
            self.create_dest_dir()
        
        for file in os.listdir(self.src_dir):
            if file.lower().endswith(self.ext) and self.keyword in file.lower():
                src_path = os.path.join(self.src_dir, file)
                dest_path = os.path.join(self.dest_dir, file)
                shutil.move(src_path, dest_path)
                print(f"Moved file {src_path} to {dest_path}")
