class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def damage_count(self, armor):
        total_damage = self.damage - armor
        return total_damage

    def attack(self, health, armor):
        health -= self.damage_count(armor)
        return health


class Player(Person):
    def attack(self, enemy_health, enemy_armor):
        output = super(Player, self).attack(enemy_health, enemy_armor)
        output_text = f'The player {self.name} attacks, the enemy\'s health is now: {output}'
        print(output_text)
        return output


class Enemy(Person):
    def attack(self, player_health, player_armor):
        output = super(Enemy, self).attack(player_health, player_armor)
        output_text = f'The enemy {self.name} attacks, the player\'s health is now: {output}'
        print(output_text)
        return output


class Game:
    def __init__(self, player, enemy):
        self.player: Player = player
        self.enemy: Enemy = enemy

    def battle_cycle(self, turns):
        enemy_health = self.enemy.health
        enemy_armor = self.enemy.armor
        player_health = self.player.health
        player_armor = self.player.armor
        for i in range(turns):
            if enemy_health > 0 and player_health > 0:
                print(f'Turn #{i + 1}')
                enemy_health = self.player.attack(enemy_health, enemy_armor)
                if enemy_health > 0:
                    player_health = self.enemy.attack(player_health, player_armor)
                    if player_health <= 0:
                        print(f'The player {self.player.name} is killed by the enemy!')
                        break
                elif enemy_health <= 0:
                    print(f'The enemy {self.enemy.name} is killed by the player!')
                    break
            else:
                break
        print(player_health, enemy_health)


if __name__ == '__main__':
    player1 = Player('Mirriy', 256, 121, 25)
    enemy1 = Enemy('Chaos Prophet', 666, 66, 6)
    battle = Game(player1, enemy1)
    battle.battle_cycle(9)
