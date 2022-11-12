import random

class Armor:
    def __init__(self, armor_name, max_block):
        '''Instantiate instance properties:
            name: String
            max_block: Integer
        '''
        self.armor_name = armor_name
        self.max_block = max_block

    def block(self):
        '''Generates and returns a random block_value between 0 and self.max_block'''
        block_value = random.randint(0, self.max_block)
        return block_value

if __name__ == "__main__":
    shield = Armor("Debugging shield", 15)
    print(shield.armor_name)
    print(shield.block())