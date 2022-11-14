from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    '''
    Instantiate properties
        team_one: None
        team_two: None
    '''
    self.team_one = Team("Team One")
    self.team_two = Team("Team Two")

    def create_ability(self):
        '''
        Prompt for ability information.
        return ability with values from user input
        '''
        ability_name = input("What is the ability name? > ")
        max_damage = input("What is the max damage of the ability? > ")
        return Ability(ability_name, max_damage)

    def create_weapon(self):
        '''
        Prompt for weapon information.
        return weapon with values from user input
        '''
        weapon_name = input("What is the weapon name? > ")
        max_damage = input("What is the max damage of the weapon? > ")
        return Weapon(weapon_name, max_damage)

    def create_armor(self):
        '''
        Prompt for armor information.
        return armor with values from user input
        '''
        armor_name = input("What is the armor name? > ")
        max_damage = input("What is the max damage of the armor? > ")
        return Armor(weapon_name, max_damage)

    def create_hero(self):
        '''
        Prompt for hero information.
        return hero with values from user input
        '''
        hero_name = input("Hero's name > ")
        hero = Hero(hero_name)
        add_time = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice > ")
            if add_item == "1":
                new_ability = create_ability(self)
                hero.add_ability(ability)
            elif add_item == "2":
                new_weapon = create_weapon(self)
                hero.add_weapon(weapon)
            elif add_item == "3":
                new_armor = create_armor(self)
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        '''
        Prompt the user to build team_one
        '''
        num_of_team_members = int(inpuit("How many members would you like on Team One? > "))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''
        Prompt the user to build team_one
        '''
        num_of_team_members = int(inpuit("How many members would you like on Team Two? > "))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''
        Battle team_one and team_two together
        '''
        team_one.attack(team_two)

    def show_stats(self):
        '''
        Prints team statistics to the terminal
        '''
        print()
        print(self.team_one.team_name + " statistics: ")
        self.team_one.stats()
        print()
        print(self.team_two.team_name + " statistics: ")
        self.team_two.stats()
        print()

        team_kills = 0
        team_deaths = 0
        team_survivors = list()
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
            if hero.deaths == 0:
                team_survivors.append(hero.hero_name)
        if team_deaths == 0:            
            team_deaths = 1
        print(self.team_one.team_name + " average K/D ratio was: " + str(team_kills/team_deaths))
        if len(team_survivors) > 0:
            print(f"The surviving members of {team_one.team_name} are: {team_survivors}")


        team_kills = 0
        team_deaths = 0
        team_survivors = list()
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
            if hero.deaths == 0:
                team_survivors.append(hero.hero_name)   
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.team_name + " average K/D ratio was: " + str(team_kills/team_deaths))
        if len(team_survivors) > 0:
            print(f"The surviving members of {team_one.team_name} are: {team_survivors}")




