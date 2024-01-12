import os

#after last /, replace with any specific file

file_path = '/users/alanz/Downloads/'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print('File has successfully been deleted!')
else:
    print('This file does NOT exist!')  