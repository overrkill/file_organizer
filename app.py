from os import listdir ,mkdir , rename
from os.path import join , isfile , isdir , splitext 
from datetime import date
#getting list of files

folder_path = r"C:\Users\abhik\Downloads"

list_of_files = [f for f in listdir(folder_path) if isfile(join(folder_path,f))]

print(list_of_files)

# placing files in appropriate folder
def placefile(filename:str):
    oldfilename , ext = splitext(filename) 
    new_folder = str(date.today())
    print('moving {}'.format(oldfilename))
    if(isdir(join(folder_path,ext))):
        if(isdir(join(folder_path,ext,new_folder))):
            
            rename(join(folder_path,filename),join(folder_path,ext,new_folder,filename))            
        else:
            mkdir(join(folder_path,ext,new_folder))
            rename(join(folder_path,filename),join(folder_path,ext,new_folder,filename))  
    else:
        mkdir(join(folder_path,ext))
        mkdir(join(folder_path,ext,new_folder))
        rename(join(folder_path,filename),join(folder_path,ext,new_folder,filename))

#callthe function
for f in list_of_files:
    placefile(f)