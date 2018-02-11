label davenportmeet:

label .meet:
        python:
            dmpoints = 0
            posAnswer = 3
            neutAnswer = 0
            negAnswer = -3


        scene bg outside with dissolve

        "Finally! Sweet sunshine! You’d been wandering the halls for upwards of an hour, and it’s been hectic enough that the fresh air is incredibly refreshing."

        "It’s such a beautiful summer day right now! The walk is pretty far carrying textbooks like this but the weather more than makes up for it."

        "Your mood jumps enough that you hum a bit to yourself, regretting leaving your headphones in your dorm, but not letting that get you down at all. One of your books shifts awkwardly in your hand, and you look down to fix your grip on it when --"

        unknown "LOOK OUT!"

        mc "!!!"

        "CRASH!"

        "You’re rattled, looking around frantically from your new place on the pavement. Your books are scattered around you, there’s a bike on it’s side to your left and your arm is skinned up."

        menu:
            "Ow.":
                call .ow
            "Fuck!":
                call .fuck
        show dav neutral at right with easeinright
        menu:
            "I'm alright.":
                call .alright
            "{i}Flip off.{/i}":
                call .flipoff

        unknown "Sorry about that. I was running errands preparing for the new school year and wasn't watching where I was going. Here, let me help you."

        "He picks up your textbooks from where they fell, brushing off pieces of dirt as he does so. He hands the stack back to you."

        menu:
            "{i}Accept apology.{/i}":
                call .accept
            "{i}Grab them and glare.{/i}":
                call .glare

        menu:
            "{i}Accept his help.{/i}":
                call .accepthelp
            "{i}Decline graciously.{/i}":
                call .gracious
            "{i}Decline ungraciously.{/i}":
                call .ungracious

        menu:
            "{i}Excitedly describe major.{/i}":
                call .excite
            "{i}Just say the name of it.{/i}":
                call .namemajor
            "It’s nothing stupid like botany or illusion.":
                call .stupid

        call .party
        return
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        label .ow:
            $dmpoints += neutAnswer

            mc "Ow."
            "You sit dazed on the ground until a hand appears in front of you."

            unknown "Are you alright?"
            return
        #~~~~~~~~
        label .fuck:
            $dmpoints += negAnswer

            mc "That fucking hurt, asshole!"

            "You sit dazed but angry on the ground until a hand appears in front of you."

            unknown "That’s quite a mouth you have there. Are you alright?"

            return

        #~~~
        label .alright:
            $dmpoints += posAnswer

            mc "I'm alright."

            "You take the hand in front of your face and they help hoist you to your feet again."

            "The one helping you is a gnome man. Handsome, with a well-kept moustache. Even scuffed and ruffled from falling off his bike, he has a very impressive demeanour."

            "He has an apologetic smile on his face. You accept his hand and start brushing the dirt off yourself."

            return
        #~~~~

        label .flipoff:
            $dmpoints += negAnswer

            "Your face contorts into a frown as you flip off the owner of the hand in your face. He’s done enough…"

            "The hand that was in front of you withdraws. You look up and see a handsome gnome with a well-kept moustache. Even bruised and ruffled from falling off his bike, he has a very impressive demeanour."

            "He has an apologetic expression on his face. You pick yourself up off the ground and start brushing the dirt off yourself."


            return
        #~~~~~~
        label .accept:
            $dmpoints += posAnswer

            mc "It’s fine! I’ve had worse where nobody’s offered to help me back up! Thanks for sticking around."

            "You watch as he starts picking his own stuff off the ground and placing them back into the basket on his bike. You are about to ask him if he needs help when your own books starts slipping out of your hands again."

            unknown "Do you need some help with that? It’s the least I can do after knocking you over."

            return
        #~~~~
        label .glare:
            $dmpoints += negAnswer

            "You say nothing, grabbing your books from his grasp and glaring. You see his pleasant expression leave his face and watch his whole demeanour grow colder. You start inspecting your own books  while he is busy picking up his own stuff."

            "He looks over at you struggling with to balance your books with your now scratched up arms, and seems to take pity on you."

            unknown "Do you need some help with that? It’s the least I can do after knocking you over."
            return

        #~~~~
        label .accepthelp:
            $dmpoints += neutAnswer

            mc "That would be great, actually. I’m on my way to the IPRE dorm. Is that on your way?"

            dav "I’m headed there too! We can kill two birds with one stone, this way. My name’s Davenport. I’m one of the RA’s."
            return

        #~~~~
        label .ungracious:
            $dmpoints += negAnswer

            mc "I’m not really in the mood to see my stuff thrown onto the ground a second time. So no thanks."

            "The gnome takes a deep breath to regain his composure. He seems a bit on edge."

            unknown "That’s fair considering what happened. Once again, I apologize. No matter how good a bike rider I am, that does not mean I can be negligent in looking out for everyone around me."

            menu:
                "{i}Accept his apology.{/i}":
                    call .accept2
                "{i}Scoff.{/i}":
                    jump .scoff #this choice causes the scene to end early
            return


        #~~~
        label .accept2:
            $dmpoints += neutAnswer


            "You sigh. Maybe you were a bit too harsh. He didn’t mean it, and he’s genuinely apologising..."

            mc "That’s ok, man. Sorry I was such a dick, today has been weird. Being knocked over just sorta pushed me too far and I shouldn’t have lashed out. We cool?"

            "The gnome looks pleasantly surprised at your admission. You suppose that he didn’t expect you to turn around and apologise back."

            unknown "I think we’re cool. Are you sure you didn’t want any help?"

            #mc "Uh..."

            menu:
                "Still no, but thanks.":
                    jump .nah #ends scene early
                "Might as well.":
                    call .sure

            return

        #~~~~~~
        label .nah:
            $dmpoints += neutAnswer

            mc "Thanks for the offer but I do just kinda want to go and settle in."

            dav "Understandable. I’m Davenport, by the way."
            mc "I'm [mcname]."
            dav "Well, [mcname], if you’re ever in my dorm..."

            "Davenport rummages through his basket, and hands you a flyer."

            dav "The other RAs and I are having a welcome back party for people in my dorm if you would like to come. It’s just a little thing so everyone could get to know one another. It would be nice if you could make it!"

            "And with that, he props his bike back up, and give you a little wave, and hops onto his bike and pedals off."

            "You glance at the flyer. Oh. IPRE Dorm. Well, it’s a good thing you made up with him - He’s your new RA apparently."

            "You re-adjust your books in your arms and head off."

            "The rest of your walk is uneventful, you walk in the dorm entrance, finding your room once again and patting your pockets for your key."

            jump .end

        #~~~~
        label .sure:
            $dmpoints += neutAnswer
            mc "If you aren’t going out of your way, then sure."

            unknown "Don’t worry about it. Tell you what, I’m on the way to the IPRE Dorm right now. If you’re headed that way, then we can tackle two birds with one stone."

            menu:
                "That's my dorm!":
                    call .mydorm
                "{i}Roll: Deception. Crit Fail.{/i}":
                    call .fail

            #call .gracious
            return

        #~~~
        label .scoff:
            $dmpoints += negAnswer

            "You scoff at his apology."

            mc "Yeah."

            dav "Well, it’s been nice to meet you, but I do have to be going. My name is Davenport, by the way. I’m one of the RAs for the IPRE Dorm. I know we got off to a bad start but I hope we can get along with each other."

            "He dusts off his pants and hops back on his bike, nodding in your direction and pedalling away."

            jump .end




        #~~~~~~~~~
        label .gracious:


            mc "I’m alright! Thanks though. I don’t want to get in the way of your errands."

            unknown "Don’t worry about it. Tell you what, I’m on the way to the IPRE Dorm right now. If you’re headed around there, then we can tackle two birds with one stone."

            menu:
                "That's my dorm!":
                    call .mydorm
                "{i}Roll: Deception. Crit Fail.{/i}":
                    call .fail


            return

        #~~~~~~
        label .mydorm: #my dorm, my dorm, my dorm, talkin bout,,, my doooorm. my dorm! (im so sorry)
            $dmpoints += posAnswer

            mc "Actually yeah, that’s my dorm!"

            dav "Really? Then it’s not just polite, it’s my duty to help you back to the dorm! I’m one of the RAs for that building. My name is Davenport, by the way."

            mc "Oh, I remember that name! You’re the RA for the floor I’m on. I’m [mcname]. And I think I will take your help."

            "He takes half your books from you and places them nicely on top of his basket, walking the bike next to you."

            "Now that you are looking looking closely, it looks like he has stuff for a party."

            dav "I’m really sorry about running you over with your bike. That was not normal RA behavior."

            "The two of you walk in silence for a bit."

            dav "If you don’t mind me asking, what are you majoring in?"

            return

        #~~~~~
        label .fail:
            $dmpoints += negAnswer

            mc "Uh. Nope. Never heard of it. Super new here. Yep. New new new."

            "He eyes you strangely."

            dav "Ok then? I’m Davenport, the RA for the IPRE Dorm."

            menu:
                "{i}Introduce yourself.{/i}":
                    call .intro
                "{i}Be rude.{/i}":
                    call .rude

            return

        #~~~~~~
        label .intro:
            $dmpoints += posAnswer

            mc "I'm [mcname]."

            dav "Wait, [mcname]? I remember seeing that name for one of the floors I look after..."

            "He seems a bit hurt that you said you hadn’t heard of it. Why did you think that was a good idea?"

            dav "So... What’s your major?"

            return

        #~~~~
        label .rude:
            $dmpoints += negAnswer

            mc "Oh you’re an RA, huh? So you’re a snitch. I’m [mcname]. I don’t think we’ll fucking get along."

            "He holds your antagonistic glare without wavering."

            dav "I see. I remember seeing that name for one of the floors I look after. In that case."

            "Davenport hands you a flyer. You take it reluctantly, holding it gingerly with two fingers."

            dav "The other RAs and I are having a welcome back party for everyone in the dorm if you would like to come. It’s just a little thing so everyone could get to know one another."

            dav "I know you’re in a bad mood right now but would you still like to come? You might find yourself making good friends with the rest of the dorm."

            jump .party

        #~~~~~
        label .namemajor:
            $dmpoints += neutAnswer

            mc "Oh, I'm taking [mcmajor]."

            "You don’t give him much to go off of there."

            dav "Sounds cool!"

            "You nod in response and look ahead again, focusing on walking the right way."

            "Once you get to your dorm, Davenport hands you a flier."

            dav "The other RAs and I are having a welcome back party for everyone in the dorm if you would like to come. It’s just a little thing so everyone could get to know one another. Would you like to come?"


            return

        #~~~~
        label .excite:
            $dmpoints += posAnswer

            mc "Oh! I’m taking [mcmajor]. It’s super cool."

            "The two of you spend the next few minutes talking about your major before arriving at your dorm."


            "Once you get to your dorm, Davenport hands you a flier."

            dav "The other RAs and I are having a welcome back party for everyone in the dorm if you would like to come. It’s just a little thing so everyone could get to know one another. Would you like to come?"

            return

        #~~~~
        label .stupid:
            $dmpoints += negAnswer

            mc "Eh, it’s nothing that exciting. Better than something like fucking… I dunno? Botany? Illusion? Something boring and weird like that."

            "You can’t read Davenport’s expression too well, but if you didn’t know better you’d think he was deliberately keeping his expression very… Neutral."

            dav "Would you like some help getting your stuff up?"

            mc "Thanks, but no thanks! I got it."

            "Davenport hands you your textbooks back. As he does so, he also hands you a flyer."

            dav "The other RAs and I are having a welcome back party for everyone in the dorm if you would like to come. It’s just a little thing so everyone could get to know one another. Would you like to come?"

            jump .party

        #~~~~~
        label .party:

            menu:
                "{i}Enthusiastic agreement.{/i}":
                    call .enthuse
                "{i}Normal agreement.{/i}":
                    call .normal
                "{i}Not sure.{/i}":
                    call .idk
                "What is this? Fucking grade school?":
                    call .gradeschool

            "Davenport leaves you standing in the hallway as he walks off, rounding the corner and disappearing. He’s quite a guy."

            jump .end


        #~~~~~~~
        label .enthuse:
            $dmpoints += posAnswer
            mc "I’d love to!"
            call .pos
            return

        label .normal:
            $dmpoints += posAnswer
            mc "If I can make it, I’ll see you there."
            call .pos
            return

        label .idk:
            $dmpoints += neutAnswer
            mc "Hm. I don't know..."
            call .pos
            return

        label .pos:
            dav "It would be great to have you there. I'm in Room 23 if you need any help. And [mcname]?"

            "He pauses for a few moments to make sure he has your attention."

            dav "Welcome to school." #REPLACE with school name

            return

        #~~~~~
        label .gradeschool:
            $dmpoints += negAnswer

            mc "Is this fucking grade school or something? Do people really need their hand held to meet their fucking neighbors?"

            show dav strained at right

            dav "Nonetheless, it would still be great to have you there. I'm in room 23 if you need any help. And [mcname]?"

            "He pauses for a few moments to make sure he has your attention."

            dav "Welcome to school." #REPLACE with school name

            return

        #~~~~
        label .end:
            hide dav with easeoutright

            "You open your door and place your books on your desk. That is the last thing on your to-do list for the day. You jump onto your bed and sink into the comforter."

            "You’re a bit tired, even though it’s still fairly early. The sun is only just finished setting and it’s still not fully dark out yet."

            "Maybe a cat nap would do you some good before going for another walk to try to make friends."

            "You toss a blanket over yourself, not bothering to change your clothes before closing your eyes and letting your breathing slow down."

            #for debugging
            "You have %(dmpoints)d points"

            return
