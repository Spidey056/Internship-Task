import os

if os.path.exists("./check.txt"):
    print("The text file exist in the directory.")

else:
    print("The text file doesn't exist in the directory.")