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
    define unknown = Character("????")
    define steven = Character("Steven")
    define julia = Character("Julia")


# The game starts here.
label start:
    jump nameChara
    return

label start2:
    #bg: cab interior
    #sprite: none

    scene bg cab with dissolve

    mc "Well. This is it I guess. First week at COLLEGE NAME? Let's make it a good one."

    "The cab driver looks at you funny in her mirror as you insert your card into the machine to pay for the ride. {i}Guess I started my internal monologue out loud,{/i} you think to yourself."

    "Sometimes shit happens. Sometimes that shit involves moving across the country and transferring all your credits to a brand new school to finish your degree."

    "But hey, gotta roll with the punches. No use in worrying about that. You’re here now."

    #bg: campus entrance
    #sprite: none

    scene bg college

    "Stepping out of the car into the breeze, you can smell the faint smell of salt and fish on the breeze. You had forgotten that this was a beach town. That’d be nice in the summer, at least."

    "The cab driver pops the trunk with a Click!, and you lift your bags out from the recess and heft the messenger bag over your head and onto your shoulder."

    "{i}Thank god I got the bags with wheels,{/i} you think to yourself, hopping over the curb and…"

    jump magnusmeet.meet

    #after all lup meeting choices

    label finddorm:

        "Where {i}was{/i} your dorm? You study it carefully before folding it gently and sticking it into your jacket pocket for easy access."

        "You’ll definitely need to look over it at least two more times."

        "You make your way slowly over to the entrance, taking note of the signs plastered in the large buildings."

        "Arcana Hall… Interesting. You can see Roost Hall in the distance and an huge building with a very large dome sitting atop it. You have no idea what that building is used for but the dome is cool. Looks like there’s a mural on it from here."

        "Oh! Nestled into the corner of Roost Hall is a library. You’re probably going to spend a ton of time in there; you can’t work on your homework unless you’re in that kind of environment. You get too distracted."

        "You’ll probably check that out once you settle into your dorm. Gotta focus on that first."

    return

label nameChara:
    scene bg black
    $ mcname = renpy.input("What is your name?")
    $ mcname = mcname.strip()
    define mc = Character("[mcname]")
    jump start2
