import glob

def keywords_hyperlink():
    """
    FROM:

    # SEE ALSO

    coroutine(n), generator(n)
    """

    """
    TO:

    # SEE ALSO

    [coroutine(n)](coroutine.md), [generator(n)](generator.md)
    """  

    """
    FROM:

    # KEYWORDS

    coroutine, generator
    """
    
    """
    TO:

    # KEYWORDS

    [coroutine](coroutine.md), [generator](generator.md)
    """

    for filename_dir in glob.glob(".\markdown\*"):
        with open(filename_dir, "r") as f:
            source = f.read()

            for index, line in enumerate(source.split("\n")):
                if line.startswith("# SEE ALSO"):
                    print(line)
                    for key in source.split("\n")[index+2].split(", "):
                        source = source.replace(key, f"[{key}]({key[:-3]}.md)")

        with open(filename_dir, "w") as f:
            f.write(source)

keywords_hyperlink()