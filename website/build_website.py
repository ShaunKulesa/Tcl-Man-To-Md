import os
import glob
import shutil

yml = """
site_name: Tcl/Tk
site_url: https://www.tcl.tk/man

theme:
  name: material
  highlightjs: false

  features:
    - content.code.copy

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences

nav:
  - Home: 
    - index.md
"""

rootdir = "..\man-to-md\markdown\*"
folder_dirs = []

for item in glob.glob("..\man-to-md\markdown\*"):
    if os.path.isdir(item):
        folder_dirs.append(item)
        
for folder_dir in folder_dirs:
    folder = folder_dir.split("\\")[-1]

    yml += f"    - {folder}:\n"
    yml += f"      - {folder}/index.md\n"

    if not os.path.exists(f".\docs\{folder}"):
        os.makedirs(f".\docs\{folder}")

    for filename_dir in glob.glob(f"{folder_dir}\*"):
        filename = filename_dir.split("\\")[-1]
        extension = filename.split(".")[-1]

        shutil.copyfile(filename_dir, f".\docs\{folder}\{filename}")

# Get home index.md
shutil.copyfile("..\man-to-md\markdown\index.md", ".\docs\index.md")


# for filename_dir in glob.glob(".\docs\*"):
#     filename = filename_dir.split("\\")[-1]
#     extension = filename.split(".")[-1]

#     yml += f"    - {filename.replace('.md', '')}: {filename}\n"

with open("mkdocs.yml", "w") as f:
    f.write(yml)

os.system("mkdocs serve")




