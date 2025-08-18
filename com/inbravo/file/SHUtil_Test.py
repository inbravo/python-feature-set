import os
import shutil

# This script demonstrates various file operations using the shutil module in Python.
#    Directory and files operations
#        Platform-dependent efficient copy operations
#        copytree example
#        rmtree example
#    Archiving operations
#        Archiving example
#        Archiving example with base_dir
#    Querying the size of the output terminal

# Create a directory
os.mkdir('example_dir')

# Create a file in the directory
with open('example_dir/example_file.txt', 'w', encoding='utf-8') as f:
    f.write('This is an example file.')

# Copy a file
shutil.copy('example_dir/example_file.txt', 'example_dir/copied_file.txt')

# Copy a directory
shutil.copytree('example_dir', 'example_dir_copy')

# Move a file
shutil.move('example_dir/copied_file.txt', 'example_dir/moved_file.txt')

# Rename a file
os.rename('example_dir/moved_file.txt', 'example_dir/renamed_file.txt')

# Archive a directory (creates a zip file)
shutil.make_archive('example_dir_archive', 'zip', 'example_dir')

# Extract the archive
shutil.unpack_archive('example_dir_archive.zip', 'extracted_dir')

# Remove a directory tree
shutil.rmtree('example_dir')
shutil.rmtree('example_dir_copy')
shutil.rmtree('extracted_dir')

# Remove the archive
os.remove('example_dir_archive.zip')

print("All shutil operations completed successfully.")