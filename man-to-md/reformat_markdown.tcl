package require fileutil

#coroutine(n), generator(n)

#[coroutine(n)](coroutine.md), [generator(n)](generator.md)
  

foreach filename_dir [glob -directory "./markdown" -type f *] {
    set fp [open $filename_dir r]
    set source [read $fp]
    close $fp

    set lines [split $source "\n"]
    set index 0

    foreach line $lines {        
        if {$line == "# SEE ALSO"} {

            set keywords [lindex $lines [expr $index + 2]]
            puts $keywords

            
            foreach keyword $keywords {
                # set keyword [string trim $keyword]
                puts $keyword
                
                # puts \"\[$keyword\]\"
            }
        }

        incr index
    }
}