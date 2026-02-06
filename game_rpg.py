#Latihan 1

class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.info()
hero2.info()

hero1.hp = 500
print(hero1.hp)

#Latihan 2
class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2)
hero2.serang(hero1)

#Latihan 3
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print("Mana tidak cukup")

eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
eudora.serang(balmond)
eudora.skill_fireball(balmond)

#Latihan 4
class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal

    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai):
        if nilai < 0:
            self.__hp = 0
        elif nilai > 1000:
            print("Cheat terdeteksi!")
            self.__hp = 1000
        else:
            self.__hp = nilai

    def diserang(self, damage):
        self.set_hp(self.get_hp() - damage)
        print(f"{self.nama} HP tersisa {self.get_hp()}")

hero1 = Hero("Layla", 100)
hero1.set_hp(-50)
print(hero1.get_hp())

#Latihan 5
from abc import ABC, abstractmethod

class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass

class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menyerang {target}")

    def info(self):
        print(f"Saya Hero {self.nama}")

class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menyerang {target}")

    def info(self):
        print(f"Saya Monster {self.jenis}")

#latihan 6
class Hero:
    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print("Hero menyerang")

class Mage(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) Fireball!")

class Archer(Hero):
    def serang(self):
        print(f"{self.nama} (Archer) Panah!")

class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} (Fighter) Pedang!")

class Healer(Hero):
    def serang(self):
        print(f"{self.nama} menyembuhkan teman!")

pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Healer("Estes")
]

for p in pasukan:
    p.serang()
