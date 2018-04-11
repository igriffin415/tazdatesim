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
    "You almost missed the smell of vacuum sealed books, if you’re being honest. The clerks at the register have fairly long lineups, so you take a number and wander the aisles a bit, looking at the supplies for different majors. Why do architecture students need 12 different kinds of rulers?"
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
            jump .leave
label .approach:
    $bmpoints += posAnswer
    "You walk up to the guy and shift on your feet for a moment. You have to say something otherwise you’re just watching this guy to struggle. And that’s just weird."
    jump .leave














label .leave:
    "You heard your number finally get called and you walk up to the front of the line, eager to get your books and be on your way."
    "They didn’t have all your books - You don’t even need the reusable bags you brought with you - So you just carry them in your arms and wish the clerk a good day before finding your way out of the maze of hallways and get to your dorm."
