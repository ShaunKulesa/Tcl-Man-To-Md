# Tcl-Man-To-Md

## What is the aim?

The aim of this is it to convert the man pages written in nroff to markdown which is a modern and universal solution for everyone.

From that point onwards the man pages will then be edited by the community as markdown. This opens up a bigger opportunity as the markdown can be converted back to nroff for those who need it or it can be converted to plain html.

This also allows us to use software such as mkdocs to convert the markdown into a modern looking documentation.

## Tools needed

### Pandoc:

This is used to convert many types of formats to each other, custom converters can also be written in lua so that may be something to look into. 

It is used in 1man_to_md.py to convert the man pages to markdown.

Download - https://pandoc.org/installing.html

### Mkdocs:

This is used to convert the markdown files into a modern looking documentation (theme is "readthedocs").

Download - "pip install mkdocs" using python 3.8 and above.
