import os

def count_file_extensions(dir_path):

    if not os.path.isdir(dir_path):
        print(f"Error:{dir_path} is not a valid directory.")
        return
    
    extension_count = {}

    for root,dir,files in os.walk(dir_path):

        for file in files:

            _, extension = os.path.splitext(file)

            if not extension:
                continue


            extension = extension[1:]

            extension_count[extension] = extension_count.get(extension,0) + 1

    for extension,count in extension_count.items():
        print(f"{count} {extension} file {'s' if count > 1 else ''} in {dir_path}")
    
dir_path = "C:\\Users\\Srinivas\\OneDrive\\Desktop\\Internship Task"
count_file_extensions(dir_path)