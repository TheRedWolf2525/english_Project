# Redéfinit le comportement de fade par défaut.
define fade = Fade(0.5, 0.2, 0.5)

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define boss = Character("Boss", color="#9f2525")

############################### logique métier ###############################

define number_of_suspects = 5

# Ces valeurs seront conservées d'une partie à l'autre.
# Elles doivent être initialisées pour supprimer un warning, mais elles peuvent
# être ré-écrites plus tard.
default persistent.player_name = None
default persistent.suspect_manager = None
default persistent.killer_id = None
default persistent.clues = None

init python:
    from suspects import SuspectManager
    persistent.suspect_manager = SuspectManager()
    from request_util import request_from_gemini


# The game starts here.
label start:

    # logique métier à exécuter à chaque nouvelle partie
    $ persistent.killer_id = persistent.suspect_manager.generate_valid_suspects()
    $ persistent.clues = persistent.suspect_manager.find_unique_signature_combination(persistent.killer_id)
            

    # Text 
    "Welcome to the game."
    $ persistent.player_name = renpy.input("Please enter your name:") or "Lestrade"

    # affiche
    scene bg office
    show boss serious

    boss "Hello, Officer [persistent.player_name]."
    boss "A murder occured in a nearby school. Mr Koro, a teacher that worked there, was found dead."

    # show image du mort

    

    boss "That will be your first case to solve."
    boss "Are you ready?"

    scene bg police 1 
    show boss serious
    with fade

    boss "We just recived a list of clues from the crime scene."
    boss "Sadly, as always, it seems that writing a good report is too much to ask..."
    boss "Here is all I've got :"

    python:
        for key in persistent.clues:
            val = persistent.suspect_manager.get_suspect_by_id(persistent.killer_id).get_attributes()[key]
            renpy.say(boss, key+" : "+str(val))

    boss "We managed to capture all [number_of_suspects] suspects. Here they are:"
    show boss serious at left

    python:
        for suspect in persistent.suspect_manager.get_suspects():
            renpy.show(suspect.getPicture("sad"), at_list=[Position(xalign=0.5, yalign=1.0)])
            renpy.say(boss, str(suspect))
            renpy.hide(suspect.getPicture("sad"))     

    show boss serious at center 
    boss "You have to find out who killed Mr Koro."

    jump choose_dialogue
    
    # jump guess_culprit

    # This code is not executed
    "Game will exit NOW"

    return

label give_hints:
    boss "We just recived a list of clues from the crime scene."
    boss "Sadly, as always, it seems that writing a good report is too much to ask..."
    boss "Here is all I've got :"

    python:
        for key in persistent.clues:
            val = persistent.suspect_manager.get_suspect_by_id(persistent.killer_id).get_attributes()[key]
            renpy.say(boss, key+" : "+str(val))
    
    boss "Now it's your turn"
    jump choose_dialogue

# Allows selection of the next person that will be interrogated.
label choose_dialogue:
    scene bg police 2
    
    python:
        for suspect_id in range(number_of_suspects):
            suspect = persistent.suspect_manager.get_suspect_by_id(suspect_id)
            renpy.show_screen("button_interrogate_suspect_" + str(suspect_id), suspect.getName(), 0.1 + 0.2*suspect_id, 0.5)

    show screen button_guess_culprit
    show screen button_ask_hints
    
    "Who do you want to interrogate next?"
    


screen button_interrogate_suspect_0(Texte, x, y):
    frame:
        background "#444444"
        padding (10, 10)
        xalign x yalign y
        textbutton [Texte] action Call("interrogate_suspect", 0)

screen button_interrogate_suspect_1(Texte, x, y):
    frame:
        background "#444444"
        padding (10, 10)
        xalign x yalign y
        textbutton [Texte] action Call("interrogate_suspect", 1)

screen button_interrogate_suspect_2(Texte, x, y):
    frame:
        background "#444444"
        padding (10, 10)
        xalign x yalign y
        textbutton [Texte] action Call("interrogate_suspect", 2)

screen button_interrogate_suspect_3(Texte, x, y):
    frame:
        background "#444444"
        padding (10, 10)
        xalign x yalign y
        textbutton [Texte] action Call("interrogate_suspect", 3)

screen button_interrogate_suspect_4(Texte, x, y):
    frame:
        background "#444444"
        padding (10, 10)
        xalign x yalign y
        textbutton [Texte] action Call("interrogate_suspect", 4)

screen button_guess_culprit:
    frame:
        background "#444444"
        padding (10, 10)
        xalign 0.3 yalign 0.7
        textbutton "Guess the culprit" action Jump("guess_culprit")

screen button_ask_hints:
    frame:
        background "#444444"
        padding (10, 10)
        xalign 0.7 yalign 0.7
        textbutton "Ask for hints" action Jump("give_hints")

label interrogate_suspect(suspect_id):
    hide screen button_interrogate_suspect_0
    hide screen button_interrogate_suspect_1
    hide screen button_interrogate_suspect_2
    hide screen button_interrogate_suspect_3
    hide screen button_interrogate_suspect_4
    hide screen button_guess_culprit
    hide screen button_ask_hints
    
    ## faut poser la question au bon suspect
    while True:
        $ question = renpy.input("Write here:") or ""
        $ persistent.suspect_manager.get_suspect_by_id(suspect_id).add_entry(question)
        $ answer = request_from_gemini("Maggie Mag", persistent.suspect_manager.get_suspect_by_id(suspect_id).coop, ["you were at home last night"], question, persistent.suspect_manager.get_suspect_by_id(suspect_id).exchanges)
        $ persistent.suspect_manager.get_suspect_by_id(suspect_id).add_entry(answer)
        "Maggie: [answer]"


screen button_guess_suspect_0(Texte, x, y):
    frame:
        background "#444444"
        padding (10, 10)
        xalign x yalign y
        textbutton [Texte] action Call("guessed", 0)

screen button_guess_suspect_1(Texte, x, y):
    frame:
        background "#444444"
        padding (10, 10)
        xalign x yalign y
        textbutton [Texte] action Call("guessed", 1)

screen button_guess_suspect_2(Texte, x, y):
    frame:
        background "#444444"
        padding (10, 10)
        xalign x yalign y
        textbutton [Texte] action Call("guessed", 2)

screen button_guess_suspect_3(Texte, x, y):
    frame:
        background "#444444"
        padding (10, 10)
        xalign x yalign y
        textbutton [Texte] action Call("guessed", 3)

screen button_guess_suspect_4(Texte, x, y):
    frame:
        background "#444444"
        padding (10, 10)
        xalign x yalign y
        textbutton [Texte] action Call("guessed", 4)


# scene where the player tries to guess the culprit
label guess_culprit:

    hide screen button_interrogate_suspect_0
    hide screen button_interrogate_suspect_1
    hide screen button_interrogate_suspect_2
    hide screen button_interrogate_suspect_3
    hide screen button_interrogate_suspect_4
    hide screen button_guess_culprit
    hide screen button_ask_hints


    scene office
    show boss serious
    with fade

    boss "So, [persistent.player_name], you think you have enough data to 
    try and guess who commited the crime?"

    boss "Well, who was it?"

    python:
        suspects = persistent.suspect_manager.get_suspects()
    
    python:
        for suspect in suspects:
            renpy.say(boss, suspect.getName()+"?")
            renpy.show_screen("button_guess_suspect_" + str(suspect.id), suspect.getName(), 0.1 + 0.2*suspect.id, 0.5)

    boss "You should click on the name of the person you think is the killer."

    return

label guessed(suspect_id):
    hide screen button_guess_suspect_0
    hide screen button_guess_suspect_1
    hide screen button_guess_suspect_2
    hide screen button_guess_suspect_3
    hide screen button_guess_suspect_4

    "You guessed [persistent.suspect_manager.get_suspect_by_id(suspect_id).getName()]?"
    "You are sure? Let's see..."

    python:
        if suspect_id == persistent.killer_id:
            renpy.say(boss, "You guessed it right!")
        else:
            renpy.say(boss, "You guessed it wrong!")
            renpy.say(boss, "The killer was [persistent.suspect_manager.get_suspect_by_id(persistent.killer_id).getName()]")

    return