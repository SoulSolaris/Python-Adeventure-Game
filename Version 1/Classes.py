class Health:
  def __init__(self, amount=50, maxHealth=-1):
    self.__currentHealth = amount
    if maxHealth != -1:
      self.__maxHealth = maxHealth
    else:
      self.__maxHealth = amount

  def GetCurrentHealth(self):
    return self.__currentHealth
  def GetMaxHealth(self):
    return self.__maxHealth

  def AddHealth(self, amount):
    if self.currentHealth + amount < self.__maxHealth:
      self.__currentHealth += amount
    else:
      self.__currentHealth = self.__maxHealth

  def LoseHealth(self, amount):
    self.__currentHealth -= amount

  def IsDead(self):
    return self.__currentHealth <= 0

class Inventory:
  def __init__(self, length):
    self.__maxLength = length
    self.__items = ["."]*self.__maxLength
    self.__pointer = 0
  
  def GetItems(self):
    return self.__items
  def GetMaxLength(self):
    return self.__maxLength
  
  def AddItem(self, item):
    if self.__items[-1] == ".":
      self.__items[self.__pointer] = item
      self.__pointer += 1
      return True # The item was added to the list
    else:
      return False # The inventory is too full


class Character:
  def __init__(self, name, health):
    self.__name = name
    self.__health = health

  def GetName(self):
    return self.__name
  def GetHealth(self):
    return self.__health

class Weapon:
  def __init__(self, name, damage):
    self.__name = name
    self.__damage = damage

  def GetName(self):
    return self.__name
  def GetDamage(self):
    return self.__damage

  def UseWeapon(self, other):
    other.GetHealth().LoseHealth(self.__damage)