## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere


class Spell:

  name = ""
  lvl = 0
  spell_type = ""
  
  
  def __init__(self, *spell):
    self.name = spell[0]
    self.lvl = spell[1]
    self.spell_type = spell[2]
