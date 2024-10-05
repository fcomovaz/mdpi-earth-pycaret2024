import os
import shutil

# iterate in the Salamanca folder and subfolders and remove the moviles folders
root_dir = 'Salamanca'
remove_dir = 'moviles'

for dirpath, dirnames, filenames in os.walk(root_dir):
    for dirname in dirnames:
        if dirname == remove_dir:
            path = os.path.join(dirpath, dirname)
            # print('Removing:', path)
            shutil.rmtree(path)
            # print('Removed:', path)

print('Done!')