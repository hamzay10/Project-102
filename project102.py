import os 
import shutil

source = "C:/Users/faria/Downloads/abc"
destination = "C:/Users/faria/OneDrive/Desktop"


list_of_files = os.listdir(source)
#print(list_of_files)

# Move All Image files from Downloads Folder to Another Folder
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.docx', '.pdf', '.html', '.txt','.xls']:

        path1 = source + '/' + file_name                       # Example path1 : Downloads/ImageName1.jpg        
        path2 = destination + '/' + "Document_Files"                     # Example path2 : D:/My Files/Image_Files      
        path3 = destination + '/' + "Document_Files" + '/' + file_name   # Example path3 : D:/My Files/Image_Files/ImageName1.jpg
        #print("path1 " , path1)
        #print("path3 ", path3)

        # Check if Folder/Directory Path Exists Before Moving
        # Else make a NEW Folder/Directory Then Move
        if os.path.exists(path2):
          print("Path exists and moving the files " + file_name + ".....")

          # Move from path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Creating the folder and moving the files " + file_name + ".....")
          shutil.move(path1, path3)