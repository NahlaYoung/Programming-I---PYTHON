#import random for rolling stats
import random
#I started with the superclass bacause it made sense
#contains basic attributes included in all races
class Humanoids:
    def __init__(self, height, weight, hair, eye, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.height = height
        self.weight = weight
        self.hair = hair
        self.eye = eye
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

def characterCreation():
    #welcoming
    print("Hello! Welcome to my RPG simulator. There are three races available to play:")
    print("1. Human  2. Elf  3. Dwarf")
    print("Please enter the NUMBER of the race you would like.")
    #asking user for multiple inputs
    race_choice = int(input("Which race would you like to play?: "))
    height = int(input("Enter a height for your character from 3ft - 7ft: "))
    weight = int(input("Enter a weight for your character from 60 - 300lbs: "))
    hair = str(input("Pick a hair color from these choices: white, silver, gray, black, brown, green, blue, yellow, pink, red, blonde: ")).lower()
    eye = str(input("Pick an eye color from these choices: white, black, red, green, blue, brown, purple, amber: ")).lower()
    #random rolling stats from 1-18
    strength = random.randint(1, 18)
    dexterity = random.randint(1, 18)
    constitution = random.randint(1, 18)
    intelligence = random.randint(1, 18)
    wisdom = random.randint(1, 18)
    charisma = random.randint(1, 18)

    return race_choice, height, weight, hair, eye, strength, dexterity, constitution, charisma, wisdom, intelligence


#subclass huma with specified instruction for race
class Human(Humanoids):
    def human(self,strength, dexterity, constitution, intelligence, wisdom, charisma):
        print("As a Human you are able to add 2 points to a skill of your choice.")
        plustwo_choice = input("Pick a skill: ").lower() #i converted input to lower because even i don't use capital letters and i thought it would be obviously easier
        bold_skill = False #I had to use this to track when the user selected a skill
        #without it, the color and bold would not show in the final attributes 
        if plustwo_choice == "strength":
            strength += 2
            bold_skill = True
            print(f"\033[1m\u001b[35mStrength: {strength} pts\033[0m")
            #added this to make the chosen skill bold
            #i had to research how to do this
            #I used the explaniation from replit.com on ANSI 
            #It is bold and magenta
            #this is to rest color to default
        elif plustwo_choice == "dexterity":
            dexterity += 2
            bold_skill = True
            print(f"\033[1m\u001b[35mDexterity: {dexterity} pts\033[0m")

        elif plustwo_choice == "constitution":
            constitution += 2
            bold_skill = True
            print(f"\033[1m\u001b[35mConstitution: {constitution} pts\033[0m")

        elif plustwo_choice == "intelligence":
            intelligence += 2
            bold_skill = True
            print(f"\033[1m\u001b[35mIntelligence: {intelligence} pts\033[0m")

        elif plustwo_choice == "wisdom":
            wisdom += 2
            bold_skill = True
            print(f"\033[1m\u001b[35mWisdom: {wisdom} pts\033[0m")

        elif plustwo_choice == "charisma":
            charisma += 2
            bold_skill = True
            print(f"\033[1m\u001b[35mCharisma: {charisma} pts\033[0m")
        
        return strength, dexterity, constitution, intelligence, wisdom, charisma


#subclass elves with speciifed instruction for race
class Elves(Humanoids):
    def elves(self,dexterity, charisma):
        print(f'As an Elf, you now have 100% resitance to sleep and have added 2 points to thier Dexterity and Charisma.')
        dexterity = dexterity+2 #adding two ints to dexterity
        charisma = charisma+2 #adding two points to charisma
         #i added this here because without it sleep wasn't bright blue. I have no idea what this does
        return dexterity, charisma


#subclass dwarves with with specified instruction for race
class Dwarves(Humanoids):
    def dwarves(self,strength, constitution, charisma):
        print(f'As a Dwarf, you now have 20% resitance to magic and have 2 points added to Strength and Constitution. Though we have subtracted 2 points from Charisma.')
        strength = strength+2 #adding two points to strength
        constitution = constitution+2 #adding two points
        charisma = charisma-2 #subtracting two points
        return strength, constitution, charisma

def main():
    #I knew i had to refrence the attriubtes I was going to use throughout this function
    #I tried to do it the opposite direction and i got an error.
    race_choice, height, weight, hair, eye, strength, dexterity, constitution, charisma, wisdom, intelligence = characterCreation()
    print("Your character has the following attributes:")
    print(f"Height:{height} ft")
    print(f"Weight:{weight} lbs")
    print(f"Hair Color:{hair}")
    print(f"Eye Color:{eye}")
    print(f"Strength:{strength} pts")
    print(f"Dexterity:{dexterity} pts")
    print(f"Constitution:{constitution} pts")
    print(f"Wisdom:{wisdom} pts")
    print(f"Intelligence:{intelligence} pts")
    print(f"Charisma:{charisma} pts")
    #had a little art moment to seperate the main attributes from the new ones 
    print(" ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ")
    print("' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '")


    if race_choice == 1:
        human_instance = Human(height, weight, hair, eye, strength, dexterity, constitution, intelligence, wisdom, charisma)
        strength, dexterity, constitution, intelligence, wisdom, charisma = human_instance.human(strength, dexterity, constitution, intelligence, wisdom, charisma)
        #I did the +2 points within the huma class so i did not need to add it here
        #final attributes with added skils
        print("Your final attributes are:")
        print(' ' ' ' ' ' ' ' ' ' ' ' ' ')
        print(f"Height:{height} ft")
        print(f"Weight:{weight} lbs")
        print(f"Hair Color:{hair}")
        print(f"Eye Color:{eye}")
        print(f"Strength: {strength} pts")
        print(f"Dexterity: {dexterity} pts")
        print(f"Constitution: {constitution} pts")
        print(f"Wisdom: {wisdom} pts")
        print(f"Intelligence: {intelligence} pts")
        print(f"Charisma: {charisma} pts")
    elif race_choice == 2:
        #pass the orginal skills so it doesnt expect the added skills only for elves. 
        # I refrnced challenge 11 because I was getting an error.  
        elves_instance = Elves(height, weight, hair, eye, strength, dexterity, constitution, intelligence, wisdom, charisma)
        dexterity, charisma = elves_instance.elves(dexterity,charisma)
        #final attributes with added skills
        print("Your final attributes are:")
        print(' ' ' ' ' ' ' ' ' ' ' ' ' ')
        print(f"Height: {height} ft")
        print(f"Weight: {weight} lbs")
        print(f"Hair Color: {hair}")
        print(f"Eye Color: {eye}")
        print(f"Strength: {strength} pts")
        print(f"\033[1m\u001b[35mDexterity: {dexterity} pts \033[0m")
        print(f"Constitution: {constitution} pts")
        print(f"Wisdom: {wisdom} pts")
        print(f"Intelligence: {intelligence} pts")
        print(f"\033[1m\u001b[35mCharisma: {charisma} pts \033[0m")
        print(f"\033[1m\u001b[35mSleep: 100% Resistance \033[0m")
    elif race_choice == 3:
        #cretaed an instance for dwarves again that would call the function within the class
        dwarves_instance = Dwarves(height, weight, hair, eye, strength, dexterity, constitution, intelligence, wisdom, charisma)
        strength, constitution, charisma = dwarves_instance.dwarves(strength,constitution,charisma)
        #final attributes with added skills
        print("Your final attributes are:")
        print(' ' ' ' ' ' ' ' ' ' ' ' ' ')
        print(f"Height:{height} ft")
        print(f"Weight:{weight} lbs")
        print(f"Hair Color:{hair}")
        print(f"Eye Color:{eye}")
        print(f"\033[1m\u001b[35mStrength: {strength} pts \033[0m") 
        print(f"Dexterity: {dexterity} pts")
        print(f"\033[1m\u001b[35mConstitution: {constitution} pts \033[0m") 
        print(f"Wisdom: {wisdom} pts") 
        print(f"Intelligence: {intelligence} pts")
        print(f"\033[1m\u001b[35mCharisma: {charisma} pts \033[0m")
        print(f'\033[1m\u001b[35mMagic: 20% Resistance \033[0m')

#call the main function
if __name__ == "__main__":
    main()
    print('THANK YOU FOR PLAYING')
    print('ENJOY YOUR NEW CHARACTER !!!')

