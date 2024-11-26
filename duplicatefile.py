import os
import shutil

extensions = []

while True:
    source_dr = input('Enter source directory : e.g. C:/Users/miles/Desktop/CardCash\n')
    if not os.path.exists(source_dr):
        print('Source directory does not exist.')
        continue
    else:
        lists = os.listdir(source_dr)
        for y in lists:
            print(y)
        break

while True:
    source_file = input('Enter source file from the list to duplicate.\ne.g. 370112_96xxdata.txt\n')
    currentDir = os.path.join(source_dr, source_file)
    if not os.path.exists(currentDir):
        print(f"Source file '{source_file}' does not exist.")
        continue
    else:
        break

print('Enter extensions to duplicate (will append_96xxdata.txt), enter STOP to proceed with duplication.')
while True:
    targetExtensions = input()
    if targetExtensions == 'STOP':
        print(extensions)
        break
    else:
        extensions.append(targetExtensions)


source_file_path = os.path.join(source_dr, source_file)


for prefix in extensions:

        new_filename = f"{prefix}_96xxdata.txt"
        new_file_path = os.path.join(source_dr, new_filename)

        try:
            shutil.copyfile(source_file_path, new_file_path)
        except shutil.SameFileError as e:
            print('Same extension found, not duplicated ' + str(e))
        print(f"Created: {new_file_path}")

print("Completed.")
