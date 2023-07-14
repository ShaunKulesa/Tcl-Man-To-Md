import glob

def fix_code_block(source: str):
    # The man .CS and .CE create 5 spaces whereas md uses 4 spaces for a code block

    """
    Output before:
    >     proc yieldm {value} {
    >         yieldto return -level 0 $value
    >     }
    """

    """
    Output after:
        proc yieldm {value} {
            yieldto return -level 0 $value
        }
    """
    
    # replace .CS with .nf in source files
    source = source.replace(".CS", ".nf")

    # replace .CE with .fi in source files
    source = source.replace(".CE", ".fi")

    return source

for filename_dir in glob.glob("source\*"):
    filename = filename_dir.split("\\")[-1]
    extension = filename.split(".")[-1]

    if extension == "macros":
        continue
    
    else:
        with open(filename_dir, "r") as f:
            source = f.read()

            source = fix_code_block(source)
        
        with open(filename_dir, "w") as f:
            f.write(source)