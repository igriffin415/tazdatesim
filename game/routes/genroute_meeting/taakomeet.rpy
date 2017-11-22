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

        if(lmpoints <0 ):
            call goodlup
        else:
            call badlup

#unite



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        label goodlup:

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
                    call takehand
                "You got it":
                    call nohand

            mc "So. You're not Lup."

            notlup "Right-o."

            mc "I’m [mcname]. Nice to meet you?"

            "Not-Lup checks out their nails and studies you carefully."

            taako "You have the privilege of meeting her delightful brother Taako. How’d you meet Lup, my dude? Obviously you don’t know her too well if you thought she could be me."

            mc "I actually just met her this morning. She was looking for some guy and we ended up chatting for a bit. She seemed really cool!"

            taako "Is she still looking for Greg? Gods, I told her to leave him and just fill his car with gogurt. Teach the shit a lesson."

            menu:
                "{i}Laugh{/i}":
                    call laugh
                "{i}Agree{/i}":
                    call agree
                "{i}Disagree{/i}":
                    call disagree


            return

        label takehand:
            $tmpoints += posAnswer

            mc "Thanks."

            "You grasp their hand and stand up straight, brushing your hand back through your hair and patting down your clothes. Hoping they won’t notice you aren’t making eye contact."

            return

        label nohand:
            $tmpoints += negAnswer

            "Waving their hand away you get yourself to your feet. No reason to make yourself seem more incompetent. Brushing your hand back through your hair and patting down your clothes, you hope they won’t notice you aren’t making eye contact."

            return

        #~~~~

        label laugh:
            $tmpoints += posAnswer

            "You can’t help but snicker at the mental image."
            #show taako happy
            mc "Ok, but seriously? If it comes to that, let me know. I want in."
            return

        label agree:
            $tmpoints += neutAnswer
            mc "That’s a great revenge plan, Taako. If it comes to that let me know how it goes."

            taako "Will do, bubeleh."
            return

        label disagree:
            $tmpoints += negAnswer
            mc "Isn’t that kind of mean? Like, sure he was a douche but property damage is a bit extreme."
            #show taako angryears

            taako "Keep talking like that and you might earn yourself a ticket on the Gogurt Limited."

            "You hold up your hands defensively. He takes his pranks pretty seriously."

            mc "Please don’t gogurt my stuff. I won’t tell, scout’s honor."

            taako "Fine, but only ‘cause you asked nicely."

            return

#~~~~~~~~~~~
        label badlup:

            "What luck you have. It’s Lup. You stare a bit longer than you should have, and before you know it, you’re making eye contact with her. Your reflexes are far less than cat-like; there’s no way she didn’t spot you, and after the impression you made you doubt she didn’t recognize you there."

            "Maybe if you snuck away now? Where’s the exit?"

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
