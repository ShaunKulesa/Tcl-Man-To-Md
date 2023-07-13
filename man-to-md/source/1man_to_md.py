import os
import glob

for filename_dir in glob.glob("*"):
    filename = filename_dir.split("\\")[-1]
    extension = filename.split(".")[-1]
    
    if extension == "py":
        continue
    
    os.system(f"pandoc --from man --to markdown < {filename_dir} > ../markdown/{filename_dir.replace('source', 'markdown').replace(f'.{extension}', '.md')}")