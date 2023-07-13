import os
import glob
import shutil

yml = """
site_name: Tcl/Tk
site_url: https://www.tcl.tk/man
theme: readthedocs

nav:
"""

for filename_dir in glob.glob("..\man-to-md\markdown\*"):
    print(filename_dir)
    filename = filename_dir.split("\\")[-1]
    extension = filename.split(".")[-1]

    shutil.copyfile(filename_dir, f".\docs\{filename}")

for filename_dir in glob.glob(".\docs\*"):
    filename = filename_dir.split("\\")[-1]
    extension = filename.split(".")[-1]

    yml += f"  - {filename.replace('.md', '')}: {filename}\n"

with open("mkdocs.yml", "w") as f:
    f.write(yml)

os.system("mkdocs serve")