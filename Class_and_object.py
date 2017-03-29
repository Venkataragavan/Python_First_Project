class hero():
    life = 5

    def __init__(self):
        print('Hero is ready')

    def attack(self):
        print('Hero : You are attacking an enemy!')
        enemy.defend(self)

    def defend(self):
        print('Hero : You are being attacked')
        self.life-=1
        print(str(self.life)+ 'hero lives left')

class enemy(hero):
    life=5

    def __init__(self):
        print('Enemy is ready')

    def attack(self):
        print('Enemy : You are attacking the hero')
        hero.defend(self)

    def defend(self):
        print('Enemy : You are being attacked')
        self.life-=1
        print(str(self.life) + ' enemy lives left')

hero1 = hero()
enemy1= enemy()

hero1.attack()
enemy1.attack()
hero1.defend()
enemy1.defend()
