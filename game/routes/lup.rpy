label lup:

label .meet:
        #bg: campus entrance
        #sprite: lup serious

        scene bg college
        show lup neutral at right

        "Out of nowhere there’s a girl. And she’s in your face. And she’s asking you a very insistent question."

        unknown "Have you seen a jackass named Greg FUCKING Grimaldis?"

        menu:

            "I haven't, sorry.":
                jump havenot

            "Nope.":
                jump nope

            "Even if I had, I probably wouldn’t tell YOU.":
                jump evenif


        label havenot:

            jump coursenot


        label nope:

            #sprite: lup distrusting

            mc "I haven't."

            "The girl studies your face for a moment."

            unknown "You aren’t trying to pull a fast one on me, are ya?"

            menu:

                "No, of course not.":
                    jump coursenot

                "No?":
                    jump no

                "And if I am?":
                    jump andif




            label coursenot:

                mc "No sorry, I actually just got here? I’m not even sure who that is. What did he do?"

                #sprite: lup relaxed

                lup "New, huh? Nice to meet you, I’m Lup."

                mc "I'm [mcname]!"

                lup "Anyway~, Greg Grimaldis borrowed 15 bucks from me. I’m a nice person. He needed the cash, I gave him it. That wouldn’t be a problem! Except now the motherfucker is refusing to pay me back."

                mc "Well that’s shitty of him."

                #sprite: lup serious

                lup "Right?! Anyway, I have a plan on getting the money out of his slimy hands, but I need to find the bastard first."

                mc "What’s your plan, Lup?"

                #sprite: lup flirty

                lup "That's more of a third date question, yeah?"

                menu:

                    "{i}Ignore the comment.{/i}":
                        jump ignore

                    "{i}Flirt back.{/i}":
                        jump flirt

                label ignore:

                    "You decide to ignore that. Probably better in the long run. She seems WAY out of your league."

                    #sprite: lup neutral

                    lup "Anyway, keep an eye out for Greg. Catch you later!"

                    "You wave as she disappears quickly into the sea of people. She seems really nice. You hope you get to see her again."

                    jump goodside

                label flirt:

                    mc "And how could I go about getting one of those “third dates”..?"

                    #sprite: lup laugh

                    lup "You seem cool, TERM OF ENDEARMENT. Maybe I’ll see you around?"

                    menu:

                        "Help you look?":
                            jump help

                        "Good luck!":
                            jump goodluck

                    label help:

                        mc "Maybe I could help you look for him after I get my things to my dorm? If I could figure out where that is…"

                        #sprite: lup happy

                        lup "I appreciate that, but I don’t have time to waste. Every second I spend not finding Greg is a second wasted. Or maybe not. I wouldn’t call this a waste of time. "

                        "You laugh. Lup seems really nice? She’s just radiating this awesome vibe. You could see yourself getting to know her better."

                        jump goodside

                    label goodluck:

                        mc "I try my best. Anyway, Good luck finding him! I hope that you catch him quickly."

                        lup "Me too, Hombre. Catch you later!"

                        "And with a quick wave, she’s gone. Lost in the sea of people that moved around you."

                        "It’s too bad she had to leave so quickly. You really enjoyed that chat."

                        jump goodside




            label andif:

                mc "And if I am? What could you even do about it?"

                jump badchoice


            label no:

                mc "No?"

                #sprite: lup relaxed

                lup "No sweat! If you see him though? Tell him “When Lup finds you, your ass is grass.”"

                "And with that, “Lup” disappears into the sea of people. {i}What a strange person. I pity Greg for whatever the hell he did.{/i}"

                jump goodside

        label evenif:

            mc "Nope. Honestly if I had I wouldn’t tell you, if you’re so vindictive you’re demanding people tell you where some dude went. "

            jump badchoice

        label badchoice:

            #sprite: lup distrusting

            "Her eyes narrow."

            lup "Listen, you don’t have to be an asswipe about this. Greg’s got this coming for him. He doesn’t fuck over Lup and get away with it."

            menu:

                "What did he do?":
                    jump whatdid

                "Sorry I thought you might just be bullying him.":
                    jump bullying


            label whatdid:

                lup "Listen, thug. At this point it’s not of your damn business. If you see his sorry ass? Tell him “Lup’s coming. And when she finds you? Your ass is grass.”"

                jump badside

            label bullying:

                lup "Are you kidding me? That’s the kind of person you think I am?? You don’t even know me!"

                jump badside

            label badside:

                "And with that, she angrily bumps past you, disappearing into the sea of people."

                "For a second you think, {i}Wow I’d hate to get on her bad side.{/i} But it occurs to you that maybe you already have…"

                "Might as well just head to your room. You pull out your wallet to take the map out of the billfold, and…"

                "Fuck. You’re missing 15$?!? It couldn’t have been Lup, you would have noticed. Probably just fell out on the trip here."

                jump finddorm

            label goodside:

                "You pull out your wallet to take the map out of the billfold."

                jump finddorm
