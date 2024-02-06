def SAVE(Character, Inventory):
  with open('Saves.txt', "w") as file:
    file.write(f"{Character.GetName()}\n{Character.GetHealth().GetCurrentHealth()}\n{Character.GetHealth().GetMaxHealth()}")

def ShowStats(Character):
  return f"Name: {Character.GetName()}\nCurrent Health: {Character.GetHealth().GetCurrentHealth()}\nMax Health: {Character.GetHealth().GetMaxHealth()}"

def ShowHealth(Character):
  return f"{Character.GetName()} has {Character.GetHealth().GetCurrentHealth()}"

def ShowInventory(Inventory):
  print("--Inventory--")
  for item in Inventory.GetItems():
    if item != ".":
      print(f"- {item.GetName()}")
    else:
      print(".")

def Attack(Character, Other, Weapon):
  Weapon.UseWeapon(Other)
  return f"{Character.GetName()} did {Weapon.GetDamage()} to {Other.GetName()}"