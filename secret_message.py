import os
import random

pics_dir = r"/home/cmoser/projects/udacity/secret_message" 

def mix_pics():
    os.chdir(pics_dir)
    file_list = os.listdir(os.getcwd())
    for file in file_list:
        os.rename(file, str(random.randint(0,9)) + str(random.randint(0,9)) + file)

def unmix_pics():
    os.chdir(pics_dir)
    file_list = os.listdir(os.getcwd())
    for file in file_list:
        os.rename(file, file.translate(None, "0123456789"))

mix_pics()
#unmix_pics()
