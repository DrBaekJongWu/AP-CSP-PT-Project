import random

class pokemon:
    def __init__(self, name, health, att, spatt, defense, spdef, speed, type1, level, a1, a2, a3, a4, type2= False):
        self.name = name
        self.health = health
        self.att = att
        self.spatt = spatt
        self.defense = defense 
        self.spdef = spdef
        self.speed = speed
        self.type1 = type1
        self.type2 = type2
        self.attacks = [a1,a2,a3,a4]
        self.debuff = False
        self.level = level
    def attack(self, enemy, attackMove, attackType, moveType):
        shot = random.randint(0,101)
        acc = attackMove.acc
        if(self.debuff == "confusion" or self.debuff == "blinded"):
            acc -= 20
        if(acc >= shot):
            critical = random.randint(0,10001)
            if(critical <= 625):
                critical = 2
            else:
                critical = 1
            if attackType == "att":
                defStat = enemy.defense
                attStat = self.att
            if attackType == "spatt":
                defStat = enemy.spdef
                attStat = self.spatt
            damage = (((((2*self.level/50)+2)*attackMove.power*(attStat/defStat))/50)+2)*critical
            if(moveType == self.type1 or moveType == self.type2):
                stab = 1.5
            else:
                stab = 1
            damage = damage*stab
            randomCof = random.randint(85,101)/100
            print(randomCof)
            damage = round(damage*randomCof)
            enemy.health -= damage
            print(enemy.health)
class attack:
    def __init__(self, power, acc, movetype , attacktype, debuff=False):
        self.power = power
        self.acc = acc
        self.movetype = movetype
        self.attacktype = attacktype
        self.debuff = debuff
at1 = attack(70,90,"Fire", "att")
at2 = attack(70,90,"Fire", "att")
at3 = attack(70,90,"Fire", "att")
at4 = attack(70,90,"Fire", "att")
p1 = pokemon("p1", 100, 100, 100, 100, 100, 100,"Fire",20, at1,at2,at3,at4)
p2 = pokemon("p2", 100, 100, 100, 100, 100, 100,"Fire",20, at1,at2,at3,at4)
p1.attack(p2,p1.attacks[1], p1.attacks[1].attacktype, p1.attacks[1].movetype)
p2.attack(p2,p1.attacks[1], p1.attacks[1].attacktype, p1.attacks[1].movetype)