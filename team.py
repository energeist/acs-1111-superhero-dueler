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
                print("found")
                found_hero = True
        if not found_hero:
            print("not found")
            return 0

    def view_all_heroes(self):
        '''
        returns a list of current heroes on the team
        '''
        print(f"Heroes on the {self.team_name} roster:")
        for hero in self.heroes:
            print(f"{hero.hero_name}")

    def stats(self):
        '''
        Print team statistics
        '''
        for hero in self.heroes:
            if hero.deaths == 0:
                deaths = 0
            else:
                deaths = hero.deaths
            kd = hero.kills/deaths
            print(f"{hero.name} Kill/Death ratio: {kd}")

    def revive_heroes(self, health=100):
        '''
        Resets current health for all heroes to starting_health
        '''
        for hero in self.heroes:
            hero.current_health = health
    
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
        # i = 0
        # while i < 2:
            random_hero = random.choice(living_heroes)
            print("random hero: " + random_hero.hero_name)
            random_opponent = random.choice(living_opponents)
            print("random opponent: " + random_opponent.hero_name)
            hero_to_remove = random_hero.fight(random_opponent)
            print("hero to remove: " + hero_to_remove.hero_name)
            if hero_to_remove in living_heroes:
                living_heroes.remove(hero_to_remove)
                print("floop")
            else:
                print("doink")
                living_opponents.remove(hero_to_remove)
            if living_heroes:
                print(f"length of living_heroes: {len(living_heroes)}")
                print(f"Remaining heroes for {self.team_name}")
                for hero in living_heroes:
                    print(f"{hero.hero_name}")
            print()
            if living_opponents:
                print(f"length of living_opponents: {len(living_opponents)}")
                print(f"Remaining heroes for {other_team.team_name}")
                for hero in living_opponents:
                    print(f"{hero.hero_name}")
            print()
            # i += 1

            