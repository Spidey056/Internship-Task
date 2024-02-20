import os

isExist = os.path.isdir("./new_dir")


if isExist:
    print("The Folder Already Exist.")
else:
    os.mkdir(os.path.join("./","new_dir"))
    f = open("./new_dir/output.txt","w")