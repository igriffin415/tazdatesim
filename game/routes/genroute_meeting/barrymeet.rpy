label barrymeet:
    $knowBarryName = True;

label .meet:
    python:
            bmpoints = 0
            posAnswer = 3
            neutAnswer = 0
            negAnswer = -3

    scene bg college with dissolve

    "Ah shit. It’s getting pretty late already. You pull up your email and take a screenshot of your textbook list. Hopefully they’ll have what you need in stock today, but you doubt it. Worst case scenario you just put them on order and wait a week."

    scene bg bookstore with dissolve

    "Finding the bookstore takes a fair amount of wandering around. The signs aren’t helpful in the slightest, but soon enough you make your way up to Miller Hall, the STEM wing of the school, and walk through the door."
    "You almost missed the smell of vacuum sealed books, if you’re being honest. The clerks at the register have fairly long lineups, so you take a number and wander the aisles a bit, looking at the supplies for different majors."
    "Why do architecture students need 12 different kinds of rulers?"
    "A loud THUMP a few aisles over catches your attention, and you meander over to peek at what happened."
    "You see..."

    show barry neutral at right with moveinright

    "A guy struggling."
    "As a senior you’ve had your fair share of heavy semester with a ton of textbooks, but this guy has about triple compared to the most you have ever had to buy, and to make matters worse, he’s trying to stuff all these books into a single blue jansport."
    "It’s a little bit intimidating, and makes your wallet hurt."
    "You’re also curious, to say the least."

    menu:
        "Approach Him":
            jump .approach
        "You have better things to do":
            $knowBarryName = False
            $bmpoints += negAnswer
            "He’s probably just another poor freshman trying to take on too much. Good luck, bud. See you in library hell during Finals."
            jump .leave
label .approach:
    $bmpoints += posAnswer
    "You walk up to the guy and shift on your feet for a moment. You have to say something otherwise you’re just watching this guy to struggle. And that’s just weird."
    menu:
        "Hey":
            jump .hey
        "Do you need help?":
            jump .needHelp
        "Sup fresh-meat":
            jump .freshMeat

label .hey:
    $bmpoints += neutAnswer
    mc "Uh, hey. Books, huh?"
    "The guy looks up at you kinda like he barely heard you, which is fair, you didn’t really speak too loud."
    unknown "Uh, yeah, these are books."
    mc "Cool, uh."
    "Ah, maybe should say something less excruciatingly awkward."
    menu:
        "Do you need help?":
            jump .needHelp
        "Sup fresh-meat":
            jump .freshMeat

label .needHelp:
    $bmpoints += posAnswer
    mc "Do you need a hand? I have two."
    unknown "Ah, um, sure. Could you hold these?"
    mc "Yeah, I got you. I think I might have a bag or something."
    unknown "God, thank you. Uh, you just carry around a bag?"
    mc "If you don’t need my bag then…"
    unknown "Nevermind, nevermind, thank you."
    "He thrusts stack of books in your direction without looking and you just barely manage to grab a hold on it before he goes right back to trying to shove the mountain into his bag."
    "You pull out one of the reusable bags you brought with you - for your own books, you might add - and start to help him out."
    "You glance at him a few times between your own game of book-tetris. He’s weirdly intense about getting those books put away. You motion for him to hand you a few more, and, as he does, you try to make conversation."
    mc "I’m curious--why all the books? I’m a senior and my book list isn’t this bad."
    unknown "Some of them are for my friends because they never bother to buy even the required course packs."
    "That seems... too generous. "
    unknown "Then they owe me. "
    "Ah, that’s a college student alright."
    "With the last book tucked away and the Jansport haphazardly closed, the guy huffs a bit, and stands. You hand him the canvas bag and he gives you a curt smile in return."
    "The guy seems to have recovered somewhat from stuffing his books into his backpack, but still looks decently flustered as he looks around. Is he lost? Do you still need to help him?"
    "His phone buzzes and he jumps, startled and nearly dropping his Organic Necromancy book that must have cost more than two of your paychecks."
    "He flips it open - A FLIP PHONE?? What century is this guy living in? - And scans the screen for a moment before meeting your eyes."
    unknown "Shit. Uh, I gotta go. See you in class?"

    menu:
        "Uh, yeah, see you later.":
            call .seeyou
        "No, you won’t.":
            call .nowont

    "But wait..?"
    mc "How do you know that we have a class together?"
    "He laughs."
    unknown "I’m in most classes. If you ever need anything, I’ve also taken most of the classes here. Just hit me up. Or one of the twins, they’ll point you my way."
    mc "The twins?"
    "You’ve only met one pair of twins today but like? Did he mean them? Another set of twins? You aren’t a Divination Wizard or anything."
    "He throws up a peace sign in response to your confusion."
    unknown "If you don’t know the twins yet, I don’t believe you’re actually a senior here."
    mc "I am, but whatever."
    unknown "Of course you are. Thanks for helping me with the books."
    mc "It was no problem."
    mc " You got a name, or do you want me to call you book boy?"
    barry "Oh shit I forgot. My name’s Barry, and yours is…?"
    mc "It's [mcname]."
    barry "[mcname], I’ll see you around."
    "Barry just… leaves without saying another word. You didn’t even get his last name and who knows how many Barry’s there are at this university."
    "You’d probably be able to find him pretty easily just based off what you’ve seen of him. Memorable guy to say the least."
    "You still don’t really believe that he’s in your classes, but you guess when things start up you’ll see if he’s telling the truth or not."
    "You do kinda wanna see more of him."
    jump .leave


label .seeyou:
    mc "Yeah, see you later."
    return
label .nowont:
    mc "No, you probably won’t."
    unknown "No, you will."
    return


label .freshMeat:
    $bmpoints += negAnswer
    "He glances up at you weird a strange expression on his face before quietly saying"
    unknown "God, I wish I was a freshman."
    "Wait, really? He’s buying a billion books, some of which you know you can find online, because you have those PDFs already."
    mc "You’re not?"
    unknown " Considering I’m taking three capstone courses, no. I’m a senior."
    mc "Oh same. Why are you buying all your books then. That’s usually a big red flag for “never been to college before.”"
    unknown "Well for one, working with real books is easier. I already work with two screens I don’t need a third just for a reference book."
    "He goes back to his book-tetris, and you stand there awkwardly before deciding if you should try to salvage what's left of… This."
    menu:
        "Just go. Save yourself":
            jump .justgo
        "Try to make conversation":
            jump .converse

label .converse:
    mc "I’m curious--why all the books?"
    unknown "Some of them are for my friends because they never bother to buy even the required course packs."
    "That seems... too generous. "
    unknown "Then they owe me. "
    "Ah, that’s a college student alright."
    "His phone buzzes and he looks down, nearly dropping his Organic Necromancy book that must have cost more than two of your paychecks."
    unknown "Shit. Uh, I gotta go. See you in class?"

    menu:
        "Uh, yeah, see you later.":
            call .seeyou
        "No, you won’t.":
            call .nowont

    "But wait..?"
    mc "How do you know that we have a class together?"
    "He laughs."
    unknown "I’m in most classes. If you ever need anything, I’ve also taken most of the classes here. Just hit me up. Or one of the twins, they’ll point you my way."
    mc "The twins?"
    "You’ve only met one pair of twins today but like? Did he mean them? Another set of twins? You aren’t a Divination Wizard or anything."
    "He throws up a peace sign in response to your confusion."
    unknown "If you don’t know the twins yet, I don’t believe you’re actually a senior here."
    mc "{i}I am.{i}"
    unknown "Of course you are."
    mc " You got a name, or do you want me to call you book boy?"
    barry "Oh shit I forgot. My name’s Barry, and yours is…?"
    mc "It's [mcname]."
    barry "[mcname], I’ll see you around."
    "Barry just… leaves without saying another word. You didn’t even get his last name and who knows how many Barry’s there are at this university."
    "… Probably not many. He seems pretty wierd."
    "You still don’t really believe him that he’s a senior or that he’s in your classes, but you guess when things start up you’ll see if he’s telling the truth or not."
    jump .leave

label .justgo:
    $knowBarryName = False
    mc "I gotta go, I think my number is about to be called."
    unknown "Ok. Bye?"
    "You scurry away awkwardly and avoid looking in that direction the whole time you’re in line for your books."
    jump .leave

label .leave:
    "You heard your number finally get called and you walk up to the front of the line, eager to get your books and be on your way."
    "They didn’t have all your books - You don’t even need the reusable bags you brought with you - So you just carry them in your arms and wish the clerk a good day before finding your way out of the maze of hallways and get to your dorm."
