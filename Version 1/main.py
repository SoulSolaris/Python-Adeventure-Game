import Classes, Functions
  
#if __name__ == "__main__":
try:
  with open("Saves.txt", 'r') as file:
    SaveName = file.readline().strip()
    SaveCHealth = int(file.readline().strip())
    SaveMhealth = int(file.readline().strip())
  Player = Classes.Character(SaveName, Classes.Health(SaveCHealth, SaveMhealth))
except:
  Player = Classes.Character(input("Enter username: "), Classes.Health())

  
Enemy = Classes.Character("Dog", Classes.Health())
Sword = Classes.Weapon("Sword", 30)

PlayerInventory = Classes.Inventory(3)

print(Functions.ShowStats(Player))
Functions.SAVE(Player, PlayerInventory)


"""
Functions.ShowInventory(PlayerInventory)
PlayerInventory.AddItem(Sword)
Functions.ShowInventory(PlayerInventory)
"""


"""
print(Functions.ShowStats(Player))
print(Functions.ShowStats(Enemy))
print(Functions.Attack(Player, Enemy, Sword))
print(Functions.ShowStats(Player))
print(Functions.ShowStats(Enemy))
"""