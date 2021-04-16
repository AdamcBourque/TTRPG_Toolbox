## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere


class Spell:

  name = ""
  lvl = 0
  school = ""
  action = ""
  components = (0,0,"")
  duration = ""
  spell_range = 0
  ritual = 0
  description = ""
  
  
  def __init__(self, spell):
    self.name = spell[0]
    self.lvl = spell[1]
    self.school = spell[2]
    self.action = spell[3]
   # self.components = spell[4] + 
    self.duration = spell[7]
    self.spell_range = spell[8]
    self.ritual = spell[9]
    self.description = spell[10]


  def display():
    print("Not Implimented")
