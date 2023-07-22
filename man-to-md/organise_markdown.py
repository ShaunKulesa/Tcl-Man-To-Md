from bs4 import BeautifulSoup
import requests
import glob
import shutil
import os

url = 'https://www.tcl.tk/man/tcl/'
ext = 'html'

sub_dirs = ["UserCmd", "TclCmd", "TkCmd", "ItclCmd", "SqliteCmd", "TdbcCmd", "TdbcmysqlCmd", "TdbcodbcCmd", "TdbcpostgresCmd", "ThreadCmd", "TclLib", "TkLib", "ItclLib", "TdbcLib", "Keywords"]

def listFD(url, ext=''):
    page = requests.get(url).text
    # print(page)
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

markdown_files = []

for file_dir in glob.glob(".\markdown\*"):
    markdown_files.append(file_dir.split("\\")[-1].split(".")[0])

for sub_dir in sub_dirs:
    if not os.path.exists("./markdown/" + sub_dir):
        os.mkdir("./markdown/" + sub_dir)
    
    for file_dir in listFD(url+sub_dir, ext):
        file = file_dir.split("/")[-1].split(".")[0]

        if file in markdown_files:            
            shutil.copyfile("./markdown/" + file + ".md", "./markdown/" + sub_dir + "/" + file + ".md")

# Get all comma separated command names under `# NAME` before the `-` in the markdown file



# get each folder name in .\markdown
rootdir = ".\markdown"
file_dirs = []

for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        file_dirs.append(file)

# print(file_dirs)

for file_dir in file_dirs:
    # {"command": "filename"}
    command_files = {}

    for filename_dir in glob.glob(".\markdown\\" + file_dir + "\*"):
        filename = filename_dir.split("\\")[-1].split(".")[0]
        extension = filename_dir.split("\\")[-1].split(".")[-1]

        with open(filename_dir, "r") as f:
            lines = f.readlines()
            
            start_index = None
            end_index = None
            commands = ""

            index = 0

            for line in lines:
                # get index of lines between .SH SYNOPSIS and the next .SH
                
                # get start index
                if "# NAME" in line:
                    # print(line)
                    start_index = index + 1
                    # print()
                    continue
                    
                # get end index
                if start_index != None:
                    if "#" in line:
                        # print(line)
                        end_index = index
                        break
                
                index += 1
                
            # print(lines[start_index:end_index + 1])
            if not start_index == None and not end_index == None:              
                for section_line in lines[start_index:end_index + 1]:

                    # remove all newlines
                    section_line = section_line.replace("\n", "")
                        
                    # append to commands
                    commands += section_line

                commands = commands.split("-")[0].replace(" ", "").split(",")
                
                for command in commands:
                    command_files[command] = filename + ".md"
            
    # Create index.md file for each folder
    with open("./markdown/" + file_dir + "/index.md", "w") as f:
        f.write("# " + file_dir + "\n\n")
        f.write("## Commands\n\n")
        for command in command_files:
            f.write("- [" + command + "](" + command_files[command] + ")\n")

# Create home index.md file
with open("./markdown/index.md", "w") as f:
    f.write("# Tcl/Tk\n\n")
    f.write("## Categories\n\n")

    for file_dir in file_dirs:
        f.write("- [" + file_dir + "](" + file_dir + "/index.md)\n")
