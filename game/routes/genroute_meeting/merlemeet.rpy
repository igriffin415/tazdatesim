label merlemeet:
    $ trustmerle = False
label .meet:
        python:
            mermpoints = 0
            posAnswer = 3
            neutAnswer = 0
            negAnswer = -3

        #bg: legato hall
        #sprite: merle neutral

        scene bg legato_hall
        with fade

        "You wander aimlessly through Legato Hall."
        "You distantly hear the distinct rhythms of up-tempo jazz music playing."
        "It is not unusual to hear music playing in the Legato given it is the hub for both the fine and performing arts."
        "You walk down the halls, following the sound of jazz music."
        "After a minute or two of searching, you find the source of the music."
        "A large, seemingly enchanted, boombox floods the halls with its uproarious melody."
        "You spot an older dwarven man at the end of the hallway."

        show merle neutral at right
        with moveinright

        "He is quickly approaching you, executing numerous spinning and kicking dance moves that all seem to be extremely technical in nature."
        "You are so enthralled by his dance that you only notice at the very last minute he is going to run you down, still kicking and spinning in time with the music."
        "You dive out of the way just as he performs a large jump, his trailing foot making him trip over your ankle."

        show merle neutral at right
        with hpunch

        "You groan in agony and grab your ankle."
        "The music screeches to a halt and you watch the man feel around for the thick glasses that fell off his face in the jump."
        "He puts them on and turns to you. He instantly looks appalled at what he has just done."
        "He scrambles nearer to you, on his hands and knees."

        unknown "I’m sorry I just got so caught up in the music and the routine I was working on. Are you okay? I hope I didn’t hurt ya."

        menu:
            "It's okay.":
                jump .imokay
            "Owww!":
                jump .owww
            "You're a careless fool!":
                jump .careless

        label .imokay:
            $ mermpoints += posAnswer
            mc "It’s okay.{w} I know what it's like to get caught up in something.{w} But I think you hurt my ankle with that last jump."
            jump .looksee

        label .owww:
            $ mermpoints += neutAnswer
            mc "I think you hurt my ankle with that last jump!"
            jump .looksee

        label .careless:
            $ mermpoints += negAnswer
            mc "Why weren’t you looking where you were going?{w} Why were you dancing the hall in the first place?{w} What were you thinking blasting music that loud?"
            mc "You messed up my ankle but if I hadn’t jumped out of the way you could have hurt me much worse."
            mc "I can’t believe someone as old as you would do this!"

            unknown "I’m really sorry. You’re right. I should’ve been paying more attention."
            "His eyes are sad, he almost looks dejected at your reprimand."
            jump .looksee

        label .looksee:
            "He gestures to your ankle."
            unknown "Can I have a look see? I’m an experienced cleric so I could heal that right up for you."
            menu:
                "Show him your ankle":
                    jump .showhim
                "Look at him with doubt":
                    jump .doubt

        label .showhim:
            "Without pause, you stick your foot out so he can inspect your ankle."
            $ trustmerle = True
            $ mermpoints += posAnswer
            jump .checkup
        label .doubt:
            "You shoot him an incredulous look but, after a moment, show him your ankle anyway.{w} You hope he is actually as experienced as he says he is."
            $ trustmerle = False
            $ mermpoints += negAnswer
            jump .checkup

        label .checkup:
            "He gingerly touches your ankle and nods a bit."
            unknown "It’s not in the best shape but no worse than a sprain. I’ll have you up and walking in just a minute."
            "He claps his hands and rubs them together while muttering a divine incantation. He touches your ankle."

            if trustmerle:
                "The pain is instantly gone."
            else:
                "After a moment the pain vanishes."

            "You feel completely restored."
            "He smiles at you."
            unknown "That one’s on the house on account of me doing the damage."
            "He winks."
            unknown "But, say, how did you like that routine I was doing?"

            menu:
                "Tell the truth":
                    $ mermpoints += posAnswer
                    jump .zoneoftruth
                "Downplay what you thought":
                    $ mermpoints += neutAnswer
                    jump .zoneoftruth
                "Lie":
                    $ mermpoints += negAnswer
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
            $ mermpoints += posAnswer
            mc "My name is [mcname!t]. It’s nice to meet someone as talented as you, Merle."
            jump .finalwords
        label .justname:
            $ mermpoints += neutAnswer
            mc "My name is [mcname!t], but I don’t know if I’m really a fan yet."
            jump .finalwords
        label .notafan:
            $ mermpoints += negAnswer
            mc "I’m not really a fan, but my name is [mcname!t]."
            merle "Well, we’ll have to change that! You just need to see more of my work."
            jump .finalwords

        label .finalwords:
            "He smiles jovially."
            merle "It’s always good to see a new face and it’s nice to meet you too, [mcname!t]!{w} What brings you to the Legato building anyway?{w} Anything you need help with?"
            mc "I was wandering around and was intrigued by the music you had on so I followed the sound of it."
            menu:
                "Good Music":
                    $mermpoints += posAnswer
                    mc "It sounded cool. Thought I’d check it out."
                    merle "Well I’m glad {i}somebody{/i} on this damned campus appreciates the music I dance to!"
                "Weird Music…":
                    $mermpoints += negAnswer
                    mc "It was honestly… Kind of weird. I didn’t expect to find the source of it."
                    merle "You can’t win em’ all I guess."
            merle "In any case, I have to keep practicing my moves. Don’t be a stranger."
            merle "If you ever wanna talk or need any help you can always find me over in the dance studio or the gardens."
            "He winks at you before running back up the hall and cartwheeling through one of the doorways leading into a dance studio."
            "You sit there in stunned silence for a moment."
            "You wonder how such an old man can have more energy and flexibility than you."
            "You stand up, dust yourself off, and decide where to head to next."
            "You have [mermpoints] Merle points."
            return
