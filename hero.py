import random

class Ability:
    def __init__(self, ability_name, max_damage):
        '''Instance properties
            ability_name: String
            max_damage: Integer
        '''
        self.ability_name = ability_name
        self.max_damage = max_damage

    def attack(self):
        '''Return a value between 0 and the value set by self.max_damage'''
        random_value = random.randint(0, self.max_damage)
        return random_value

class Hero:
    def __init__(self, hero_name, starting_health=100):
        '''Instance properties
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.hero_name = hero_name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        '''Current hero will take turns fighting the opponent hero passed in.
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
