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