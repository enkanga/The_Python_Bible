import random

difficulty = 2 # 1 : easy, 2 : medium, 3: hard
health = 50
potion_health = int(random.randint(25, 50) / difficulty)

health = health + potion_health
print(health)
