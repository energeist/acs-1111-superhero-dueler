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

if __name__ == "__main__":
    ability = Ability("Debug Ball", 15)
    print(ability.ability_name)
    print(ability.attack())