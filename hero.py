import random
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

class Hero:
    def __init__(self, hero_name, starting_health=100):
        '''Instance properties
            abilities: list
            armors: list
            name: String
            starting_health: Integer - default value: 100
            current_health: Integer
        '''
        self.abilities = list()
        self.armors = list()
        self.hero_name = hero_name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        '''
        Add an ability to the current hero's list of abilities
            ability: ability object
        '''
        self.abilities.append(ability)

    def add_armor(self, armor):
        '''
        Add an armor to the current hero's list of armors
            armor: armor object
        '''
        self.armors.append(armor)

    def attack(self):
        '''
        Calculate total damage from all ability attacks.
            return: total_damage, Integer
        '''
        total_damage = 0
        for ability in self.abilities:
            current_damage = ability.attack()
            total_damage += current_damage
            print(f"{self.hero_name} is attacking with {ability.ability_name} for {current_damage} damage")
        print(f"Total damage dealt by all abilities: {total_damage}")
        return total_damage

    def defend(self):
        '''
        Calculate the total block amount from all armor blocks
            incoming_damage: Integer
            return: unblocked_damage, Integer
        '''
        total_block = 0
        for armor in self.armors:
            current_block = armor.block()
            total_block += current_block
            print(f"{self.hero_name} is blocking with {armor.armor_name} for {current_block} blocked damage")
        print(f"Total damage blocked by all armor: {total_block}")
        return total_block

    def take_damage(self, damage):
        '''
        Subtracts the amount of unblocked damage after defending from self.current_health
            damage: Integer
        '''
        if damage > 0:
            unblocked_damage = 0
            print(f"Unblocked damage: {damage}")
            self.current_health -= damage
        else:
            print(f"{self.hero_name} blocked all the incoming damage!")
        

    def is_alive(self):
        '''
        Return True or False depending on whether the hero is alive or not.
            Returns alive, boolean
        '''
        alive = True
        if self.current_health <= 0:
            alive = False
        return alive

    def add_death(self, num_deaths):
        '''
        Setter for self.deaths property
            num_deaths: Integer
        '''
        self.deaths += num_deaths

    def add_kill(self, num_kills):
        '''
        Setter for self.kills property
            num_kills: Integer
        '''
        self.kills += num_kills

    def fight(self, opponent):
        '''
        Current hero will take turns fighting the opponent hero passed in. Attack order is randomly chosen by round to ensure a fair fight, since we don't have a speed attribute (yet).
            opponent - hero object
        '''
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Neither hero has any abilities, the fight is a draw!")
        else:
            round = 0
            while self.is_alive() == True and opponent.is_alive() == True:
                round +=1
                # randomize the order of attacks for the turn:
                if random.randint(0,1) == 0:
                    attack_order = [self, opponent]
                else:
                    attack_order = [opponent, self]
                # first hero attacks second hero
                print(f"Round {round} - Attack order: {attack_order[0].hero_name} -> {attack_order[1].hero_name}.")
                attack_order[1].take_damage(attack_order[0].attack()-attack_order[1].defend())
                print(f"{attack_order[1].hero_name} has {attack_order[1].current_health} HP remaining.")
                if attack_order[1].is_alive():
                    # second hero attacks back if still alive
                    attack_order[0].take_damage(attack_order[1].attack()-attack_order[0].defend())
                    print(f"{attack_order[0].hero_name} has {attack_order[0].current_health} HP remaining.")
            if self.is_alive() == False:
                print(f"{opponent.hero_name} wins the fight after {round} rounds!")
                loser = self
                opponent.add_kill(1)
                self.add_death(1)
            if opponent.is_alive() == False:
                print(f"{self.hero_name} wins the fight after {round} rounds!")
                loser = opponent
                self.add_kill(1)
                opponent.add_death(1)            
        return loser
            
    # def fight(self, opponent):
    #     '''
    #     Current hero will take turns fighting the opponent hero passed in.
    #     '''
    #     self_score = 0
    #     total_health = self.current_health + opponent.current_health
    #     if random.randint(1,100) <= (self.current_health / total_health * 100):
    #         print(f"{self.hero_name} wins the battle against {opponent.hero_name}!")
    #         self_score += 1
    #     else:
    #         print(f"{opponent.hero_name} wins the battle against {self.hero_name}!")
    #     return self_score

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 100)
    other_hero = Hero("Papa", 100)

####TEST CODE AREA####

def solo_heroes_test():
    ability1 = Ability("WHERE'S WILL???", 10)
    ability2 = Ability("WHERE'S WILL??!!!?!?!", 25)
    armor1 = Armor("Mithril chain", 15)
    armor2 = Armor("A big-ass shield", 10)
    ability3 = Ability("Psionic Child Army", 35)
    ability4 = Ability("Splash", 5)
    weapon1 = Weapon("Christmas Lights", 25)
    weapon2 = Weapon("Gaslight", 25)
    my_hero.add_ability(ability1)
    my_hero.add_ability(ability2)
    my_hero.add_ability(weapon1)
    my_hero.add_armor(armor1)
    my_hero.add_armor(armor2)
    other_hero.add_ability(ability3)
    other_hero.add_ability(ability4)
    other_hero.add_ability(weapon2)
    other_hero.add_armor(armor1)
    other_hero.add_armor(armor2)
    my_hero.fight(other_hero)

def jodie_athena_test():
    jodie = Hero("Jodie Foster", 100)
    aliens = Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    athena = Hero("Athena", 100)
    socks = Armor("Socks", 10)
    athena.add_armor(socks)
    jodie.fight(athena)


# fights = 0
# score = 0
# while fights < 100:
#     score += my_hero.fight(other_hero)
#     fights += 1

# print(f"{my_hero.hero_name} won {score} out of {fights} fights!")

def test_team_attack():
    team_one = Team("One")
    jodie = Hero("Jodie Foster")
    brodie = Hero("Brodie Gloster")
    aliens = Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    brodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_one.add_hero(brodie)
    print(team_one.heroes[0].hero_name)
    print(team_one.heroes[1].hero_name)
    team_two = Team("Two")
    athena = Hero("Athena")
    socks = Armor("Socks", 10)
    juno = Hero("Juno")
    juno.add_armor(socks)
    athena.add_armor(socks)
    team_two.add_hero(athena)
    team_two.add_hero(juno)
    print(team_two.heroes[0].hero_name)
    print(team_two.heroes[1].hero_name) 
    team_one.attack(team_two)

# solo_heroes_test()
test_team_attack()
# jodie_athena_test()