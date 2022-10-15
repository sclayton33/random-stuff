#! /usr/bin/python
"""Script to rename the season number in TV show filepaths. e.g S01 to S02.
Can be adapted to rename other parts."""
import os

# Set all of these as needed
OLD_SEASON_NUM = 'S01'
NEW_SEASON_NUM = 'S02'
SEASON_PATH = r"/path/to/season/folder"

# counts number of files changed and creates empty list to store new file names
counter = 0
files = []

# changes to desired directory so files will be found
os.chdir(SEASON_PATH)

# loops through all files in the directory
for file_name in os.listdir(SEASON_PATH):
    if OLD_SEASON_NUM in file_name :
        old_name = file_name
        new_name = file_name.replace(OLD_SEASON_NUM, NEW_SEASON_NUM)
        counter += 1
        files.append(new_name)
        os.rename(old_name, new_name)


print('Number of files changed:' counter)
print(files)
