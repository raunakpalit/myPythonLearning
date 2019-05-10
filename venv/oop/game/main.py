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

from enemy import Enemy, Troll, Vampyre, VampyreKing

# random_monster = Enemy("Basic Enemy", 12, 1)
# print(random_monster)

# random_monster.take_damage(4)
# print(random_monster)

# random_monster.take_damage(8)
# print(random_monster)

# random_monster.take_damage(12)
# print(random_monster)

# ugly_troll = Troll("Pug")
# print(ugly_troll)

# another_troll = Troll("Ug")
# print(another_troll)

# brother = Troll("Urg")
# print(brother)

# brother.take_damage(3)
# print(brother)

# brother.take_damage(5)
# print(brother)

# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()

# vampyre_instance = Vampyre("FirstVampyre")
# print(vampyre_instance)

# vampyre_instance.take_damage(4)
# print(vampyre_instance)

# vampyre_instance.take_damage(6)
# print(vampyre_instance)

# while vampyre_instance.alive:
#     vampyre_instance.take_damage(1)
    # print(vampyre_instance)

vamp = VampyreKing("VKing")
print(vamp)

vamp.take_damage(8)
print(vamp)
