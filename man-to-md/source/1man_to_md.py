import os
import glob

for filename_dir in glob.glob("*"):
    filename = filename_dir.split("\\")[-1]
    extension = filename.split(".")[-1]

    if extension == "py":
        continue

    os.system(f"pandoc --from man --to markdown < {filename_dir} > ../markdown/{filename_dir.replace('source', 'markdown').replace(f'.{extension}', '.md')}")

    if not os.path.isdir(filename_dir):
    
        footer = "<!---\n"

        with open(filename_dir, "r") as f:
            lines = f.readlines()

            for line in lines:
                if """'\\" Copyright (c)""" in line:
                    footer += f"{line[4:-2]}\n"
        
        footer += "-->\n"
            
    with open(f"../markdown/{filename_dir.replace('source', 'markdown').replace(f'.{extension}', '.md')}", "r") as f:
        lines = f.readlines()

        if lines[-1] != "\n":
            lines.append("\n")
        
        lines.append(footer + "\n")
    
    with open(f"../markdown/{filename_dir.replace('source', 'markdown').replace(f'.{extension}', '.md')}", "w") as f:
        f.writelines(lines)
        


