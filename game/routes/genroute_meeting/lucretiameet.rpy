label lucretiameet:
    
label .meet:
    python:
            points = 0
            posAnswer = 3
            neutAnswer = 0
            negAnswer = -3
    
    #bg library 
    
    "Lost in your thoughts, you don’t even notice the figure coming towards you until it’s too late."
    
    show lucretia neutral at right
    
    unknown "Oof!"
    
    "You look over a pile of books to see a woman clutching at her nose."
    menu:
        
        "Apologize profusely":
            jump apologize
        "Blame her":
            jump blame
            
    label apologize:
        mcname "I'm so sorry! I wasn't looking where I was going and ran right into you!"
        
        "Color fills her cheeks and she lifts her hand away from her nose. Thank god, there doesn't seem to be any blood?"
        
        unknown "I'm the one who should apologize. I couldn't see over my books and that's my fault"
        jump bothResponse
        
    label blame:
        mcname "Watch where you're going!"
        
        unknown "I  couldn't see over all my books and that's my fault. I'm sorry."
        jump bothResponse
        
    label bothResponse:
        menu:
            
            "Ask if she's alright":
                jump askIfAlright
            "Accept her apology":
                jump acceptApology
                
    label acceptApology:
        mcname "You should be sorry."
        
        "Her eyes darken even as the flush on her cheeks deepen."
        
        unknown "Of course. I wish you a good day."
        
        "She bows her head and starts gathering up her books."
        
        menu:
            
            "Help her":
                jump attemptHelp
                
            "Leave":
                jump leave
                
        label attemptHelp:
            "You reach down to pick up one of the many books scattered across the walkway."
            
            "Her hand snaps out and grabs the book out from under your hand."
            
            unknown "I'm sure you have important places to be going. I wouldn't want to cause you any dely."
            
            menu:
                
                "Leave":
                    jump leave
                    
            label leave:
                "You nod, step lightly over the books, and continue towards the buildings before you."
                
                hide lucretia neutral
                
                "You probably don’t want to meet up with that book lady again, so you ought to change your destination. Instead, you wander into Roost Hall. The place seems interesting; lots of people are walking in and out."
                
                "The hall is well lit and warm, decorated with a variety of wood, metal and stone art pieces. There are quite a few people bustling up and down the corridor, entering rooms that are alive with laughter and creation." 
                
                "The building seems to be home to a variety of trades, from the signs: metalworking, carpentry, electrics...the list goes on."
                
                "As you look around, a sudden buzzing catches your attention. Curiosity gets the better of you as you gently push open the classroom door." 
                
                jump magnusmeet.meet
                
            label askIfAlright:
                mcname "Is your nose okay?"
                
                "She looks down at her hands to check for a moment before looking back up to you."
                
                unknown "I'm fine. Just a little startled is all."
                
                "You look down at the books scattered across the walkway and read a few titles: “Jellyfish Blooms: Ecological and Societal Importance”, “Abjuration Theory in Extraplanar Application”, “Cnidaria: Ecology, Distribution Patterns, and Interactions”, “Qing Architecture”."
                
                unknown "I'll... pick these up."
                
                menu:
                    "Offer to help":
                        jump offerHelp
                    "Say goodbye and keep going":
                        jump sayGoodbye
                        
            label sayGoodbye:
                mcname "Maybe I'll see you around campus." 
                
                "She looks up from the hanful of books she's collected already and gives you a polite smile."
                
                unknown "Maybe you will."
                
                hide lucretia neutral
                
                "You step around the remaining books and head forward. You’re sure she’s heading to the library next and that would be an awkward encounter for sure. You should probably change your destination."
                
                "You wander into roost hall. The place seems interesting; lots of people are walking in and out."
                
                "The hall is well lit and warm, decorated with a variety of wood, metal and stone art pieces. There are quite a few people bustling up and down the corridor, entering rooms that are alive with laughter and creation. The building seems to be home to a variety of trades, from the signs: metalworking, carpentry, electrics...the list goes on."
                
                "As you look around, a sudden buzzing catched your attention. Curiosity gets the better of you as you gently push open the classroom door." 
                
                jump magnusmeet.meet
                
            label offerHelp:
                mcname "Please, let me help you with those!"
                
                unknown "Oh no! It's fine, really. You go ahead and keep going. I'm sure you have important places to be."
                
                menu:
                    "Insist":
                        jump insistHelp
                    "Politely leave":
                        jump sayGoodbye
            
            label insistHelp:
                mcname "I was heading towards the library anyway. It would be no trouble at all."
                
                "She stares at you a moment before ducking her head."
                
                unknown "Alright. I could use a hand."
                
                "With two people it’s easy, despite the fact that there are so many books. How was she even able to carry this many on her own? You can barely fit your chin over the stack in your hands. Maybe you should ask her."
                
                "Except, when you open your mouth to get her attention, you realize you don’t even know her name. Chagrined at your lack of manners, you consider your options."
                
                menu:
                    "Ask for her name":
                        jump askName
                    "Introduce yourself":
                        jump introduceSelf
                    "Say nothing and wallow in your mistakes":
                        jump sayNothing
            label askName:
                mcname "Excuse me, but I didn't catch your name."
                
                unknown "It's Lucretia. I would shake your hand but I don't exactly want to pick up these books again."
                
                "You laugh and she gives you a polite smile."
                
                lucretia "And yours?"
                
                mcname "I go by [mcname]."
                
                "The two of you walk side by side in companionable silence, making sure to watch your surroundings and not trip up the stairs."
                
                "In unspoken accord, you each push a shoulder against one of the carved oak double doors and push them open."
                
                jump unite
                
            label introduceSelf:
                mcname "By the way, my name is [mcname]."
                
                unknown "Nice to meet you, [mcname]. I apologize for my poor manners! My name is Lucretia."
                
                "You pick up the last of the books before the two of you walk toward the library."
                
                "Lucretia steps ahead and pushes one of the double-doors open with her shoulder for you to follow through behind. You let your gaze wander around the room as you walk toward return slot."
                
                jump unite
            
            label sayNothing:
                "The two of you pick up the last couple books before walking toward the library in awkward silence."
                
                "As you approach the double-doors of the library she glances over at you."
                
                unknown "My name's Lucretia, by the way."
                
                "You almost trip on thin air but luckily recover before you do anything stupid. Or, at least, any more stupid than what you’ve done already."
                
                mcname "My name's [mcname]."
                
                lucretia "Glad to make your acquaintance, [mcname]."
                
                "She easily pushes one of the oak doors open with her shoulder and you walk into the library behind her, gaze wandering around the room."
            
            label unite:
                "It's a beautiful sight."
                
                "Shelves rise up high into the air, decorated sliding ladders acting as the only way to reach some of the higher ones. Sunlight filters in from skylights on the ceiling. There are alcoves hidden in the curves of the walls with elegant carving curling all along the arch of their openings."
                
                "Lucretia nudges your arm, dragging you back to the present."
                
                "You help her put the books in the return slot."


