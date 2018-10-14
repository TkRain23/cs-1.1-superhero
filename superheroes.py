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
    def __init__(self, name, health=100):
        # Initialize starting values
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

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

    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense.
        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.defend()
        if self.health == 0:
            total_defense = 0
            # self.heroes.remove(hero)
        return total_defense

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the
        hero's health.

        If the hero dies update number of deaths.
        """
        if self.health > 0:
            self.health -= damage_amt
        if self.health < 1:
            self.deaths += 1
            return self.deaths

    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """
        self.kills += num_kills

    def add_armor(self, Armor):
        """
        This method equps a piece of armor to the hero
        """
        self.armors.append(Armor)


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

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.
        It should call add_kill() on each hero with the number of kills made.
        """
        total_team_strength = 0

        for hero in self.heroes:
            total_team_strength += hero.attack()

        for hero in self.heroes:
            # other_team.defend(total_team_strength)
            hero.add_kill(other_team.defend(total_team_strength))
        # return total_team_strength

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """

        total_team_defense = 0

        for hero in self.heroes:
            total_team_defense += hero.defend()

        if damage_amt > total_team_defense:
            damage_amt -= total_team_defense
            return self.deal_damage(damage_amt)

    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """

        number_of_heroes = 0
        number_of_deaths = 0

        for hero in self.heroes:
            number_of_heroes += 1

        distributed_damage = damage // number_of_heroes

        for hero in self.heroes:
            if hero.health > distributed_damage:
                hero.take_damage(distributed_damage)
            else:
                hero.take_damage(distributed_damage)
                number_of_deaths += 1

        return number_of_deaths

    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """

        #  check all heroes in hero list
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """

        for hero in self.heroes:
            print("{0} Stats - Kills: {1} | Deaths: {2}".format(hero.name, hero.kills, hero.deaths))


    # def update_kills(self):
    #     """
    #     This method should update each hero when there is a team kill.
    #     """
    #     team_kill = 0
    #     for hero in self.heroes:
    #
    #         hero.add_kill()

    def heroes_are_alive(self):
        """
        This method returns true if there are still heroes alive.
        """
        for hero in self.heroes:
            if hero.health <= 0:
                return False
        return True


class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = str(name)
        self.defense = int(defense)

    def defend(self):
        """
        Return a random value between 0 and the
        initialized defend strength.
        """
        random_defend_value = random.randint(0, self.defense)
        return random_defend_value


class Arena:
    def __init__(self, teams_one, team_two):
        """
        Declare variables
        """
        self.team_one = team_one
        self.team_two = team_two

    def add_new_hero(self, team):
        hero_name = input("Enter Hero Name: ")
        new_hero = Hero(hero_name)
        team.add_hero(new_hero)
        return new_hero

    def add_new_ability(self, hero):
        user_incomplete = True
        while user_incomplete:
            ability_name = input("Enter Ability Name: ")
            ability_power = input("Enter Ability Power: ")
            new_ability = Ability(ability_name, int(ability_power))
            hero.add_ability(new_ability)

            add_more_ability = input('Add another Ability (Yes or No): ')
            if add_more_ability.upper() == 'NO':
                user_incomplete = False


    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        user_incomplete = True
        while user_incomplete:
            hero = self.add_new_hero(self.team_one)
            self.add_new_ability(hero)

            is_user_complete = input("Add another Hero? (Enter Yes or No): ")
            if is_user_complete.upper() == "NO":
                user_incomplete = False


    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
        user_incomplete = True
        while user_incomplete:
            hero = self.add_new_hero(self.team_two)
            self.add_new_ability(hero)

            is_user_complete = input("Add another Hero? (Enter Yes or No): ")
            if is_user_complete.upper() == "NO":
                user_incomplete = False
            elif user_incomplete.upper() != "YES":
                is_user_complete = input("Add another Hero? (Enter Yes or No): ")

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """
        battle_in_progress = True
        battle_victor = 0

        while battle_in_progress:
            attack_turn = random.randint(0,1)

            if attack_turn == 0:
                self.team_one.attack(self.team_two)
                battle_in_progress = self.team_two.heroes_are_alive()
                if battle_in_progress == False:
                    battle_victor = 0
            elif attack_turn == 1:
                self.team_two.attack(self.team_one)
                battle_in_progress = self.team_one.heroes_are_alive()
                if battle_in_progress == False:
                    battle_victor = 1

        if battle_victor == 0:
            print('The Jedi win!')
        elif battle_victor == 1:
            print('The Sith win!')

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
        print("Team One:")
        self.team_one.stats()
        print("Team Two:")
        self.team_two.stats()


if __name__ == "__main__":
    game_in_progress = True

    team_one = Team("Jedi")
    team_two = Team("Sith")

    arena = Arena(team_one, team_two)

    print('Build the Jedi Team: ')
    arena.build_team_one()

    print('Build the Sith Team: ')
    arena.build_team_two()
    print('May The Force Be With You: War Begins')

    while game_in_progress:
        arena.team_battle()
        arena.show_stats()
        game_restart = input("Play Again? Y or N: ")

        if game_restart.lower() == "n":
            game_in_progress = False

        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
