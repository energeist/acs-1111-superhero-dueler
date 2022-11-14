import random

class Team:
    def __init__(self, team_name):
        '''
        Initializes a team with a team name
            team_name: String
        '''
        self.team_name = team_name
        self.heroes = list()

    def add_hero(self, hero):
        '''
        Adds a hero to the team list
        hero - a hero object
        '''
        self.heroes.append(hero)


    def remove_hero(self, hero_to_remove):
        '''
        Removes a hero from the team list, if that hero isn't found then return 0
        hero - a hero object
        '''
        found_hero = False
        for hero in self.heroes:
            if hero.hero_name == hero_to_remove:
                self.heroes.remove(hero)
                found_hero = True
        if not found_hero:
            return 0

    def view_all_heroes(self):
        '''
        returns a list of current heroes on the team
        '''
        print(f"Heroes on the {self.team_name} roster:")
        for hero in self.heroes:
            print(f"{hero.hero_name}")

    def revive_heroes(self, health=100):
        '''
        Resets current health for all heroes to starting_health
        '''
        for hero in self.heroes:
            hero.current_health = starting_health
    
    def attack(self, other_team):
        '''
        Battle each team against the other
            other_team - team object
        '''
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            random_hero = random.choice(living_heroes)
            random_opponent = random.choice(living_opponents)
            hero_to_remove = random_hero.fight(random_opponent)
            if hero_to_remove in living_heroes:
                self.remove_hero(hero_to_remove)
            else:
                other_team.remove_hero(hero_to_remove)
            print(f"Remaining heroes for {self.team_name}")
            for hero in self.heroes:
                print(f"{hero.hero_name}")
            print()
            print(f"Remaining heroes for {other_team.team_name}")
            for hero in other_team.heroes:
                print(f"{hero.hero_name}")

            