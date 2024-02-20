import os

def ls(directory):
  for filename in os.listdir(directory):
    print(filename)

ls('.')