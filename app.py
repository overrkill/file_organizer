from os import listdir ,mkdir , rename
from os.path import join , isfile , isdir , splitext 
from datetime import date
#getting list of files

folder_path = r"location\of\folder\to\organize"

list_of_files = [f for f in listdir(folder_path) if isfile(join(folder_path,f))]

print(list_of_files)

# placing files in appropriate folder
def placefile(filename:str):
    # get extensions of file
    oldfilename , ext = splitext(filename) 
    #name of folder organized datewise
    new_folder = str(date.today())
    print('moving {}'.format(oldfilename))
    #check folder of ext
    if(isdir(join(folder_path,ext))):
        #check folder of date
        if(isdir(join(folder_path,ext,new_folder))):
            #move to file
            rename(join(folder_path,filename),join(folder_path,ext,new_folder,filename))            
        else:
            #create date folder
            mkdir(join(folder_path,ext,new_folder))
            #move to file
            rename(join(folder_path,filename),join(folder_path,ext,new_folder,filename))  
    else:
        # create ext/date folder
        mkdir(join(folder_path,ext))
        mkdir(join(folder_path,ext,new_folder))
        #move to file
        rename(join(folder_path,filename),join(folder_path,ext,new_folder,filename))

#organize the files
for f in list_of_files:
    placefile(f)