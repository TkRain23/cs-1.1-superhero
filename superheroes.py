import random


class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting vlaues
        # Set Ability name
        self.name = name
        # Set Attack Strength
        self.attack_strength = attack_strength

    def attack(self):
        # Return attack value
        # Calculate lowest attack value as an integer
        lowest_attack = self.attack_strength//2
        # Use Random.int(a, b) to select a random attack valueself.
        random_attack_value = random.randint(lowest_attack, self.attack_strength)
        # Return attack value between 0 and the full attack.
        return random_attack_value

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength


class Hero:
    def __init__(self, name):
        # Initialize starting values
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def attack(self):
        # Run attack() on every ability hero has
        # Call the attack method on every ability in our ability list
        total_attack = 0
        for ability in self.abilities:
            # Add up and return the total of all attacks
            total_attack += ability.attack()
        return total_attack

    self.armors = list()
    self.start_health = start_health
    self.health = health
    self.deaths = 0
    self.kills = 0

    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense.
        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """

    def take_damage(self, damage_amt):
        pass

    def add_kill(self, num_kills):
        pass


class Weapon(Ability):

    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        # Use Random.int(a, b) to select a random attack valueself.
        random_attack_value = random.randint(0, self.attack_strength)
        # Return attack value between 0 and the full attack.
        return random_attack_value


class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
        return 0

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        for hero in self.heroes:
            if name == hero.name:
                return hero
        return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)

    def defend(self, damage_amt):
        pass

    def deal_damage(self, damage):
        pass

    def revive_heroes(self, health=100):
        pass

    def stats(self):
        pass

    def update_kills(self):
        pass


class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        """
        Return a random value between 0 and the
        initialized defend strength.
        """
        random_defend_value = random.randint(0, self.defense)
        return random_defend_value


if __name__ == "__main__":
    # If you run this file from the terminal this block is exectured

    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
