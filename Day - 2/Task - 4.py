import os

if os.path.exists("./file.txt"):
    os.remove("file.txt")
    print("The file is removed successfully.")

else:
    print("The file does not exist")

