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



# ----------------------------------------------------------------------------


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

    """ This method should run the defend method on each piece of armor and calculate the total defense.
    If the hero's health is 0, the hero is out of play and should return 0 defense points.
    """
    def defend(self):
        if (self.health > 0): ##Come back to this and see if a while loops will work
            for item in self.armors:
                defence += item.defend()
        return defence

    """
    This method should subtract the damage amount from the
    hero's health.
    If the hero dies update number of deaths.
    """
    def take_damage(self, damage_amt):
        self.health -= damage_amt
        if(self.health <= 0):
            self.deaths += 1
            return 1
        return 0


    """ This method should add the number of kills to self.kills"""
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

    def add_hero(self, Hero):
        """Add Hero object to the list"""
        self.heroes.append(Hero) # Think this is right

    def remove_hero(self, name):
        """Remove hero from hero list. If hero isn't found, return 0"""
        if self.name != None:
            for hero in self.view_all_heroes:
                if name in hero.name:
                    self.heroes.remove(hero)
                else:
                    return 0
        else:
            return 0

    def find_hero(self, name):
        """Find and return hero from list. If hero isn't found, return 0"""
        if self.heroes != None:
            if name == hero.name:
                return heroe
            else:
                return 0

    def view_all_heroes(self):
        """Print out all heroes to the console"""
        for hero in self.heroes:
            name = hero.name
            print(name)

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
