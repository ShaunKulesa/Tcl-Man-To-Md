import os
import glob

for filename_dir in glob.glob("source\*"):
    print(filename_dir)

    filename = filename_dir.split("\\")[-1]
    extension = filename.split(".")[-1]

    if extension == "macros":
        continue
    
    else:
        with open(filename_dir, "r") as f:
            source = f.read()

            # replace .CS with .nf in source files
            source = source.replace(".CS", ".nf")

            # replace .CE with .fi in source files
            source = source.replace(".CE", ".fi")
        
        with open(filename_dir, "w") as f:
            f.write(source)