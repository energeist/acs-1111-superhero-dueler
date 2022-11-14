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
        max_damage = int(input("What is the max damage of the ability? > "))
        return Ability(ability_name, max_damage)

    def create_weapon(self):
        '''
        Prompt for weapon information.
        return weapon with values from user input
        '''
        weapon_name = input("What is the weapon name? > ")
        max_damage = int(input("What is the max damage of the weapon? > "))
        return Weapon(weapon_name, max_damage)

    def create_armor(self):
        '''
        Prompt for armor information.
        return armor with values from user input
        '''
        armor_name = input("What is the armor name? > ")
        max_damage = int(input("What is the max block value of the armor? > "))
        return Armor(armor_name, max_damage)

    def create_hero(self):
        '''
        Prompt for hero information.
        return hero with values from user input
        '''
        hero_name = input("Hero's name > ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice > ")
            if add_item == "1":
                new_ability = self.create_ability()
                hero.add_ability(new_ability)
            elif add_item == "2":
                new_weapon = self.create_weapon()
                hero.add_ability(new_weapon)
            elif add_item == "3":
                new_armor = self.create_armor()
                hero.add_armor(new_armor)
        return hero

    def build_team_one(self):
        '''
        Prompt the user to build team_one
        '''
        num_of_team_members = int(input("How many members would you like on Team One? > "))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''
        Prompt the user to build team_one
        '''
        num_of_team_members = int(input("How many members would you like on Team Two? > "))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''
        Battle team_one and team_two together
        '''
        self.team_one.attack(self.team_two)

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
            print(f"The surviving members of {arena.team_one.team_name} are: {team_survivors}")


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
            print(f"The surviving members of {arena.team_two.team_name} are: {team_survivors}")

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()


