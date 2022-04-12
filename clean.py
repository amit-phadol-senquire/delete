import logging
import os, os.path
import glob
from click import option
from numpy import delete

DIR = '/home/eaglai/amit/raw'
DIR2 = '/home/eaglai/amit/res'
#DIR = '/home/eaglai/.mount_folders/hub_media/raw'
#DIR2 = '/home/eaglai/.mount_folders/hub_media/res'

count = 0
list_of_files = sorted( os.listdir(DIR), key=lambda x: os.path.getctime (os.path.join(DIR, x)),
                                 reverse= False )
if len(list_of_files)<= 200:
        print("Number of files not present total file present is", + len(list_of_files))

else:
        num = round(len(list_of_files)/2)
        print("Cleaning raw")
        if num <= len(list_of_files):
                for x in range(0, num):
                        os.remove(os.path.join(DIR, list_of_files[x]) )

list_of_files1 = sorted( os.listdir(DIR2), key=lambda x: os.path.getctime (os.path.join(DIR2, x)),
                                reverse= False )
if len(list_of_files1)<= 200:
        print("Number of files not present in res  total file present is", + len(list_of_files1))

else:
        num1 = round(len(list_of_files1)/2)
        print("Cleaning res")
        if num1 <= len(list_of_files1):
                for x in range(0, num1):
                        os.remove(os.path.join(DIR2, list_of_files1[x]) )
