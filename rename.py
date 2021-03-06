# Takes user input to rename video files for plex
# Author: Trojan

import os
import shutil
import glob
# using this module to natural sort the files by episode number.
import natsort as ns

# get the name of the show and the current season from the user
show_name = input("What is the show's name? ")
current_season = input("What is the current season? ")

# gets the list of files in the anime folder for renaming,sets the episode counter and sorts the files by episode using a natural sort on the name string of the files
path = os.path.join(r"C:\Users\troym\Downloads\Video")
filenames = os.listdir(path)
filesort = ns.natsorted(filenames)
episode_counter = 1

# if statement, to check if filesort list is empty
if filesort:
    # loops through all the files in the video folder and renames each one with the show name, the season, and the iterated episode number, if no files prints error
    for files in filesort:
        filename, file_extension = os.path.splitext(files)
        os.rename(path + "\\" + filename + file_extension, path + "\\" + show_name + " " + "s" +
                  str(current_season).zfill(2) + "e" + str(episode_counter).zfill(2) + file_extension)
        episode_counter = episode_counter + 1
else:
    print("Opps! No files in the folder to rename.")

os.mkdir(fr"C:\Users\troym\Downloads\Video\{show_name}")
season_folder = os.mkdir(fr"C:\Users\troym\Downloads\Video\{show_name}\Season {current_season}")

season_folder_dir = os.path.join(fr"C:\Users\troym\Downloads\Video\{show_name}\Season {current_season}")

files = os.listdir(path)

for file in files:
    filename, file_extension = os.path.splitext(file)
    if file_extension != "":
        shutil.move(path + "\\" + file, season_folder_dir)
