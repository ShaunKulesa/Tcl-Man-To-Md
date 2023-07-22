import glob
import os



for filename_dir in glob.glob(".\source\*"):
    filename = filename_dir.split("\\")[-1].split(".")[0]
    extension = filename_dir.split("\\")[-1].split(".")[-1]

    with open(filename_dir, "r") as f:
        lines = f.readlines()
        
        start_index = None
        end_index = None
        section_text = ""

        for line in lines:
            # get index of lines between .SH SYNOPSIS and the next .SH
            
            # get start index
            if ".SH SYNOPSIS" in line:
                start_index = lines.index(line) + 1
                continue
                
            # get end index
            if start_index != None:
                if ".SH" in line:
                    end_index = lines.index(line)
                    print(lines[start_index:end_index])
                    break
            
        # Delete all .nf and .fi lines
        if start_index != None and end_index != None:
            for index, line in enumerate(lines[start_index:end_index]):
                
                if ".nf" in line or ".fi" in line:
                    lines[start_index + index] = ""

            with open(filename_dir, "w") as f:
                f.writelines(lines)
                
    
            



            
            # if start_index != None:
            #     if ".SH" not in line:
            #         section_text += line
            
            # print(section_text)
                    
            
                