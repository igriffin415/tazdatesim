image bg legato_hall = "cab.png"
image bg merle neutral = "merle neutral.png"
$trustmerle = False

label merlemeet:
    label .meet:
        python:
            points = 0
            posAnswer = 3
            neutAnswer = 0
            negAnswer = -3

        #bg: legato hall
        #sprite: merle neutral

        scene bg cab
        with fade

        "You wander aimlessly through Legato Hall."
        "You distantly hear the distinct rhythms of up-tempo jazz music playing."
        "It is not unusual to hear music playing in the Legato given it is the hub for both the fine and performing arts."

        menu:
            "Investigate":
                jump .investigate
            "Ignore it":
                jump .ignore

        label .investigate:
            "You walk down the halls, following the sound of jazz music."
            "After a minute or two of searching, you find the source of the music."
            "A large, seemingly enchanted, boombox floods the halls with its uproarious melody."
            "You spot an older dwarven man at the end of the hallway."

            show merle neutral at right

            "He is quickly approaching you, executing numerous spinning and kicking dance moves that all seem to be extremely technical in nature."
            "You are so enthralled by his dance that you only notice at the very last minute he is going to run you down, still kicking and spinning in time with the music."
            "You dive out of the way just as he performs a large jump, his trailing foot making him trip over your ankle."

            # hpunch

            "You groan in agony and grab your ankle."
            "The music screeches to a halt and you watch the man feel around for the thick glasses that fell off his face in the jump."
            "He puts them on and turns to you. He instantly looks appalled at what he has just done."
            "He scrambles nearer to you, on his hands and knees."

            merle "I’m sorry I just got so caught up in the music and the routine I was working on. Are you okay? I hope I didn’t hurt ya."

            menu:
                "It's okay.":
                    jump .imokay
                "Owww!":
                    jump .owww
                "You're a careless fool!":
                    jump .careless

            label .imokay:
                mc "It’s okay."
                "I know what it's like to get caught up in something."
                "But I think you hurt my ankle with that last jump."
                jump .looksee

            label .owww:
                "I think you hurt my ankle with that last jump!"
                jump .looksee

            label .careless:
                mc "Why weren’t you looking where you were going?
                Why were you dancing the hall in the first place?
                What were you thinking blasting music that loud?"
                mc "You messed up my ankle but if I hadn’t jumped out of the way you could have hurt me much worse."
                mc "I can’t believe someone as old as you would do this!"

                merle "I’m really sorry. You’re right. I should’ve been paying more attention."
                "His eyes are sad, he almost looks dejected at your reprimand."
                jump .looksee

            label .looksee:
                "He gestures to your ankle."
                merle "Can I have a look see? I’m an experienced cleric so I could heal that right up for you."
                menu:
                    "Show him your ankle":
                        $trustmerle = True
                    "Look at him with doubt":
                        $trustmerle = False

            label .showhim:
                "Without pause, you stick your foot out so he can inspect your ankle."
                jump .checkup
            label .doubt:
                "You shoot him an incredulous look but, after a moment, show him your ankle anyway.
                You hope he is actually as experienced as he says he is."
                jump .checkup

            label .checkup:
                "He gingerly touches your ankle and nods a bit."
                merle "It’s not in the best shape but no worse than a sprain. I’ll have you up and walking in just a minute."
                "He claps his hands and rubs them together while muttering a divine incantation. He touches your ankle."

                if trustmerle:
                    "The pain is instantly gone."
                else:
                    "After a moment the pain vanishes."

                "You feel completely restored."
                "He smiles at you."
                merle "That one’s on the house on account of me doing the damage."
                "He winks."
                merle "But, say, how did you like that routine I was doing?"

                menu:
                    "Tell the truth":
                        jump .zoneoftruth
                    "Downplay what you thought":
                        jump .zoneoftruth
                    "Lie":
                        jump .zoneoftruth

            label .zoneoftruth:
                mc "I thought it was amazing. I’ve never seen anything like that before."
                "He smiles wide."
                merle "I’m glad ta hear that! By the way, the name’s Merle Hightower."
                "You notice the student instructor badge he is wearing says his name is Merle Highchurch."
                "You point this out to him."
                "He chuckles."
                merle "Yeah, I always mess that up. Hightower is my middle name and Highchurch is my last name."
                merle "But, what’s your name? I’d love to know who my newest fan is."

                menu:
                    "Good to meet someone with real talent!":
                        jump .talent
                    "Tell him your name.":
                        jump .justname
                    "You're not a fan.":
                        jump .notafan

            label .talent:
                mc "My name is [mcname!t]. It’s nice to meet someone as talented as you, Merle."
                jump .finalwords
            label .justname:
                mc "My name is [mcname!t], but I don’t know if I’m really a fan yet."
                jump .finalwords
            label .notafan:
                mc "I’m not really a fan, but my name is [mcname!t]."
                merle "Well, we’ll have to change that! You just need to see more of my work."
                jump .finalwords

            label .finalwords:
                "He smiles jovially."
                merle "It’s always good to see a new face and it’s nice to meet you too, [mcname!t]!"
                "What brings you to the Legato building anyway?"
                "Anything you need help with?"
                mc "I was wandering around and was intrigued by the music you had on so I followed the sound of it."
                merle "Well I’m glad somebody on this damned campus appreciates the music I dance to!"
                "He chuckles."
                merle "In any case, I have to keep practicing my moves. Don’t be a stranger."
                merle "If you ever wanna talk or need any help you can always find me over in the dance studio or the gardens."
                "He winks at you before running back up the hall and cartwheeling through one of the doorways leading into a dance studio."
                "You sit there in stunned silence for a moment."
                "You wonder how such an old man can have more energy and flexibility than you."
                "You stand up, dust yourself off, and decide where to head to next."
                return

        label .ignore:
            "You leave the building."
            return
