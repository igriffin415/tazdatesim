label taakomeet:

label .meet:
        python:
            tmpoints = 0
            posAnswer = 3
            neutAnswer = 0
            negAnswer = -3
            #neglup = lupmeet.meet.points <  0

        scene bg legato with dissolve

        "You leave Roost Hall and wander for a bit, scrolling through your phone. Notifications are lacking, so you find yourself looking around at the scenery."

        "Walls covered in projects and schematics turn into paintings and sculpture. Judging by the fashion around you and the general vibe you’ve probably entered the Arts Building."

        "You check your map; Legato Hall. Pretty name. Big building too. You could probably get lost in here for hours looking at the art and listening to students playing music in dead-end hallways and people reading from scripts mumbling lines under their breath."

        "Auditions must start pretty early if the theatre kids are freaking out already."

        "But they’re theatre kids, so could you really tell?"

        "You turn a couple corners here and there, letting yourself get pretty lost when suddenly you’re swept up in a literal sea of people. What the hell is this?"

        "You try to escape but you’re helpless to do anything but go with the flow and walk with them. Surely they’ll stop somewhere and you can find your way back to your dorm. You’ve probably had enough of {i}whatever{/i} this is for one day."

        "You finally stumble to a stop in an auditorium, and the crowd disperses around you, joining the others already here, chatting and eating snacks. Some kind of party? A mixer."

        "You turn to escape, but your eye catches a familiar face and you double take."

        if(lmpoints < 0 ):
            call .badlup
        else:
            call .goodlup

#unite
        mc "So what’s all this for?"

        "You gesture outwards at the people around you."

        "Oh this shindig? Welcome back party for theatre nerds."

        menu:
            "Why are you here?":
                call .why
            "Yeah, you seem the type.":
                call .yeah
            "Oh.":
                call .oh

        hide taako with easeoutright
        "You weasel your way out of the auditorium and down the hall, the sounds of people still following you in the echoes, even as you get further and further from the fray."

        "Probably not. You’re better off trying to find your way out of Legato entirely."
        #for debugging
        "You have %(tmpoints)d points"
        return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        label .goodlup:

            "It’s Lup! What cool coincidence, seeing her twice in one day. You wait until she meets your eyes and you wave, walking towards her as she looks at you inquisitively."

            "That’s weird though, she almost looks like she doesn’t recognize you. You swallow back a lump in your throat. Maybe not too weird. She seems like a pretty popular person. You’re probably just another face in the crowd-!"

            "You’re so focused on your inner monologue that you miss a step and fall flat on your face."

            "Right in front of Lup."

            "Cool. Great. Definitely not embarrassing. {i}Play it off, [mcname].{/i}"

            mc "Hey. Long time no see?"

            show taako neutral at right with easeinright

            notlup "No see’s for sure. Good to know even strangers are falling for me though."

            "Yeah that’s not Lup. Your face flushes uncomfortably as you push yourself up. A hand is stretched out and Not-Lup is offering you a help up."

            menu:
                "Take it greatfully":
                    call .takehand
                "You got it":
                    call .nohand

            mc "So. You're not Lup."

            notlup "Right-o."

            mc "I’m [mcname]. Nice to meet you?"

            "Not-Lup checks out their nails and studies you carefully."

            taako "You have the privilege of meeting her delightful brother Taako. How’d you meet Lup, my dude? Obviously you don’t know her too well if you thought she could be me."

            mc "I actually just met her this morning. She was looking for some guy and we ended up chatting for a bit. She seemed really cool!"

            taako "Is she still looking for Greg? Gods, I told her to leave him and just fill his car with gogurt. Teach the shit a lesson."

            menu:
                "{i}Laugh{/i}":
                    call .laugh
                "{i}Agree{/i}":
                    call .agree
                "{i}Disagree{/i}":
                    call .disagree


            return

        label .takehand:
            $tmpoints += posAnswer

            mc "Thanks."

            "You grasp their hand and stand up straight, brushing your hand back through your hair and patting down your clothes. Hoping they won’t notice you aren’t making eye contact."

            return

        label .nohand:
            $tmpoints += negAnswer

            "Waving their hand away you get yourself to your feet. No reason to make yourself seem more incompetent. Brushing your hand back through your hair and patting down your clothes, you hope they won’t notice you aren’t making eye contact."

            return

        #~~~~

        label .laugh:
            $tmpoints += posAnswer

            "You can’t help but snicker at the mental image."
            #show taako happy
            mc "Ok, but seriously? If it comes to that, let me know. I want in."
            return

        label .agree:
            $tmpoints += neutAnswer
            mc "That’s a great revenge plan, Taako. If it comes to that let me know how it goes."

            taako "Will do, bubeleh."
            return

        label .disagree:
            $tmpoints += negAnswer
            mc "Isn’t that kind of mean? Like, sure he was a douche but property damage is a bit extreme."
            #show taako angryears

            taako "Keep talking like that and you might earn yourself a ticket on the Gogurt Limited."

            "You hold up your hands defensively. He takes his pranks pretty seriously."

            mc "Please don’t gogurt my stuff. I won’t tell, scout’s honor."

            taako "Fine, but only ‘cause you asked nicely."

            return

#~~~~~~~~~~~
        label .badlup:

            "What luck you have. It’s Lup. You stare a bit longer than you should have, and before you know it, you’re making eye contact with her."

            "Your reflexes are far less than cat-like; there’s no way she didn’t spot you, and after the impression you made you doubt she didn’t recognize you there."

            "Maybe if you snuck away now? Where’s the exit?"

            show taako neutral at right with easeinright

            notlup "Hey."

            "You jump, whipping your head around as you’re pulled out of your inner monologue. And then the confusion hits. The voice doesn’t match the face."

            mc "You aren't Lup."

            taako "Quite the conversationalist, aren’t we. This is Taako speaking, Lup can’t come to the phone right now since she’s off doing whateverthefuck while I’m at this ‘party’."

            "You snicker at the joke."

            mc "Sorry; she and I didn’t get off on quite the right foot. I was a bit nervous seeing, well, you here because of it."

            taako "Yeah, I get that a lot, being her twin brother and all. She looking for Greg still?"

            mc "How’d you guess?"

            taako "She gets pretty heated when she’s dealing with that fucker. Unless you royally fucked up I doubt she’ll hold it against you for long."

            "You shrug. No point in dragging this Lup-talk out any further."

            return

        #~~~~~~~~~~~~~

        label .why:
            $tmpoints += posAnswer

            mc "If it’s for nerds, what’s someone like you doing here?"

            taako "Cause if there’s a party I {i}have{/i} to be there. Also it’s my major so i sorta need to be."

            mc "Oh that’s cool! Are you going to be in any of the shows this year."

            taako "You know it. Cha’boys a star."

            menu:
                "{i}Gush about theatre.{/i}":
                    call .gush
                "Cool!":
                    call .cool

            taako "I dabbled in a few different spots before deciding to do this. I’m already great at transmutation, don’t need to major in that, etcetera, etcetera."

            taako "What can I say, I live for the applause."

            "A small chime rang out from Taako’s side. He dug through his bag and pulled out his cell, his face lighting up while reading his notifications."

            taako "Oh shit, bone boy’s coming through for Taako. You met Krav? He’s pretty cool. Got a lead on something more fun happening, wanna come?"

            menu:
                "I wish I could!":
                    call .iwish
                "Parties aren't really my thing.":
                    call .notmything
                "Yeah, no.":
                    call .yeahno

            return




        label .gush:
                $tmpoints += posAnswer
                mc "God I just love theatre."

                taako "No shit, huh?"

                mc "Yeah. What have you played in before?"

                taako "Bit parts here and there, best thing to do was Cabaret. I was the emcee."

                mc "Nice. Wish I could have seen that."
                #taako dismissive, nervous
                taako "Honestly Lup probably has a bootleg somewhere if you {i}really{/i} want to."

                #cocky look, ears down
                taako "Of course, it’s {i}me{/i} so why wouldn’t you."

                "He waved me off, changing the subject."
                return

        label .cool:
                $tmpoints += neutAnswer
                mc "Awesome you found something you like, Taako!"

                menu:
                    "I love my major!":
                        call .lovemajor
                    "I'm... {i}meh{/i} about my major.":
                        call .meh
                    "I don't like my major.":
                        call .dontlike


                return

        label .lovemajor:
                mc "It took me a bit to find something I settled into well, but I’m glad I did. I really enjoy it."
                return
        label .meh:
                mc "My major’s pretty cool. It’ll do me some good. Wish i was more passionate about it, though."
                return
        label .dontlike:
                mc "To be honest, I wish I liked my major more? Like in the long run it’s a good choice but it isn’t my passion, ya know?"
                return

        #~~~~~~~
        label .iwish:
                $tmpoints += posAnswer
                mc "I actually have to get going. This wasn’t on my to-do list. Still fun though."

                taako "Plus you got to meet me. That’ll brighten up any day, bubbeleh."

                taako "You run along then. I’ve got a bunch of nerds to hang out with."
                return

        label .notmything:
                $tmpoints += posAnswer
                mc "I appreciate the invite, but parties aren’t exactly my “thing”. I’m only still here cause I’m talking to you, If I’m honest."

                taako "Fair. I am pretty amazing conversation. You go on then. Maybe I’ll see you around."

                mc "I’ll be on the lookout. Bye!"
                return

        label .yeahno:
                $tmpoints += negAnswer
                mc "Yeah, no thanks."

                taako "Oh. Alright. See you alright."

                mc "Bye Taako."
                return

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        label .yeah:
            $tmpoints += neutAnswer
            mc "Yeah you seem like the theatre type."

            taako "What gave me away? Was it the fact I’m simultaneously over and underdressed, or just my aura that says I live for drama."

            #show taako happy
            "He laughs."

            mc "Both, honestly. You like it though?"

            taako "Hells yeah, man. Why would I be here if I didn’t?"

            mc "Some people just sorta deal if it’ll make ‘em money. Don’t think theatre’s that kinda place though."

            taako "Pfft. No shit."

            "A small chime rang out from Taako’s side. He dug through his bag and pulled out his cell, his face lighting up while reading his notifications."

            taako "Oh shit, bone boy’s coming through for Taako. I gotta run. Ta~!"
            return

        label .oh:
            $tmpoints += negAnswer

            mc "That's cool I guess."

            taako "Mhm. If this isn’t your shindig, the door’s thataway my dude."

            mc "Oh, I didn’t mean-"

            taako "Yeah whatever. I’ll call you."

            hide taako with easeoutright

            "Taako turned abruptly and walked through the crowd, plastering a smile across his face and giving a very enthusiastic girl a hug."

            "You wonder if you can salvage that whole thing…"

            "Probably not. You’re better off trying to find your way out of Legato entirely."
            return
