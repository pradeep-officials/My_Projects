# import pandas as pd
import os

# root_in="C:\\Users\pradeep\\Desktop\\PC_file_cleaner_input\\"
# root_out="C:\\Users\pradeep\\Desktop\\PC_File_Cleaner\\"
dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)
scriptpath = os.path.realpath(__file__)
print("Script path is : " + scriptpath)
# root_in=input() #to Take input path at run time
# root_out=input() #to Take output path at run time
root_in = dirpath
root_out = dirpath
files = os.listdir(root_in)

pyfiles = []
for file in files:
    list1 = file.split(".")
    if (len(list1) >= 2):
        if (list1[1] == 'py' or list1[1] == 'exe'):
            pyfiles.append(file)


def ignore_scriptfiles(scrpt_files):
    for script_file in scrpt_files:
        files.remove(script_file)


''' 
if files.__contains__('PC_File_Cleaner.py'):
    files.remove('PC_File_Cleaner.py')
if files.__contains__('PC_File_Cleaner_same_dir.py'):
    files.remove('PC_File_Cleaner_same_dir.py')
if files.__contains__('__init__.py'):
    files.remove('__init__.py')
if files.__contains__('PC_File_Cleaner_same_dir.exe'):
    files.remove('PC_File_Cleaner_same_dir.exe')
'''
print("List of all files: \n****************************************************************")
print(files)
print("List of script files to be ignored: \n****************************************************************")
print(pyfiles)
ignore_scriptfiles(pyfiles)
print("List of files and folders to be categorised: \n****************************************************************")
print(files)
print("List of categorised files: \n****************************************************************")


# function for creating folder
def ifNotExistsCreate(folder):
    if not os.path.exists(root_out + "\\" + folder):
        os.makedirs(root_out + "\\" + folder)


# function for moving files:
def file_mover(file_names, folder_name):
    for file in file_names:
        os.replace(root_in + "\\" + file, root_out + "\\" + folder_name + "\\" + file)
        print("File Moved from " + root_in + "\\" + file + " To-" + root_out + "\\" + folder_name + "\\" + file)


ifNotExistsCreate("Images")
ifNotExistsCreate("Medias")
ifNotExistsCreate("Documents")
ifNotExistsCreate("Others")
imgExt = [".png", ".jpg", ".jpeg"]
medExt = [".m4a", ".mpg"]
docExt = [".txt", ".xlsx", ".pdf", ".xls", ".docx", ".doc", ".pptx", ".csv"]
images = []
'''
for file in files:
    #print(root_in+file)
    #print(root_out+"Images")
    if os.path.splitext(file)[1].lower() in imgExt:
        images.append(file)
        print(images)
'''
# short formate for above code:

images = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]
print("images files :***********\n")
print(images)

medias = [file for file in files if os.path.splitext(file)[1].lower() in medExt]
print("media files :***********\n")
print(medias)

docs = [file for file in files if os.path.splitext(file)[1].lower() in docExt]
print("docs files :***********\n")
print(docs)

others = [file for file in files if (os.path.splitext(file)[1].lower() not in docExt) \
          and (os.path.splitext(file)[1].lower() not in imgExt) \
          and (os.path.splitext(file)[1].lower() not in medExt) \
          and os.path.isfile(root_in + "\\" + file)
          ]
print("other files :***********\n")
print(others)

ifNotExistsCreate("Images")
ifNotExistsCreate("Medias")
ifNotExistsCreate("Documents")
ifNotExistsCreate("Others")

file_mover(images, "Images")
file_mover(medias, "Medias")
file_mover(docs, "Documents")
file_mover(others, "Others")
