label barrymeet:
    $knowBarryName = False;

label .meet:
        python:
            bmpoints = 0
            posAnswer = 3
            neutAnswer = 0
            negAnswer = -3

        scene bg bookstore with dissolve
        "Ah shit. It’s getting pretty late already. You pull up your email and take a screenshot of your textbook list. Hopefully they’ll have what you need in stock today, but you doubt it. Worst case scenario you just put them on order and wait a week."
        "Finding the bookstore takes a fair amount of wandering around. The signs aren’t helpful in the slightest, but soon enough you make your way up to Miller Hall, the STEM wing of the school, and walk through the door."

        jump barrymeet.end

label .end:
    return
