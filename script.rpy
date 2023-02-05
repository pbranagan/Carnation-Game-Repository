define a = Character("Alex")
define g = Character("Ghost")
define m = Character("Mom")
define d = Character("Dad")
define p = Character("Pig")
define s = Character("Sam")
define n = Character("")
define b1 = Character("Bully 1")
define b2 = Character("Bully 2")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg foyer
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    
    n "It's September 26th, a Friday. The sun is shining despite the fall approaching."
    # These display lines of dialogue.
    
    show mom happy with dissolve
    
    
    m "Sweetie, I just wanted to talk to you for a moment. You know how much I love you, right?"
    hide mom happy with dissolve
    show alex happy with dissolve
    a "Of course, Mom. You're my favorite person in the world."
    hide alex happy with dissolve
    
    show mom happy with dissolve
    m "And you're mine. I just want you to know that no matter what happens, I'll always be here for you. No matter how far away you are, I'll always be watching over you."
    hide mom happy with dissolve
    scene bg neighborhood
    with fade
    show alex happy with dissolve
    a "Hello! Who is it?"
    hide alex happy with dissolve
    show pig unhappy with dissolve
    n "The world blurs around Alex. She hears her mother's legal name being spoken. She freezes."
    p "...I'm sorry for your loss."
    # phone ringing spound
    hide pig unhappy with dissolve

    show alex sad with dissolve
    n "Alex calls her father, unsure where to go, what to do."
    a "Dad?"
    d "I know. I know."
    a "Where are you, Dad?"
    d "I will be there soon."

    hide alex sad with dissolve 
    
    
    
    n "In the following weeks, the two are overcome with grief. Alex's father becomes a shell of himself, becoming otherwise emotionally detached."

    scene bg room 
    with fade
    show alex neutral with dissolve
    n "Staring in the mirror, Alex cannot identify the person who stares back at her."
    a "..."
    n "Alex cannot recognize themself."
    a "..."
    n "Alex cannot recognize themself."
    g "Alex?"
    n "There is a shadow at the back of the room."
    g "Alex?"
    hide alex neutral with dissolve
    show alex sad with dissolve
    a "Nobody's here. It's not real."
    g "Alex?"
    show mom ghost with dissolve
    hide mom ghost with dissolve
    show alex sad with dissolve
    a "Mom?"
    hide alex sad with dissolve
    show mom ghost with dissolve 
    "It's okay. It's okay. I'm here."
    hide mom ghost with dissolve
    show alex sad with dissolve
    a "I don't know who I am anymore, mom. I don't feel like I belong."
    hide alex sad with dissolve
    show mom ghost with dissolve
    g "It's okay be to be confused, honey."
    hide mom ghost with dissolve


    #add scary noise?
    

    scene bg highschoolhallway
    with fade
    show alex neutral with dissolve
    n "It's the first day of school, junior year. Alex forces herself to go, her father nowhere to be found. He was always working, these days."
    n "By their lockers, Alex is confronted by some girls."
    b1 "Four-eyes."
    b2 "Nice outfit, freak. I bet your mom made it for you, huh? Or your girlfriend?"
    hide alex neutral with dissolve
    show alex sad with dissolve 
    n "After they leave, Alex sits against the lockers, searching for her mother's reassurance."
    hide alex sad with dissolve
    show mom ghost with dissolve 
    g "I'm here for you, sweetie. It's okay."
    g "But I can't be here forever. We both know that."
    hide mom ghost with dissolve

    show bg skatepark
    with fade
    show alex neutral with dissolve
    n "Alex goes to the skatepark after school, seeking relief from the day."
    n "Mumbling to themself,"
    a "It feels like everything is falling apart. I don't know how long I can keep going like this."
    hide alex neutral with dissolve
    show sam neutral with dissolve
    s "Hey!"
    n "A person breaks Alex out of their thoughts."
    s "Hey!"
    hide sam neutral with dissolve
    show alex neutral with dissolve
    a "Hello?"
    hide alex neutral with dissolve
    show sam neutral with dissolve
    s "I'm Sam, I've never seen you here before. What's your deal?"
    hide sam neutral with dissolve
    show alex neutral with dissolve
    a "I don't have a deal... "
    hide alex neutral with dissolve
    show sam neutral with dissolve
    s "Okay... then why are you here?"
    hide sam neutral with dissolve
    show alex neutral with dissolve
    a "Just needed to get out, you know?"
    hide alex neutral with dissolve
    n "Sam is silent for a moment."
    show sam neutral with dissolve
    s "Do you want to hang out?"
    hide sam neutral with dissolve
    show alex neutral with dissolve
    a "What?"
    hide alex neutral with dissolve
    show sam neutral with dissolve
    s "Yeah."
    hide sam neutral with dissolve
    show alex neutral with dissolve
    a "Right now?"
    hide alex neutral with dissolve
    show sam neutral with dissolve
    s "Yeah! Right now."
    hide sam neutral with dissolve

    scene bg colorfulroom
    with fade

    show sam neutral with dissolve
    s "Are you new to the area or something?"
    hide sam neutral with dissolve
    n "The two are in Sam's room. Alex had never seen so much color before. They found themself preferring it."
    show alex neutral with dissolve
    a "No, I've lived here all my life. Just never been to the skatepark before."
    hide alex neutral with dissolve
    show sam neutral with dissolve
    s "You want to skate, or what?"
    hide sam neutral with dissolve
    show alex neutral with dissolve
    a "Something like that."
    hide alex neutral with dissolve
    show sam neutral with dissolve
    n "Sam smiles."
    s "I could teach you, if you want. I'm there all the time."
    hide sam neutral with dissolve
    show alex neutral with dissolve
    n "Alex hesitates to think about this."
    a "Maybe... I don't know."
    hide alex neutral with dissolve
    show sam neutral with dissolve
    s "Let me know, then."
    hide sam neutral with dissolve
    n "The two talk for hours--something Alex is not used to anymore, but it felt so easy with her. They wanted to keep talking with Sam."
    n "Alex tells her about their identity--how ever since then, everything is different."
    n "They immediately regret it."
    show sam neutral with dissolve
    s "Don't. Don't regret that."
    s "Why is it different?"
    hide sam neutral with dissolve
    show alex neutral with dissolve
    a "You know why."
    hide alex neutral with dissolve
    n "Both of them fall silent, looking at each other."

    scene bg graveyard 
    with fade
    n "There was a funeral for Alex's mother. They couldn't bring themself to go, not at the time."
    n "They find themself standing in the graveyard, staring at their mother's gravestone."
    show alex sad with dissolve
    a "I brought you your favorite flowers, Mom."
    a "Carnations. Funny how they symbolize love and grief."
    a "I can't keep holding onto your ghost, Mom."
    a "I know you told me that. I didn't accept it then. I don't know if I fully accept it now."
    hide alex sad with dissolve
    show alex neutral with dissolve
    a "But I will keep trying."
    a "I love you."

    

    



    # This ends the game.

    return
