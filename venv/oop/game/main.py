from player import Player

tim = Player("Tim")
# print(tim.name)
# print(tim.lives)
# tim.lives -= 1
# print(tim)

# tim.lives -= 1
# print(tim)

# tim.lives -= 1
# print(tim)

# tim.lives -= 1
# print(tim)

# tim.level += 2
# print(tim)

# tim.score = 500
# print(tim)

from enemy import Enemy

random_monster = Enemy("Basic Enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(12)
print(random_monster)

