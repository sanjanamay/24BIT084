import os
import shutil
def create_and_copy(src_file, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Directory '{dest_dir}' created.")
    else:
        print(f"Directory '{dest_dir}' already exists.")
    shutil.copy(src_file, dest_dir)
    print(f"File '{src_file}' copied to '{dest_dir}'.")
source_file = 'subdir/source.txt'  
destination_dir = 'new_subdir'  
create_and_copy(source_file, destination_dir)
