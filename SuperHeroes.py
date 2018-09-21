import random
class Ability:
    def __init__(self, name, attack_strength):
    # Initialize Starting values
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        #return attack value
        lowest_attack = self.attack_strength // 2
        return  random.randint(lowest_attack, self.attack_strength)

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength



# -------------------------------** Hero Class **---------------------------------------------


class Hero:
    def __init__(self, name, health = 100):
        #Initialize starting values
        self.abilities = list()
        self.name = name

        self.armors = list()
        self.start_health = start_health
        self.health = start_health
        self.deaths = 0
        self.kills = 0

    """ 1. This method should run the defend method on each piece of armor and calculate the total defense.
    2. If the hero's health is 0, the hero is out of play and should return 0 defense points.
    """
    def defend(self):
        if (self.health > 0): ##Come back to this and see if a while loops will work
            for item in self.armors:
                defence += item.defend()
        return defence

    """
    1. This method should subtract the damage amount from the
    hero's health.
    2. If the hero dies update number of deaths.
    """
    def take_damage(self, damage_amt):
        self.health -= damage_amt
        if(self.health <= 0):
            self.deaths += 1
            return 1
        return 0


    """ 1. This method should add the number of kills to self.kills"""
    def add_kill(self, num_kills):
        self.kills += num_kills


    def add_ability(self, ability):
        # Add ability to abilities wordList
        self.abilities.append(ability)


    def attack(self):
        # Run attack() on every ability the hero has
        total_attack = 0
        if self.abilities != None:
            for ability in self.abilities:
                total_attack = total_attack + ability.attack()
        return total_attack

class Weapon(Ability):
    def attack(self):
        return  random.randint(0, self.attack_strength) #Not sure if this is right as well

#----------------------------------** TEAM CLASS **-----------------------------------------------------------
class Team:

    def __init__(self, team_name):
        """Instantiate Resources"""
        self.name = team_name
        self.heroes = list()
        self.team_kills = 0


    """ 1. Add Hero object to the list"""
    def add_hero(self, Hero):
        self.heroes.append(Hero)


    """ 1. Remove hero from hero list. If hero isn't found, return 0"""
    def remove_hero(self, name):
        if self.name != None:
            for hero in self.view_all_heroes:
                if name in hero.name:
                    self.heroes.remove(hero)
                else:
                    return 0
        else:
            return 0

    """ 1. Find and return hero from list. If hero isn't found, return 0"""
    def find_hero(self, name):
        if self.heroes != None:
            if name == hero.name:
                return heroe
            else:
                return 0

    def view_all_heroes(self):
        """ 1. Print out all heroes to the console"""
        for hero in self.heroes:
            name = hero.name
            print(name)


    """ 1. This method should total our teams attack strength and call the defend() method
    on the rival team that is passed in.
    2. It should call add_kill() on each hero with the number of kills made."""
    def attack(self, other_team):


    """ 1. This method should calculate our team's total defense.
    2. Any damage in excess of our team's total defense should be evenly distributed amongst
    all heroes with the deal_damage() method.
    3. Return number of heroes killed in attack."""
    def defend(self, damage_amt):



    """ 1. Divide the total damage amongst all heroes.
    2. Return the number of heroes that died in attack."""
    def deal_damage(self, damage):
    

    """ 1. this method should reset all heroes health  to their original starting value. """
    def revive_heroes(self, health = 100):



    """ 1. This methof should print the ratio of kills/deaths for each member of the team to the screen.
    2. This data must be output to the terminal. """
    def stats(self):



    """ 1. This method should update each hero when there is a team kill. """
    def update_kills(self):



#-------------------------------** Armor Class ** -----------------------------
class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        """
        Return a random value between 0 and the
        initialized defend strength.
        """
        return random.randint(0, self.defense)


    # If you run this file from the terminal, this block is executed

if __name__ == "__main__":
    hero = Hero("Super Man")
    print(hero.attack())
    ability = Ability("Laser Eyes", 600)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Strength", 1000)
    hero.add_ability(new_ability)
    print(hero.attack())
