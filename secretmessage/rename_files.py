import os
def rename_files():
    # (1) get file names from a folder
    # NOTE Filed directory unique to my Win10 machine 
    #file_list = os.listdir(r"C:\Users\c187r\OneDrive\Documents\GitHub\udacity\secretmessage\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    # (2) for each file, rename filename
    # Udacity Lesson 5, Part 22 Quiz: Find the name of the fuction to rename. That fuction is os.rename
    #for file_name in file_list:
        #os.rename(file_name, file_name.translate(None, "0123456789"))
        # NOTE Error given. Program is not finding dir
        # DEBUG Result: Dir is a level down from the dir wanted. It's running in the same dir as the program
rename_files()
