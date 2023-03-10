import os
import sys

# specify the destination file
destination_file = './merged.md'

def copy_content(dir_path):
    for filename in os.listdir(dir_path):
        # ignore hidden files
        if not filename.startswith('.'):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as infile:
                    # write the contents of each file to the destination file
                    with open(destination_file, 'a') as outfile:
                        file_name = file_path.split("\\")[-1]
                        outfile.write(file_name + ":\n```c\n")
                        outfile.write(infile.read() + "```\n\n")
            elif os.path.isdir(file_path):
                copy_content(file_path)

try:
    directory = sys.argv[1]

    with open(destination_file, 'w') as outfile:
        copy_content(directory)
except:
    print("No valid destination directory passed via command line argument!")
