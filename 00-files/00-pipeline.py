# create a simple script to execute some functions in my folder by name

import os

# unzip Salamanca.zip only if a Salamanca folder doesn't exist
if not os.path.exists("Salamanca"):
    os.system("unzip Salamanca.zip")
    print("Unzipped!")
    os.system("pause")
else:
    print("Folder already exists")


# return all the files in the current directory .py
pipeline = []
for file in os.listdir("."):
    if file.endswith(".py"):
        pipeline.append(file)

# execute each file in the pipeline
# remove 00-pipeline.py
pipeline.remove("00-pipeline.py")
pipeline = pipeline[0:]
for file in pipeline:
    print(f"Executed {file}")
    os.system(f"python {file}")