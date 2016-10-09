# Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can escape into an escape pod to the planet below.
# The game will be more like a Zork or Adventure type game with text outputs and funny ways to die.
# The game will involve an engine that runs a map full of rooms or scenes.
# Each room will print prints its own decription when the player enters it and then tell the engine what room to run next out of the map

# Scenes:
# Death: This is when the player dies and show be something funny
# Central Corridor: This is the starting point and has a Gothon already standing there, which the player has to defeat with a joke before continuing.
# Laser Weapon Armory: This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod. It has a keypad he has to guess the number for.
# The Bridge: Another battle scene with a Gothon where the hero places the bomb.
# Escape Pod: Where the hero escapes but only after guessing the right escape pod.


# Noun List:
# Player
# Ship
# Scene
# Gothon
# Escape Pod
# Map
# Engine
# Death
# Central Corridor
# Laser Weapon Armory
# The Bridge


# Hierarchy:
# Map
# Engine
# Scene
## Death
## Central Corridor
## Laser Weapon Armory
## The Bridge
## The Escape Pod

from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene isn't configured. Subclass it and implement enter()"
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n----------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

        quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud....if you were smarter",
            "Such a l0zr.",
            "I have a small puppy that's better at this"
        ]

        def enter(self):
            print "YOU'RE DEAD\n"
            print Death.quips[randint(0, len(self.quips)-1)]
            exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed\n" \
              "your entire crew. You are the last surviving member and your last\n" \
              "mission is to get the neutron destruct bomb from the Weapons Armory,\n" \
              "put it in the birdge, and blow the ship up after getting into an \n" \
              "escape pod.\n" \
              "\n" \
              "You're running down the central corridor to the Weapons Armory when\n" \
              "a Gothon jumps out, red scaly skin, dark grimy teeth, and a clown costume\n" \
              "flowing around his hate filled body. He's blocking the door to the\n" \
              "Armory and about to pull a weapon to blast you.\n"

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon.\n" \
                  "His clown costume is flowing and moving around his body, which throws\n" \
                  "off your aim. YOur laser hits his costume but misses him entirely. This\n" \
                  "completely ruins his brand new costume his mother bought him, which\n" \
                  "makes him fly into a rage and blast you repeatedly in the face until\n" \
                  "you are dead. Then he eats you.\n"
            return 'death'

        elif action == "dodge!":
            print "Your foot slips attempting to dodge.\n" \
                  "You slam your head on the wall, knocking you out.\n" \
                  "As soon as you wake up you get stomped by the Gothon and he eats you.\n"
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy. \n" \
                  "You tell the one Gothon joke you know " \
                  "The Gothon stops, tries not to laugh, then busts out laughing and cant move.\n" \
                  "While he's laughing you run up and shoot him square in the head \n" \
                  "putting him down, then jump through the Weapon Armory door.\n"
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE\n"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room \n" \
              "for more Gothons that might be hiding. It's dead quiet, too quiet. \n" \
              "You stand up and run to the far side of the room and find the \n" \
              "neutron bomb in its container. There's a keypad lock on the box \n" \
              "and you need the code to get the bomb out. If you get the code \n" \
              "wrong 10 times then the lock closes forever and you can't \n" \
              "get the bomb. The code is 3 digits.\n"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZZED!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out.\n" \
                  "You grab the neutron bomb and run as fast as you can to the \n" \
                  "bridge where you must place it in the right spot.\n"
            return 'the_bridge'

        else:
            print "The lock buzzes one last time and then you hear a sickening \n" \
                  "melting sound as the mechanism is fused together. \n" \
                  "You decide to sit there, and finally the Gothons blow up the \n" \
                  "ship from their ship and you die.\n"
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print "You bust onto the Bridge with the neutron destruct bomb \n" \
              "under your arm and surprise 5 gothons who are trying to \n" \
              "take control of the ship. Each of them has an even uglier \n" \
              "clown costume than the last. They haven't pulled their \n" \
              "weapons out yet, as they see the active bomb under your \n" \
              "arm and don't want to set it off.\n"

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons \n" \
                  "and make a leap for the door. right as you drop it a \n" \
                  "Gothon shoots you right in the back killing you. \n" \
                  "As you die you see another Gothon frantically try to disarm \n" \
                  "the bomb. You die knowing they will probably blow up when \n" \
                  "it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm " \
                  "and the Gothons put their hands up and start to sweat. " \
                  "You inch bakward to the door, open it, and then carefully " \
                  "place the bomb on the floor, pointing your blaster at it. " \
                  "You then jump back through the door, punch the close button " \
                  "and blast the lock so the Gothons can't get out. " \
                  "Now that the bomb is place you run to the escape pod to " \
                  "get off this tin can."
            return 'escape_pod'

        else:
            print "DOES NOT COMPUTE\n"
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to \n" \
              "the escape pod before the whole ship explodes. It seems like \n" \
              "hardly any Gothons are on the ship, so your run is clear of \n" \
              "interference. You get to the chamber with the escape pods, and \n" \
              "now need to pick one to take. Some of them could be damaged \n" \
              "but you don't have time to look. There's 5 pods, which one \n" \
              "do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button. \n" % guess
            print "The pod escapes out into the void of space, then \n" \
                  "implodes as the hull ruptures, crushing your body \n" \
                  "into jam jelly.\n"
            return 'death'

        else:
            print "You jump into pod %s and hit the eject button. \n" % guess
            print "The pod easily slides out into space heading to \n" \
                  "the planet below. As it flies to the planet, you look \n" \
                  "back and see your ship implode then explode like a \n" \
                  "bright star, taking out the Gothon ship at the same \n" \
                  "time. You've won!"

            return 'finished'



class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }


    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()