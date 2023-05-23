import argparse
import os

def copy_content(dir_path, file_type, destination_file):
    for filename in os.listdir(dir_path):
        # ignore hidden files
        if not filename.startswith('.'):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as infile:
                    # write the contents of each file to the destination file
                    with open(destination_file, 'a') as outfile:
                        file_name = file_path.split("\\")[-1]
                        outfile.write(file_name + ": \n\n ```" + file_type + "\n")
                        outfile.write(infile.read() + "```\n" +
                            "<div style=\"page-break-after: always;\"></div>\n")
            elif os.path.isdir(file_path):
                copy_content(file_path)

def main():
    parser = argparse.ArgumentParser()
    # Add an argument
    parser.add_argument('--dir', type=str, required=True,
                        help="The directory containing the files to be merged")
    parser.add_argument('--lang', type=str, required=True,
                        help="The language of the files to be merged")
    parser.add_argument('--out', type=str, required=True, default="merged.md",
                        help="The output file name")
    args = parser.parse_args()
    try:
        directory = args.dir
        file_type = args.lang
        destination_file = args.out

        with open(destination_file, 'w') as outfile:
            copy_content(directory, file_type, destination_file)
    except:
        print("No valid destination directory passed via command line argument!")

if __name__ == '__main__':
    main()
