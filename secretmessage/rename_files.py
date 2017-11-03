import os
def rename_files():
    # (1) get file names from a folder
    # NOTE File directory unique to my Win10 machine. Please import your directory to run program. 
    file_list = os.listdir(r"C:\Users\c187r\OneDrive\Documents\GitHub\udacity\secretmessage\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"C:\Users\c187r\OneDrive\Documents\GitHub\udacity\secretmessage\prank")

    # (2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    
rename_files()

#NOTE Files on GitHub have been renamed. Unzip prank.zip to get a set of files to rename.
