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
        mcname "I'm so sorry! I wasn't looking where /i was going and ran right into you!"
        
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
                
                "You probably don’t want to meet up with that book lady again, so you ought to change your destination. Instead, you wander into Roost Hall. The place seems interesting; lots of people are walking in and out."
                
                "The hall is well lit and warm, decorated with a variety of wood, metal and stone art pieces. There are quite a few people bustling up and down the corridor, entering rooms that are alive with laughter and creation." 
                
                "The building seems to be home to a variety of trades, from the signs: metalworking, carpentry, electrics...the list goes on."
                
                "As you look around, a sudden buzzing catches your attention. Curiosity gets the better of you as you gently push open the classroom door." 
                
                return #replace with magnus's meeting tag
                
            label askIfAlright:
                "good end." #to be replaced with good end
                
                return
