# Get all command names and what file they originate from.
proc get_commands {dir} {
    
    # "command": "file"
    set command_file [dict create]

    # Get all files in the directory.
    set files [glob -nocomplain -directory $dir *]
    
    # Iterate over all files.
    foreach file_dir $files {

        # Get the file name.
        set file_name [file tail $file_dir]
        
        # Open the file.
        set file [open $file_dir r]

        # Get the file contents.
        set contents [read $file]
        
        # Split the contents into lines.
        set lines [split $contents "\n"]
        
        # Get the index of the NAME section.
        set name_index [lsearch $lines "# NAME"]

        if {$name_index != -1} {
            set commands_line [lindex $lines [expr $name_index + 2]]
            
            # Get the index of the next section to get the string of that section line.
            set next_section_index [string first "#" $contents [expr [string first "# NAME" $contents]+1]]
        
            # Get the string of the next section title
            set next_section_title [string trim [string range $contents [expr $next_section_index] [expr [string first "\n" $contents $next_section_index]-1]]]

            # Get next section index in lines
            set next_section_index [lsearch $lines $next_section_title]
            
            # Get the command's lines between the NAME section and the next section.
            set command_lines [lrange $lines [expr $name_index + 2] [expr $next_section_index - 1]]
            
            # Join the command lines into a single string.
            set command_line [join $command_lines ""]
            
            # Get the command names.
            set command_names [split [lindex [split $commands_line "-"] 0] ","]
            
            # Remove whitespace from the command name and append it to $command_file
            foreach command_name $command_names {
                dict set command_file [string trim $command_name] $file_name
            }
        }
    }
}

get_commands ".\\markdown-output"


