import os

def rename_files():
    #1 get files names
    file_list = os.listdir(r"/home/cmoser/projects/udacity/prank")
    print(file_list)

    #2 for each file, rename it
    saved_path = os.getcwd()
    print ("Current Working Directory is "+saved_path)
    os.chdir(r"/home/cmoser/projects/udacity/prank")
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
