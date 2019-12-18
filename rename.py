# Takes user input to rename video files for plex
# Author: Trojan

import os
from natsort import natsorted #using this module to natural sort the files by episode number.

# get the name of the show and the current season from the user
show_name = input("What is the show's name?")
current_season = input("What is the current season?")

# gets the list of files in the anime folder for renaming and sets the episode counter
path = os.path.join(r"C:\Users\troym\Downloads\Video")
filenames = os.listdir(path)
natsorted(filenames)
episode_counter = 1

# if statement to check if filenames list is empty
if filenames:
    # loops through all the files in the video folder and renames each one with the show name, the season, and the iterated episode number, if no files prints error
    for files in filenames:
        filename, file_extension = os.path.splitext(files)
        os.rename(path + "\\" + filename + file_extension, path + "\\" + show_name + " " + "s" +
            str(current_season).zfill(2) + "e" + str(episode_counter).zfill(2) + file_extension)
        episode_counter = episode_counter + 1
else:
    print("Opps! No files in the folder to rename.")
