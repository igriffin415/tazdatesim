## MAIN FILE


init:
    $ mcname = ""

    # IPRE
    define taako = Character("Taako")
    define magnus = Character("Magnus")
    define dav = Character("Davenport")
    define lup = Character("Lup")
    define barry = Character("Barry")
    define lucretia = Character("Lucretia")
    define merle = Character("Merle")

    # OTHERS
    define angus = Character("Angus")


# The game starts here.
label start:
    jump nameChara
    return

label start2:
    mc "I'm the main character"
    return

label nameChara:
    scene bg black
    $ mcname = renpy.input("What is your name?")
    $ mcname = mcname.strip()
    define mc = Character("[mcname]")
    jump start2
