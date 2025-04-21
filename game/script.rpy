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

init python:
    from suspects import SuspectManager
    persistent.suspect_manager = SuspectManager()


# The game starts here.
label start:

    # logique métier à exécuter à chaque nouvelle partie
    $ persistent.suspect_manager.generate_suspects(number_of_suspects)

    # Text 
    "Welcome to the game."
    $ persistent.player_name = renpy.input("Please enter your name:") or "Player"

    # affiche
    scene bg office
    show boss serious

    boss "Hello, Agent [persistent.player_name]."
    boss "There was a murder in a school. That will be your first case to solve."
    boss "Are you ready?"

    scene bg police 1 
    show boss serious
    with fade

    boss "We managed to capture all [number_of_suspects] suspects. Here they are:"
    show boss serious at left

    python:
        for suspect in persistent.suspect_manager.get_suspects():
            renpy.show(suspect.getPicture("sad"), at_list=[Position(xalign=0.5, yalign=1.0)])
            renpy.say(boss, str(suspect))
            renpy.hide(suspect.getPicture("sad"))     

    boss "Also your name is still [persistent.player_name]"

    jump guess_culprit

    # This code is not executed
    "Game will exit NOW"
    return

label guess_culprit:

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
        #textbutton str(suspect) action [SetVariable("chosen_suspect", str(suspect))] xalign 0.5 yalign 0.5

    boss "J'arrive pas à faire des boutons avec leurs noms :("
    boss "adios"

    return