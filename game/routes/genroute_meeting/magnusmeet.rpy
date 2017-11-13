label magnusmeet:

label .meet:
        python:
            points = 0
            posAnswer = 3
            neutAnswer = 0
            negAnswer = -3

        #bg library hallway
        scene bg hallway
        #show magnus neutral at right
        "As you leave the library, you notice a muffled buzzing sound... it sounds like it’s coming from down the hall to your left."

        "Following the sound, you head down the hallway, into what a sign assures you is ‘Roost Hall’. The hall is well lit and warm, decorated with a variety of wood, metal and stone art pieces."

        "There are quite a few people bustling up and down the corridor, entering rooms that are alive with laughter and creation. The building seems to be home to a variety of trades, from the signs: metalworking, carpentry, electrics...the list goes on."

        "The buzzing you heard leads you to the woodworking workshop."

        "Opening the door a sliver, you see the buzzing is coming from a young woman in  goggles and ear protectors operating some kind of saw. There’s an older man as well, who appears to be varnishing a cabinet in a nice cherry."

        "Neither of them seem to have noticed you yet. They both appear very intent on their tasks, to the point of shutting out the world around-"

        show magnus neutral at right
        unknown "MAGNUS!!"

        mc "What the -"

        menu:

            "{i}Flight{/i}":
                call flight

            "{i}Fight{/i}":
                call fight

            "{i}Freak out{/i}":
                call freak

        unknown "Magnus! We’ve talked about this, don’t yell in my workshop! People are operating machinery in here!"

        magnus "Sorry Steven!"

        steven "Honestly. You’re a walking health and safety violation."

        "As the older man goes back to his work, Magnus turns back to you with a grin on his face."

        menu:
            "What the hell?":
                call wtf

            "Health and Safety, hm?":
                call HaS

        menu:

            "{i}Tell him.{/i}":
                call tellname

            "{i}No way!{/i}":
                call noname

            "{i}Health and Safety Inspector{/i}":
                call inspector

        magnus "Nice to meet you, [mcname]! I haven’t seen you around here before, are you a new student? You interested in woodworking at all?"

        mc "No, I was just looking for the source of that buzzing sound from the machine over there."

        magnus "Oh, that’s just Jules. Julia!"

        "You notice that the whirring buzz that filled the room has stopped, and the woman who was manning the buzz saw is coming towards you, both ear protectors and goggles in hand. She’s got a remarkable resemblance to Steven--maybe they’re related?"

        julia "Magnus, have you been scaring the regular folk again?"

        magnus "Oh, come on! Why is {i}everyone{/i} on my case about this?"

        "She smirks at him before turning to you with a warm smile."

        julia "Don’t mind the big guy, he’s just being difficult. Welcome to Hammer and Tongs! The name’s Julia."

        "She extends her hand."

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

        #magnus " [If positive/neutral] (grins) Yeah! See you, [Y/N]. [If negative] (neutral expression) Yeah. See you." #will figure out if statements in morning lmao

        "With a wave, they head back into the workshop, leaving you to continue exploring the campus."
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        label flight:

            "You turn and make a break for it without missing a beat. Scrambling away, you fail to notice the slight elevation of the doorway and fall backwards, landing on your back."

            "The voice comes back again, now at a regular volume."

            unknown "Sorry, sorry! Didn’t mean to scare ya so badly!"

            "Grumbling, you look up to see the person who startled you for the first time. ...Woah. {i}Muscles{/i}."

            return

        label freak:

            mc "AAAAAAA{i}AAAAAAAHHH!{/i}"

            unknown "YEEAAHH!!!"

            "You take a step back, jerking your head left and right to see your assailant. Following their laughter, you see them straighten from their hiding place and rise to their full height...Woah. {i}Muscles{/i}."

            return

        label fight:

            "{i}Thud.{/i}"

            mc "Ouch!"
            "{i}What the hell? That felt like punching a wall!{/i}"

            unknown " Ach! That hurt! Nice reflexes, buddy!"

            "Biting back a retort and rubbing your aching fist, you finally get a good look at the person who startled you. ...Woah. {i}Muscles.{/i}"

            return

        #~~~~~~~~~~~

        label wtf:

            mc "What the hell was that for, you punk?! You can’t just go and scare people like that, geesh!"

            magnus "Haha, sorry about that! It’s just, my thing, you know? Seeing how fast people can react. It’s nothing personal, I’m sorry. Hey, I didn’t catch your name..?"

            return

        label HaS:

            magnus " Yup! Health and Safety Violation, that’s me! Haha, the name’s actually Magnus, Magnus Burnsides. Hail and well met and all that, what’s your name?"

            return

        #~~~~~~~~~

        label tellname:

            mc "My name's [mcname]. It's nice to meet you!"

            return

        label noname:

            mc "You just shouted at me for no reason, I don’t see why I should tell you anything!"

            "Magnus frowns, shifting uncomfortably. He looks apologetic."

            magnus "Okay, I’m seriously sorry about that. I didn’t realise it would upset you that much, but it was a dick move. I won’t do it again."

            mc "Fine... I'm [mcname]."

            return

        label inspector:

            mc "My name is...."

            mc "The Health and Safety inspector."

            "Magnus pales slightly. Steven looks up at the mention of an inspector with concern before you laugh."

            mc "No it’s not, dingus! That’s not even a name! I’m [mcname]."

            return

        #~~~~~~~~~~~~~~~

        label bump:

            "Julia blinks in confusion for a second, but she gets the picture pretty fast, laughing loudly and closing her fist to knock her knuckles against yours."

            julia "Ahaha! I get it! Handshake too boring for you, that it? [mcname], wasn’t it? Well, if you aren’t too cool for school I hope I’ll see you round here again."

            "Magnus snickers."

            magnus "That was real stinker, Jules. If you tell jokes that bad [mcname] definitely won’t be coming back!" #name originally was pronoun. thoughts?

            return

        label shake:

            "You blink at Julia’s outstretched palm for a second, before smiling back at her and taking it. Her palms are broad and calloused, and she’s warm."

            mc "Uh, it’s a pleasure! I’m [mcname]."

            julia "Yeah, I caught it earlier! And anyway, the pleasure’s mine. It’s always great to see new faces around here, even if they are attracted by the shoddy soundproofing..."

            "She sighs."

            julia "If you see that Kalen around, tell him to stop cutting our budget! Nah, I’m just kidding. It’s not your business."

            return

        label noshake:

            "The moment stretches."

            "...Julia realises that you rebuffed her gesture, and lowers her hand awkwardly."

            julia "..."

            julia "Well, okay! Not a handshake person, I see. That’s fine."

            #magnus frowns

            magnus "..."

            return
