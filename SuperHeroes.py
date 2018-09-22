import random
#----------------------------------** Hero Class **-----------------------------------------------------------
class Hero:
    """ 1. Initialize starting values"""
    def __init__(self, name, health = 100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0


    """ 1. This method should run the defend method on each piece of armor and calculate the total defense.
    2. If the hero's health is 0, the hero is out of play and should return 0 defense points."""
    def defend(self):
        defence = 0
        if (self.health > 0): ##Come back to this and see if a while loops will work
            for item in self.armors:
                defence += item.defend()
        return defence


    """ 1. This method should subtract the damage amount from the hero's health.
    2. If the hero dies update number of deaths."""
    def take_damage(self, damage_amt):
        self.health -= damage_amt
        if(self.health <= 0):
            self.deaths += 1
            return 1
        return 0


    """ 1. This method should add the number of kills to self.kills"""
    def add_kill(self, num_kills):
        self.kills += num_kills


    """ 1. Add ability to abilities wordList"""
    def add_ability(self, ability):
        self.abilities.append(ability)


    def add_armor(self, armor):
         self.armors.append(armor)


    """ 1. Run attack() on every ability the hero has"""
    def attack(self):
        total_attack = 0
        if self.abilities != None:
            for ability in self.abilities:
                total_attack = total_attack + ability.attack()
        return total_attack



#----------------------------------** Ability Class **-----------------------------------------------------------
class Ability:
    """ 1. Initialize Starting values"""
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength


    """ 1. Return attack value"""
    def attack(self):
        lowest_attack = self.attack_strength // 2
        return  random.randint(lowest_attack, self.attack_strength)


    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength


#----------------------------------** Weapon Class **-----------------------------------------------------------
class Weapon(Ability):
    def attack(self):
        return  random.randint(0, self.attack_strength) #Not sure if this is right as well


#----------------------------------** ARMOR CLASS **-----------------------------------------------------------
class Armor:
    """ 1. Instantiate name and defense strength."""
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


    """ 1. Return a random value between 0 and the initialized defend strength."""
    def defend(self):
        return random.randint(0, self.defense)


#----------------------------------** TEAM CLASS **-----------------------------------------------------------
class Team:
    """ 1. Instantiate Resources"""
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()
        self.team_kills = 0

    """ 1. Add Hero object to the list"""
    def add_hero(self, Hero):
        self.heroes.append(Hero) # Think this is right


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


    """ 1. Find and return hero from list.
    2. If hero isn't found, return 0"""
    def find_hero(self, name):
        if self.heroes != None:
            if name == hero.name:
                return hero
            else:
                return 0


    """ 1. Print out all heroes to the console"""
    def view_all_heroes(self):
        for hero in self.heroes:
            name = hero.name
            print(name) ##### Come back to this, maybe you can simplify it


    """ 1. This method should total our teams attack strength and call the defend() method on the rival team that is passed in.
    2. It should call add_kill() on each hero with the number of kills made."""
    def attack(self, other_team):
        attack_total = 0
        for hero in self.heroes:
            print(hero.name)
            attack_total += hero.attack()
        kills = other_team.defend(attack_total)
        self.team_kills += kills
        for hero in self.heroes:
            hero.add_kill(kills)


    """ 1. This method should calculate our team's total defense.
    2. Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.
    3. Return number of heroes killed in attack."""
    def defend(self, damage_amt):
        defence = 0
        for hero in self.heroes:
            defence += hero.defend()
        if(damage_amt > defence):
            return self.deal_damage(damage_amt - defence)
        return 0

    """ 1. Divide the total damage amongst all heroes.
    2. Return the number of heros that died in attack."""
    def deal_damage(self, damage):
        deaths = 0
        for hero in self.heroes:
            deaths += hero.take_damage(damage / len(self.heroes))
        return deaths

    """ 1. This method should reset all heroes health to their original starting value."""
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.health = hero.start_health

        """ 1. This method should print the ratio of kills/deaths for each member of the team to the screen.
        2. This data must be output to the terminal."""
    def stats(self):
        print(self.name)
        for hero in self.heroes:
            hero.display()


    """1. This method should update each hero when there is a team kill."""
    def update_kills(self):
        return self.team_kills

#----------------------------------** ARENA CLASS **-----------------------------------------------------------
class Arena:
    """ 1. self.team_one = None
    2. self.team_two = None"""
    def __init__(self, team_size):
        self.team_one = None
        self.team_two = None
        self.team_size = team_size


    """ 1. This method should allow a user to build team one."""
    def build_team_one(self):
        self.team_one = Team(input("What is the name of your team?: "))
        print("Hero time! Both teams have " + str(self.team_size) + " players")
        for i in range(self.team_size):
            print("Hero number {}. ".format(i))
            self.team_one.add_hero(create_hero())


    """ 1. This method should allow user to build team two."""
    def build_team_two(self):
        self.team_two = Team(input("What is the name of the second team?: "))
        print("Hero Time! Both teams have " + str(self.team_size) + " players")
        for i in range(self.team_size):
            print("Hero number {}. ".format(i))
            self.team_two.add_hero(create_hero())


    """ 1. This method should continue to battle teams until
    one or both teams are dead."""
    def team_battle(self):
        while(self.team_one.team_kills < self.team_size and self.team_two.team_kills < self.team_size):
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
            self.show_stats()


    """ 1. This method should print out the battle statistics
    including each heroes kill/death ratio."""
    def show_stats(self):
        self.team_one.stats()
        self.team_two.stats()

#----------------------------------** TEST **-----------------------------------------------------------
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
