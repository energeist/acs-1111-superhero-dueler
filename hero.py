import random
from ability import Ability

class Hero:
    def __init__(self, hero_name, starting_health=100):
        '''Instance properties
            name: String
            starting_health: Integer - default value: 100
            current_health: Integer
        '''
        self.hero_name = hero_name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        '''
        
        '''

    def attack(self):
        '''
        '''

    def defend(self, incoming_damage):
        '''
        incoming_damage: Integer
        '''    

    def take_damage(self, damage):
        '''
        damage: Integer
        '''

    def is_alive(self):
        '''
        '''

    def fight(self, opponent):
        '''
        Current hero will take turns fighting the opponent hero passed in.
        '''
        self_score = 0
        total_health = self.current_health + opponent.current_health
        if random.randint(1,100) <= (self.current_health / total_health * 100):
            print(f"{self.hero_name} wins the battle against {opponent.hero_name}!")
            self_score += 1
        else:
            print(f"{opponent.hero_name} wins the battle against {self.hero_name}!")
        return self_score

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    other_hero = Hero("Papa", 120)
    ability = Ability("Debug", 15)
    print(ability.ability_name)
    print(ability.attack())

# fights = 0
# score = 0
# while fights < 100:
#     score += my_hero.fight(other_hero)
#     fights += 1

# print(f"{my_hero.hero_name} won {score} out of {fights} fights!")
