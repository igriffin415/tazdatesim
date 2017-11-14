label magnusmeet:

label .meet:
        python:
            points = 0
            posAnswer = 3
            neutAnswer = 0
            negAnswer = -3
            wtf = False

        #bg library hallway
        scene bg hallway with dissolve

        "Lucretia sure was something. Smart, but kinda reserved? You wonder to yourself what it might take to get her out of her shell a bit, but a sudden buzzing coming from Roost Hall distracts you."

        "It fades suddenly. It was coming from Roost Hall? The place seems interesting; lots of people are walking in and out. The hall is well lit and warm, decorated with a variety of wood, metal and stone art pieces."

        "There are quite a few people bustling up and down the corridor, entering rooms that are alive with laughter and creation. The building seems to be home to a variety of trades, from the signs: metalworking, carpentry, electrics...the list goes on."

        "{i}What the-?{/i} Curiosity gets the better of you as you gently push open the classroom door."

        scene bg roost with dissolve

        "Opening the door a sliver, you see the buzzing is coming from a young woman in goggles and ear protectors operating some kind of saw. There’s an older man as well, who appears to be varnishing a cabinet in a nice cherry."

        "Neither of them seem to have noticed you yet. They both appear very intent on their tasks, to the point of shutting out the world around them, and you-"

        show magnus neutral at right with CropMove(.1, "slideleft") #or zoomin? can't change the time tho

        unknown "MAGNUS!!"

        mc "{i}What the -{/i}"

        menu:

            "{i}Fight{/i}":
                call fight

            "{i}Flight{/i}":
                call flight

            "{i}Freak out{/i}":
                call freak

        show steven neutral at left with easeinleft
        show magnus neutral
        unknown "Magnus! We’ve talked about this, don’t yell in my workshop! People are operating machinery in here!"

        magnus "Sorry Steven!"

        steven "Honestly. You’re a walking health and safety violation."

        "Magnus laughs. Steven does not. Suddenly he turns to direct his ire to you."

        #show magnus happy; show steven stern

        steven "If you’re going to loiter put some safety glasses on. If you take an eye out, it’s not going to be on my watch."

        "You mumble an affirming greeting and grab a pair out of the bucket next to the door. There. Nothing can kill you now. While you wear these glasses you are invincible."

        "Or at least, shit won’t fly into your eyes, you guess. "

        hide steven with easeoutleft

        "As the older man goes back to his work, Magnus turns back to you with a grin on his face."

        menu:

            "Health and Safety, hm?":
                call HaS

            "What the hell?":
                call wtf


        if(wtf):
            menu:

                "{i}Tell him.{/i}":
                    call tellname

                "{i}No way!{/i}":
                    call noname

        else:
            menu:

                "{i}Tell him.{/i}":
                    call tellname

                "{i}No way!{/i}":
                    call noname

                "{i}Health and Safety Inspector{/i}":
                    call inspector

        magnus "Nice to meet you, [mcname]! I haven’t seen you around here before, are you a new student? You interested in woodworking at all?"

        mc "I'm brand new here actually. I was just looking for the source of that buzzing sound from the machine over there."

        magnus "Oh, that’s just Jules. Julia!"

        "You notice that the whirring buzz that filled the room has stopped, and the woman who was manning the buzz saw is coming towards you, both ear protectors and goggles in hand. She’s got a remarkable resemblance to Steven -- maybe they’re related?"

        show julia neutral at left with easeinleft

        julia "Magnus, have you been scaring the regular folk again?"

        magnus "Oh, come on! Why is {i}everyone{/i} on my case about this?"

        "She smirks at him before turning to you with a warm smile."

        julia "Don’t mind the big guy, he’s just being difficult. Welcome to Hammer and Tongs! The name’s Julia."

        "She extends her hand."

        #move menu to center
        menu:

            "{i}Go in for a fistbump.{/i}":
                call bump

            "{i}Shake her hand.{/i}":
                call shake

            "{i}Don't take her hand.{/i}":
                call noshake

        julia "I should probably get back to work. You know how it is, those deadlines sneak up on ya!"

        magnus "Yeah, same here. I’ve got to finish the maquette for my rocking chair for next Tuesday."

        julia "Still, hope to see you around, yeah? And you know, these workshops aren’t just for folk studying trades or arts. Anyone can use them! So if you ever feel like carving something, come visit and I’ll give you a hand. Or my Dad will. He’s the tech here!"

        "{i}She gestures to Steven.{/i}"

        if(points>=0):
            show magnus happy
            magnus "Yeah! See you, [mcname]."

        else:
            show magnus neutral
            magnus "Yeah. See you."

        hide julia with easeoutleft
        hide magnus with easeoutright
        "With a wave, they head back into the workshop, leaving you to continue exploring the campus."

        #for debugging
        "You have %(points)d points"

        return
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        label flight:

            $points += neutAnswer

            "You turn and make a break for it without missing a beat. Scrambling away, you fail to notice the slight elevation of the doorway and fall backwards, landing on your back."

            "The voice comes back again, now at a regular volume."

            show magnus concerned

            unknown "Sorry, sorry! Didn’t mean to scare ya so badly!"

            "Ow. You sit up slowly, that's going to smart tomorrow morning."

            "Jeez, that was embarrassing.  You sheepishly look up at the person who startled you for the first time."

            "...Woah. {i}Muscles{/i}."

            return

        label freak:

            $points += neutAnswer

            "Nope. Nope nope nope. This is not what you signed up for today. Your brain takes over and opens your mouth for you. It takes a second for you to realize that you are now screaming back in his face."

            mc "AAAAAAA{i}AAAAAAAHHH!{/i}"

            unknown "YEEAAHH!!!"

            "You pant, slightly out of breath and throat sore from the yelling. Jeez, that was embarrassing.  You sheepishly look up to look at the person who startled you for the first time."

            "...Woah. {i}Muscles{/i}."

            return

        label fight:

            $points += posAnswer

            "Before you can even process what was happening, your arm is in the air and your hand feels like you’ve just hit a brick wall. "

            mc "Shit! Ouch!"

            unknown "That hurt! Nice punch! You have some good reflexes dude."

            "{i}Is he for real?{/i}"

            "You bite back a retort while nursing your hand. Fuck, did you split a knuckle? You look up at whatever boulder-ass motherfucker you just hit to give him a {i}look{/i}. A “What the fuck was {b}that{/b}???” Look."

            "...Woah. {i}Muscles{/i}."

            return

        #~~~~~~~~~~~

        label wtf:

            $points += negAnswer
            $wtf = True

            mc "What the hell was that for, you punk?! You can’t just go and scare people like that, geesh!"

            magnus "Haha, sorry about that! It’s just, my thing, you know? Seeing how fast people can react. It’s nothing personal, I’m sorry. Hey, I didn’t catch your name..?"

            return

        label HaS:

            $points+= posAnswer

            magnus "Yup! Health and Safety Violation, that’s me! Haha, the name’s actually Magnus, Magnus Burnsides. Hail and well met and all that, what’s your name?"

            return

        #~~~~~~~~~

        label tellname:

            $points += neutAnswer

            mc "My name's [mcname]. It's nice to meet you!"

            return

        label noname:

            $points+= negAnswer

            mc "You just shouted at me for no reason, I don’t see why I should tell you anything!"

            "Magnus frowns, shifting uncomfortably. He looks apologetic."

            magnus "Okay, I’m seriously sorry about that. I didn’t realise it would upset you that much, but it was a dick move. I won’t do it again."

            mc "Fine... I'm [mcname]."

            return

        label inspector:

            $points += posAnswer

            mc "My name is..."

            mc "The Health and Safety inspector."

            #show magnus concerned

            "Magnus pales slightly. Steven looks up at the mention of an inspector with concern before you laugh."

            mc "No it’s not, dingus! That’s not even a name! I’m [mcname]."

            return

        #~~~~~~~~~~~~~~~

        label bump:

            $points += posAnswer

            "Julia blinks in confusion for a second, but she gets the picture pretty fast, laughing loudly and closing her fist to knock her knuckles against yours."

            #show julia happy

            julia "Ahaha! I get it! Handshake too boring for you, that it? [mcname], wasn’t it? Well, if you aren’t too cool for school I hope I’ll see you round here again."

            "Magnus snickers."

            magnus "That was real stinker, Jules. If you tell jokes that bad [mcname] definitely won’t be coming back!" #name originally was pronoun. thoughts?

            return

        label shake:

            $points += neutAnswer

            "You blink at Julia’s outstretched palm for a second, before smiling back at her and taking it. Her palms are broad and calloused, and she’s warm."

            mc "Uh, it’s a pleasure! I’m [mcname]."

            julia "Yeah, I caught it earlier! And anyway, the pleasure’s mine. It’s always great to see new faces around here, even if they are attracted by the shoddy soundproofing..."

            "She sighs."

            julia "If you see that Kalen around, tell him to stop cutting our budget! Nah, I’m just kidding. It’s not your business."

            return

        label noshake:

            $points += negAnswer

            "The moment stretches."

            "...Julia realises that you rebuffed her gesture, and lowers her hand awkwardly."

            julia "..."

            julia "Well, okay! Not a handshake person, I see. That’s fine."

            #magnus frowns

            magnus "..."

            return
