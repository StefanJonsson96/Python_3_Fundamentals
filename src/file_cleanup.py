import os

entries = os.scandir() ## scans directory for files, leaving it empty scans the current directory, or you can pass in a path

for entry in entries:
    if os.path.isfile(entry):
        print('File:', entry.name)
    elif os.path.isdir(entry):
        print('Directory:', entry.name)